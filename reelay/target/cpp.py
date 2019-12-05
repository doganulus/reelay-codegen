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

        # self.include = ["array", "reelay/discrete_time.hpp"] + include
        self.include = ["array", "discrete_time.hpp"] + include


    def generate(self, states=None, meta=None):

        # labeled_states = self.label(states)

        for library in self.include:
            self.statements.append('#include "{}"'.format(library))

        self.statements.append('')

       
        self.statements.append('template<typename T = int>')
        self.statements.append('struct Monitor{} '.format(meta['name']) + '{')
        self.statements.append('')

        if meta['bnum'] > 0:
            self.statements.append('\tstd::array<bool,{size}> {name} = std::array<bool,{size}>{init};'.format(size=meta['bnum'], name=self.now, init='{' + ','.join(['0' for i in range(meta['bnum'])]) + '}'))
            self.statements.append('\tstd::array<bool,{size}> {name} = std::array<bool,{size}>{init};'.format(size=meta['bnum'], name=self.pre, init='{' + ','.join(['0' for i in range(meta['bnum'])]) + '}' ))
            self.statements.append('')

        if meta['tnum'] > 0:
            self.statements.append('\tstd::array<interval_set<T>,{size}> {name} = std::array<interval_set<T>,{size}>{init};'.format(size=meta['tnum'], name=self.tnow, init='{' + ','.join(['interval_set<T>()' for i in range(meta['tnum'])]) + '}'))
            self.statements.append('\tstd::array<interval_set<T>,{size}> {name} = std::array<interval_set<T>,{size}>{init};'.format(size=meta['tnum'], name=self.tpre, init='{' + ','.join(['interval_set<T>()' for i in range(meta['tnum'])]) + '}' ))
            self.statements.append('')

        if meta['tnum'] > 0:
            self.statements.append('\tT now = 0;')
            self.statements.append('')

        # for vartype, varname in meta['vars']:
        #     self.statements.append("\t{} {};".format(vartype, varname))
        # self.statements.append('')
        #
        # Currently this part is a hack - to be changed
        #
        update_args = ['{} {}'.format(v[0], v[1].split('.')[0]) for v in sorted(meta['vars'])]
        self.statements.append('\tbool update({})'.format(', '.join(update_args)) + '{') 

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

        self.statements.append('')
        self.statements.append('\t\treturn output();')
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

    def visitOnceUpdate(self, obj):
        return "({} or {})".format(self.visit(obj.children[0]), self.visit(obj.children[1]))
        # return "{} = {};".format(obj.variable, self.visit(obj.update))

    def visitAlwaysUpdate(self, obj):
        return "({} and {})".format(self.visit(obj.children[0]), self.visit(obj.children[1]))
        # return "{} = {};".format(obj.variable, self.visit(obj.update))

    def visitPreviousUpdate(self, obj):
        return "{}".format(self.visit(obj.children[1]))

    def visitSinceUpdate(self, obj):
        return "{} or ({} and {})".format(self.visit(obj.children[2]), self.visit(obj.children[1]), self.visit(obj.children[0]))
        # return "{} = {};".format(obj.variable, self.visit(obj.update))

    def visitPreviousOutput(self, obj):
        return "{}".format(self.visit(obj.children[0]))

    def visitTemporalOutput(self, obj):
        return "{}".format(self.visit(obj.children[0]))

    def visitTimedSetSinceUpdate(self, obj):
        if obj.u != None:
            return "update_timed_since<T>({state}, now, {left}, {right}, {l}, {u})".format(state=self.visit(obj.children[0]), left=self.visit(obj.children[1]), right=self.visit(obj.children[2]), l=obj.l, u=obj.u)
        else:
            return "update_timed_since_unbounded<T>({state}, now, {left}, {right}, {l})".format(state=self.visit(obj.children[0]), left=self.visit(obj.children[1]), right=self.visit(obj.children[2]), l=obj.l) 

    def visitTimedSetSinceOutput(self, obj):
            return "output_timed_since<T>({state}, now)".format(state=self.visit(obj.children[0]))

    def visitTimedSetState(self, obj):
        return "{}[{}]".format(self.tnow, obj.variable)
        # return "{} = {};".format(obj.variable, self.visit(obj.update))














class StructGeneratorDense(Visitor):

    def __init__(self, include=[], atoms=dict(), now="states"):

        super().__init__()
        self.statements = []

        self.now = now
        self.pre = self.now + '_pre'

        # self.include = ["array", "reelay/discrete_time.hpp"] + include
        self.include = ["array", "dense_time.hpp"] + include


    def generate(self, states=None, meta=None):

        self.meta = meta

        for library in self.include:
            self.statements.append('#include "{}"'.format(library))

        self.statements.append('')

        self.statements.append('template<typename T = int>')
        self.statements.append('struct Monitor{} '.format(meta['name']) + '{')
        self.statements.append('')

        self.meta['num'] = self.meta['bnum'] + self.meta['tnum']

        self.statements.append('\tstd::array<interval_set<T>,{size}> {name} = std::array<interval_set<T>,{size}>{init};'.format(size=self.meta['num'], name=self.now, init='{' + ','.join(['interval_set<T>()' for i in range(self.meta['num'])]) + '}'))
        self.statements.append('\tstd::array<interval_set<T>,{size}> {name} = std::array<interval_set<T>,{size}>{init};'.format(size=self.meta['num'], name=self.pre, init='{' + ','.join(['interval_set<T>()' for i in range(self.meta['num'])]) + '}' ))
        self.statements.append('')

        self.statements.append('\tinterval_set<T> current = interval_set<T>(interval<T>::left_open(-1, 0));')
        self.statements.append('')

        # for vartype, varname in meta['vars']:
        #     self.statements.append("\t{} {};".format(vartype, varname))
        # self.statements.append('')
        #
        # Currently this part is a hack - to be changed
        #
        update_args = ['{} {}'.format(v[0], v[1].split('.')[0]) for v in sorted(self.meta['vars'])]
        self.statements.append('\tinterval_set<T> update(T now, {})'.format(', '.join(update_args)) + '{') 

        self.statements.append('')
        
        self.statements.append('\t\tcurrent = interval_set<T>(interval<T>::left_open(current.begin()->upper(), now));')

        self.statements.append('\t\t{pre} = {now};'.format(now=self.now, pre=self.pre))
        self.statements.append('')

        for state in states:
            self.statements.append('\t\t' + "{} = {};".format(self.visit(state), self.visit(state.update)))

        self.statements.append('')
        self.statements.append('\t\treturn output();')
        self.statements.append('\t}')
        self.statements.append('')
        self.statements.append('\tinterval_set<T> output()' + '{')
        self.statements.append('\t\treturn {};'.format(self.visit(self.meta['output'])))
        self.statements.append('\t}')
        self.statements.append('};')

        code = '\n'.join(self.statements)

        return code

    def visitNow(self, obj):
        return "{}[{}]".format(self.now, obj.state.variable)

    def visitPre(self, obj):
        return "{}[{}]".format(self.pre, obj.state.variable)

    def visitConstant(self, obj):
        if obj.name == "true":
            return "current"
        else:
            return obj.name

    def visitAtom(self, obj):
        if obj.args == []:
            return 'prop(current, {})'.format(obj.name)
        else:
            str_args = [self.visit(c) for c in obj.args]
            return obj.name + '({})'.format(','.join(str_args))

    def visitBooleanNot(self, obj):
        return "(current - {})".format(self.visit(obj.children[0]))

    def visitBooleanOr(self, obj):
        return '(' + " + ".join([self.visit(c) for c in obj.children]) + ')'

    def visitBooleanAnd(self, obj):
        return '(' + " & ".join([self.visit(c) for c in obj.children]) + ')'

    def visitBooleanState(self, obj):
        return "{}[{}]".format(self.now, obj.variable)
        # return "{} = {};".format(obj.variable, self.visit(obj.update))

    def visitOnceUpdate(self, obj):
        return "update_timed_since_unbounded<T>({state}, current, current, {right}, {l})".format(state=self.visit(obj.children[0]), right=self.visit(obj.children[1]), l=0)

    def visitAlwaysUpdate(self, obj):
        return "update_timed_since_unbounded<T>({state}, current, current, {right}, {l})".format(state=self.visit(obj.children[0]), right=self.visit(obj.children[1]), l=0)

    def visitSinceUpdate(self, obj):
        return "update_timed_since_unbounded<T>({state}, current, {left}, {right}, {l})".format(state=self.visit(obj.children[0]), left=self.visit(obj.children[1]), right=self.visit(obj.children[2]), l=0)

    def visitTemporalOutput(self, obj):
            return "output_timed_since<T>({state}, current)".format(state=self.visit(obj.children[0]))

    def visitTimedSetSinceUpdate(self, obj):
        if obj.u != None:
            return "update_timed_since<T>({state}, current, {left}, {right}, {l}, {u})".format(state=self.visit(obj.children[0]), left=self.visit(obj.children[1]), right=self.visit(obj.children[2]), l=obj.l, u=obj.u)
        else:
            return "update_timed_since_unbounded<T>({state}, current, {left}, {right}, {l})".format(state=self.visit(obj.children[0]), left=self.visit(obj.children[1]), right=self.visit(obj.children[2]), l=obj.l) 

    def visitTimedSetSinceOutput(self, obj):
            return "output_timed_since<T>({state}, current)".format(state=self.visit(obj.children[0]))


    def visitTimedSetState(self, obj):
        return "{}[{}]".format(self.now, self.meta['bnum'] + obj.variable)
        # return "{} = {};".format(obj.variable, self.visit(obj.update))