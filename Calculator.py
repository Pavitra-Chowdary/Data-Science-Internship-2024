n1 = float(input('Enter first number: '))
n2 = float(input('Enter second number: '))
add = n1 + n2
sub = n1 - n2
mult = n1 * n2
if n2!= 0:
    div = n1 / n2
else:
    div = "Zero Division error"
print('Addition:', n1, '+', n2, '=', add)
print('Subtraction:', n1, '-', n2, '=', sub)
print('Multiplication:', n1, '*', n2, '=', mult)
print('Division:', n1, '/', n2, '=', div)
