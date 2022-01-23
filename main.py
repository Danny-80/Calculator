# Calculator 
from art import logo

# Add
def add(n1,n2):
	return n1 + n2

# Subtract
def subtraction(n1,n2):
	return n1 - n2

# Multiplication
def multiplication(n1,n2):
	return n1 * n2

# Division
def division(n1,n2):
	return n1 / n2

operations = {
	'+': add,
	'-': subtraction,
	'*': multiplication,
	'/': division
	}

def calculator():
	print(logo)
	num1 = float(input('What is the first number?: '))
	for symbol in operations:
		print(symbol)

	do_calculation = True
	while do_calculation:
		operation_symbol = input('Pick an operation from the line above: ')
		num2 = float(input('What is the next number ?: '))
		calculation_function = operations[operation_symbol]
		answer = calculation_function(num1,num2)
		print(f'{num1} {operation_symbol} {num2} = {answer}')
		user_choice = input(f'Type "y" to continue calculating with {answer}, or type "n" to start a new calculatin.: ').lower()

		if user_choice == 'y':
			num1 = answer
		else:
			do_calulation = False
			calculator()
			print('Thank you for using the calculator')


calculator()


