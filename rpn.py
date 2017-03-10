#!/usr/bin/env python3

def calculate(arg):
	stack = list()
	
	for val in arg:
		if val == '-':
			return (stack.pop() - stack.pop()) * (-1)
		elif val == '+':
			return (stack.pop() + stack.pop())
		else:
			stack.append(arg)
	
def main():
	while True:
		calculate(input("rpn calc> "))
		
if __name__ == '__main__': # Note: that's "underscore underscore n a m e ..."
	main()
