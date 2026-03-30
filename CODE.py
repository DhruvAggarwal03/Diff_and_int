PI = 3.141592653589793

def factorial(n):
    result = 1
    for i in range (1, n+1):
        result *= i

    return result

# sin and cos

def sin(x):
    x = x % (2*PI)
    result = 0
    for n in range(15):
        term = pow(-1, n) * pow(x, 2*n+1)/ factorial(2*n+1)
        result += term
    return result

def cos(x):
    x = x % (2*PI)
    result = 0
    for n in range(15):
        term = pow(-1, n) * pow(x, 2*n)/factorial(2*n)
        result += term
    return result


def tokenize(expr):
    tokens = []
    num = ""
    i = 0

    while i < len(expr):
        if expr[i].isdigit() or expr[i] == '.':
            num += expr[i]
        else:
            if num:
                tokens.append(float(num))
                num = ''
            if expr[i] != ' ':
                tokens.append(expr[i])
        i += 1

    if num:
        tokens.append(float(num))

    return tokens

def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0


def infix_to_postfix(tokens):
    output = []
    stack = []

    for token in tokens:
        if isinstance(token, float):
            output.append(token)

        elif token == '(':
            stack.append(token)

        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        
        elif token in ('+','-','*','/'):
            while stack and precedence(stack[-1]) >= precedence(token):
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())
        
    return output
    

def evaluate_postfix(postfix):
    stack = []

    for token in postfix:
        if isinstance(token, float):
            stack.append(token)
        
        else:
            b = stack.pop()
            a = stack.pop()
            
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)

    return stack[0]
    

def evaluate(expr):
    expr = expr.replace("pi", str(PI))
    
    # handle sin and cos manually
    if expr.startswith("sin("):
        val = evaluate(expr[4:-1])
        return sin(val)
    
    if expr.startswith("cos("):
        val = evaluate(expr[4:-1])
        return cos(val)
    
    tokens = tokenize(expr)
    postfix = infix_to_postfix(tokens)
    return evaluate_postfix(postfix)


def differentiate(expr, x):
    h = 0.0001
    return (evaluate(expr.replace("x", str(x + h))) - 
            evaluate(expr.replace("x", str(x)))) / h

def integrate(expr, a, b, n=1000):
    step = (b - a) / n
    total = 0
    
    for i in range(n):
        x1 = a + i * step
        x2 = a + (i + 1) * step
        
        y1 = evaluate(expr.replace("x", str(x1)))
        y2 = evaluate(expr.replace("x", str(x2)))
        
        total += (y1 + y2) * step / 2
    
    return total

#  MAIN LOOP 
while True:
    print("\n1. Calculate")
    print("2. Differentiate")
    print("3. Integrate")
    print("4. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == '1':
        expr = input("Enter expression: ")
        print("Result:", evaluate(expr))
    
    elif choice == '2':
        expr = input("Enter function in x: ")
        x = float(input("Enter x: "))
        print("Derivative:", differentiate(expr, x))
    
    elif choice == '3':
        expr = input("Enter function in x: ")
        a = float(input("Lower limit: "))
        b = float(input("Upper limit: "))
        print("Integral:", integrate(expr, a, b))
    
    elif choice == '4':
        break
