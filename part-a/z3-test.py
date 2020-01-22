from z3 import *

a = Bool('a')
b = Bool('b')

x = Int('x')
y = Int('y')

f = And(Not(a), b, x > 0, x < 100, x < y)

solver = Solver() 

solver.add(f)
print(solver)

f_check = solver.check()

print(f_check)
if(f_check == sat):
	print(solver.model())

print()

solver.add(y < 1)
print(solver)

f_check = solver.check()
print(f_check)
if(f_check == sat):
	print(solver.model())
