import math
def calculator(num1, num2, operator):
    try:
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            return num1 / num2
        elif operator == '**':
            return int(num1 ** 0.5)
        elif operator == 'log':
            return math.log(num1)
        else:
            return 'Invalid operator. Please use one of the given operators listed.'
    except Exception as e:
        return 'Error occurred: {e}'
    
operator = input('Enter Operator (+, -, *, /, **(for square root), log): ')
num1 = float(input('Enter first number: '))
if (operator == '**' or operator == 'log'):
    print(calculator(num1, 0, operator))
else:
    num2 = float(input('Enter second number: '))
    print(calculator(num1, num2, operator))