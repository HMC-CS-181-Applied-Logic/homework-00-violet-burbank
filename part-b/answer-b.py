from propositional_logic import *

A = BoolVar('A')
B = BoolVar('B')
C = BoolVar('C')

# write code using A, B, and C, along with 
# the classes from propositional_logic.py
# and the .format() mathod to output the
# following expression:

# (((A => B) & (B => C)) => (A => C))

f_ans = Implies(And(Implies(A, B), Implies(B, C)), Implies(A, C))
print(f_ans)
print(f_ans.format())