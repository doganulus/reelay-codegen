from antlr4 import *

from reelay.parser.EreLexer import EreLexer
from reelay.parser.EreParser import EreParser
from reelay.parser.EreVisitor import EreVisitor

def build(expression):
    lexer = EreLexer(InputStream(expression))
    stream = CommonTokenStream(lexer)
    parser = EreParser(stream)
    tree = parser.expr()

    # lisp_tree_str = tree.toStringTree(recog=parser)
    # print(lisp_tree_str)

    annotator = ClassicalAnnotator()
    size, nullable, output = annotator.annotate(tree)

    builder = ClassicalBuilder()
    trigger = builder.build(tree, set([0]))

    if nullable:
        output = output | set([0])

    return size, output, trigger

def write(size, output, trigger, language='cpp', filename='matcher.cpp'):

        coder = ClassicalCodeGenerator()

        if language == 'cpp':
            code = coder.generate_cpp_code(size, output, trigger)
        else:
            raise NotImplementedError 

        return code

class ClassicalAnnotator(EreVisitor):

    def __init__(self):
        super().__init__()
        self.num = 1

    def annotate(self, tree):
        return self.visit(tree)

    # Visit a parse tree produced by EreParser#Atomic.
    def visitAtomic(self, ctx:EreParser.AtomicContext):

        ctx.nullable = False
        ctx.output = set([self.num])
        ctx.position = self.num
        ctx.letter = ctx.child.getText()
        self.num = self.num + 1 

        return self.num, ctx.nullable, ctx.output

    def visitUnion(self, ctx:EreParser.UnionContext):
        self.visit(ctx.left)
        self.visit(ctx.right)

        ctx.nullable = ctx.left.nullable or ctx.right.nullable
        ctx.output = ctx.left.output | ctx.right.output

        return self.num, ctx.nullable, ctx.output

    # Visit a parse tree produced by EreParser#Concat.
    def visitConcat(self, ctx:EreParser.ConcatContext):

        self.visit(ctx.left)
        self.visit(ctx.right)

        ctx.nullable = ctx.left.nullable and ctx.right.nullable
        ctx.output = ctx.left.output | ctx.right.output if ctx.right.nullable else ctx.right.output

        return self.num, ctx.nullable, ctx.output

    # Visit a parse tree produced by EreParser#Star.
    def visitStar(self, ctx:EreParser.StarContext):

        self.visit(ctx.child)

        ctx.nullable = True
        ctx.output = ctx.child.output

        return self.num, ctx.nullable, ctx.output

    # Visit a parse tree produced by EreParser#Grouping.
    def visitGrouping(self, ctx:EreParser.GroupingContext):

        self.visit(ctx.child)

        ctx.nullable = ctx.child.nullable
        ctx.output = ctx.child.output

        return self.num, ctx.nullable, ctx.output

    # Visit a parse tree produced by EreParser#Question.
    def visitQuestion(self, ctx:EreParser.QuestionContext):

        self.visit(ctx.child)

        ctx.nullable = True
        ctx.output = ctx.child.output

        return self.num, ctx.nullable, ctx.output

    # Visit a parse tree produced by EreParser#Plus.
    def visitPlus(self, ctx:EreParser.PlusContext):

        self.visit(ctx.child)

        ctx.nullable = ctx.child.nullable 
        ctx.output = ctx.child.output

        return self.num, ctx.nullable, ctx.output

class ClassicalBuilder(EreVisitor):

    def __init__(self):
        super().__init__()

    def build(self, tree, trigger):
        tree.trigger = trigger
        return self.visit(tree)

    # Visit a parse tree produced by EreParser#Atomic.
    def visitAtomic(self, ctx:EreParser.AtomicContext):
        return [(ctx.position, ctx.letter, ctx.trigger)]

    def visitUnion(self, ctx:EreParser.UnionContext):
        left = self.build(ctx.left, ctx.trigger)
        right = self.build(ctx.right, ctx.trigger)

        return left + right

    # Visit a parse tree produced by EreParser#Concat.
    def visitConcat(self, ctx:EreParser.ConcatContext):

        left = self.build(ctx.left, ctx.trigger)

        if ctx.left.nullable:
            right = self.build(ctx.right, ctx.left.output | ctx.trigger)
        else:
            right = self.build(ctx.right, ctx.left.output)

        return left + right

    # Visit a parse tree produced by EreParser#Star.
    def visitStar(self, ctx:EreParser.StarContext):
        return self.build(ctx.child, ctx.child.output | ctx.trigger)

    # Visit a parse tree produced by EreParser#Grouping.
    def visitGrouping(self, ctx:EreParser.GroupingContext):
        return self.build(ctx.child, ctx.trigger)

    # Visit a parse tree produced by EreParser#Question.
    def visitQuestion(self, ctx:EreParser.QuestionContext):
        return self.build(ctx.child, ctx.child.output | ctx.trigger)

    # Visit a parse tree produced by EreParser#Plus.
    def visitPlus(self, ctx:EreParser.PlusContext):
        return self.build(ctx.child, ctx.child.output | ctx.trigger)

class ClassicalCodeGenerator:

    def generate_cpp_code(self, size, output, trigger, partial=True):

        statements = [
            '#include <iostream>',
            '#include <fstream>', 
            '#include <cstring>', 
            '',
            'int main(int argc, char **argv) {',            
            ]

        statements.append('\tbool state[{size}] = {{1,{rest}}};'.format(size=size, rest=','.join([str(0) for i in range(size-1)])))
        statements.append('\tbool next_state[{size}] = {{{rest}}};'.format(size=size, rest=','.join([str(0) for i in range(size)])))
        # statements.append('\tstd::string word;')
        statements.append('\tstd::ifstream ifs(argv[1]);')
        statements.append('\tstd::string word((std::istreambuf_iterator<char>(ifs)),(std::istreambuf_iterator<char>()));')
        
        statements.append('\tfor (char letter : word){')
        if partial:
            statements.append('\t\tnext_state[0] = 1; // Start anywhere')
        else:
            statements.append('\t\tnext_state[0] = 0; // Start from the beginning')

        for position, letter, trigger in trigger:
            trig_cond = ' or '.join(['state[{}]'.format(i) for i in trigger])
            statements.append('\t\tnext_state[{}] = (letter == \'{}\') and ({});'.format(position, letter, trig_cond))

        statements.append('\t\tstd::memcpy(state, next_state, sizeof(state));')
        statements.append('\t}')

        output_cond = ' or '.join(['state[{}]'.format(i) for i in output])
        statements.append('\tstd::cout << ({}) << std::endl;'.format(output_cond))
        statements.append('}')

        generated_code = '\n'.join(statements)

        return generated_code