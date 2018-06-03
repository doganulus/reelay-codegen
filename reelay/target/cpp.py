from reelay.machine.boolean import *
from reelay.machine.timed import *

class Visitor:
    def visit(self, obj):
        func_name = 'visit' + obj.__class__.__name__
        visit_func = getattr(self, func_name)
        return visit_func(obj)

class StructGenerator(Visitor):

    def __init__(self, include=[], atoms=dict(), now="states"):

        super().__init__()
        self.statements = []

        self.now = now
        self.tnow = "t" + now

        self.pre = self.now + '_pre'
        self.tpre = self.tnow + '_pre'

        self.include = ["array", "common.hpp", "discrete_time.hpp"] + include

    def generate(self, states=None, meta=None):

        # labeled_states = self.label(states)

        for library in self.include:
            self.statements.append('#include "{}"'.format(library))

        self.statements.append('')

        self.statements.append('struct Monitor{} '.format(meta['name']) + '{')
        self.statements.append('')

        if meta['bnum'] > 0:
            self.statements.append('\tstd::array<bool,{size}> {name} = std::array<bool,{size}>{init};'.format(size=meta['bnum'], name=self.now, init='{' + ','.join(['0' for i in range(meta['bnum'])]) + '}'))
            self.statements.append('\tstd::array<bool,{size}> {name} = std::array<bool,{size}>{init};'.format(size=meta['bnum'], name=self.pre, init='{' + ','.join(['0' for i in range(meta['bnum'])]) + '}' ))
            self.statements.append('')

        if meta['tnum'] > 0:
            self.statements.append('\tstd::array<timed_set,{size}> {name} = std::array<timed_set,{size}>{init};'.format(size=meta['tnum'], name=self.tnow, init='{' + ','.join(['timed_set()' for i in range(meta['tnum'])]) + '}'))
            self.statements.append('\tstd::array<timed_set,{size}> {name} = std::array<timed_set,{size}>{init};'.format(size=meta['tnum'], name=self.tpre, init='{' + ','.join(['timed_set()' for i in range(meta['tnum'])]) + '}' ))
            self.statements.append('')

        if meta['tnum'] > 0:
            self.statements.append('\tint now = 0;')
            self.statements.append('')

        # for vartype, varname in meta['vars']:
        #     self.statements.append("\t{} {};".format(vartype, varname))
        # self.statements.append('')

        self.statements.append('\tvoid update({})'.format(', '.join(['{} {}'.format(v[0], v[1]) for v in sorted(meta['vars'])])) + '{') 

        self.statements.append('')
        
        if meta['tnum'] > 0:
            self.statements.append('\t\tnow = now + 1;')

        if meta['bnum'] > 0:
            self.statements.append('\t\t{pre} = {now};'.format(now=self.now, pre=self.pre))
        if meta['tnum'] > 0:
            self.statements.append('\t\t{pre} = {now};'.format(now=self.tnow, pre=self.tpre))

        self.statements.append('')

        for state in states:
            self.statements.append('\t\t' + "{} = {};".format(self.visit(state), self.visit(state.update)))

        self.statements.append('\t}')
        self.statements.append('')
        self.statements.append('\tbool output()' + '{')
        self.statements.append('\t\treturn {};'.format(self.visit(meta['output'])))
        self.statements.append('\t}')
        self.statements.append('};')

        code = '\n'.join(self.statements)

        return code

    def visitNow(self, obj):
        return "{}[{}]".format(self.now, obj.state.variable)

    def visitPre(self, obj):
        return "{}[{}]".format(self.pre, obj.state.variable)

    def visitConstant(self, obj):
        return obj.name

    def visitAtom(self, obj):
        if obj.args == []:
            return obj.name
        else:
            str_args = [self.visit(c) for c in obj.args]
            return obj.name + '({})'.format(','.join(str_args))

    def visitBooleanNot(self, obj):
        return "not({})".format(self.visit(obj.children[0]))

    def visitBooleanOr(self, obj):
        return '(' + " or ".join([self.visit(c) for c in obj.children]) + ')'

    def visitBooleanAnd(self, obj):
        return '(' + " and ".join([self.visit(c) for c in obj.children]) + ')'

    def visitBooleanState(self, obj):
        return "{}[{}]".format(self.now, obj.variable)
        # return "{} = {};".format(obj.variable, self.visit(obj.update))

    def visitTimedSetSinceUpdate(self, obj):
        if obj.u != None:
            return "update_timed_since({state}, {left}, {right}, {u}, now)".format(state=self.visit(obj.children[0]), left=self.visit(obj.children[1]), right=self.visit(obj.children[2]), u=obj.u)
        else:
            return "update_timed_since_unbounded({state}, {left}, {right}, {l}, now)".format(state=self.visit(obj.children[0]), left=self.visit(obj.children[1]), right=self.visit(obj.children[2]), l=obj.l) 

    def visitTimedSetSinceOutput(self, obj):
        if obj.l != None:
            return "output_timed_since({state}, {l}, now)".format(state=self.visit(obj.children[0]), l=obj.l)
        else:
            return "output_timed_since_unbounded({state}, now)".format(state=self.visit(obj.children[0]))

    def visitTimedSetState(self, obj):
        return "{}[{}]".format(self.tnow, obj.variable)
        # return "{} = {};".format(obj.variable, self.visit(obj.update))



