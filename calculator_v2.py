
prompt = input('\nEnter operator: ')
def addition(a, b): 
    print(f'\n>>> {a + b} <<<')

def subtraction(a, b):
    print(f'\n>>> {a - b} <<<')

def multiplication(a, b):
    print(f'\n>>> {a * b} <<<')

def modular(a, b):
    print(f'\n>>> {a % b} <<<')

def division(a, b):
    print(f'\n>>> {a / b} <<<')

def exponentiation(a, b):
    print(f'>>> {a ** b} <<<')

if prompt == '+':
    add = int(input())
    add2 = int(input())
    addition(add, add2)

elif prompt == '-':
    sub = int(input())
    sub2 = int(input())
    subtraction(sub, sub2)

elif prompt == 'x':
    mult = int(input())
    mult2 = int(input())
    multiplication(mult, mult2)
elif prompt == '%':
    mod = int(input())
    mod2 = int(input())
    modular(mod, mod2)

elif prompt == '/':
    div = int(input())
    div2 = int(input())
    division(div, div2)

elif prompt == '^':
    exp = int(input())
    exp2 = int(input())
    exponentiation(exp, exp2)