from frozendict import frozendict


class DiscreteFiniteFunc:
    def __init__(self, vars_and_symbols___dict, vars_and_values___dict, conditions={}, scope={}):
        self.Vars = vars_and_symbols___dict
        self.Conditions = conditions
        self.Scope = scope
        self.Mappings = vars_and_values___dict
        self.ConditionInstances = None

    def at(self):
        pass

    def max(self):
        pass

    def min(self):
        pass

    def sum(self):
        pass

    def condition(self):
        pass

    def marginalize(self):
        pass

    def __add__(self, other):
        pass

    def __radd__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __rsub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __rmul__(self, other):
        pass

    def __div__(self, other):
        pass

    def __rdiv__(self, other):
        pass

    def __pow__(self, power, modulo=None):
        pass

    def __rpow__(self, power, modulo=None):
        pass

