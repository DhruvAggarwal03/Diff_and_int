from sympy import *
x=symbols('x')
expr_input=input('Enter an expression in terms of x : ')
lower_limit=float(input('Enter lower limit of integration : '))
upper_limit=float(input('Enter upper limit of integration : '))
expr=sympify(expr_input)
derivative=diff(expr,x)
integration=integrate(expr,x)
def_integration=integrate(expr,(x,lower_limit,upper_limit))
print(f'''Original Function : {expr}
Derivative : {derivative}
Integration : {integration}
Definite Integration : {def_integration}''')
