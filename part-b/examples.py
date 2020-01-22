from propositional_logic import *

T = BoolConst(True)
F = BoolConst(False)
A = BoolVar("A")
B = BoolVar("B")

# some formulas f1, f2, f3 with just constants
f1 = And(T, F)
print(f1)
print(f1.format())
print()

f2 = Or(T, T)
print(f2)
print(f2.format())
print()

f3 = Implies(f1, Not(f2))
print(f3)
print(f3.format())
print()

# some formulas f4, f5, f6 with variables too
f4 = And(f1, A)
print(f4)
print(f4.format())
print()

f5 = Iff(f4, f1)
print(f5)
print(f5.format())
print()

f6 = Not(f5)
print(f6)
print(f6.format())
print()
