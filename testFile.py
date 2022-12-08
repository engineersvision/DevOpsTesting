from operator import add, mul
from math import pi

print(mul(2,3))

## Structure of call expression
# Operator ( Operand, Operand )
# Operator and operands are also expression to evaluate.

print(mul(add(2,mul(4,6)),add(3,5)))

rad = 5.0
area,radius = pi * pow(rad,2.0), 2 * pi * rad
print(area,radius)

f = max
print(f(1,3,2))

