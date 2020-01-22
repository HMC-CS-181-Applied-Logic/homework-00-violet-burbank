class Expression(object):
    def __init__(self):
        super()
    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__
    def __ne__(self, other):
        return not self.__eq__(other)
    def __str__(self):
        return self.__class__.__name__ + "(" + ", ".join([str(v) for v in self.__dict__.values()]) + ")"
    def __repr__(self):
        return str(self)
    def __hash__(self):
        return(hash(str(self)))

class Boolean(Expression):
    def __init__(self):
        super()

class BoolConst(Boolean):
    def __init__(self, val):
        self.val = val
    def format(self):
        return "T" if self.val else "F"

class BoolVar(Boolean):
    def __init__(self, name):
        self.name = name
    def format(self):
        return str(self.name)

class Not(Boolean):
    def __init__(self, exp):
        self.exp = exp
    def format(self):
        return "~" + self.exp.format()

class And(Boolean):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def format(self):
        return "(" + self.exp1.format() + " & " + self.exp2.format() + ")"

class Or(Boolean):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def format(self):
        return "(" + self.exp1.format() + " | " + self.exp2.format() + ")"

class Implies(Boolean):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def format(self):
        return "(" + self.exp1.format() + " => " + self.exp2.format() + ")"

class Iff(Boolean):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def format(self):
        return "(" + self.exp1.format() + " <=> " + self.exp2.format() + ")"
