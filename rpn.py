#!/usr/bin/env python3

import operator
import colorama
from colorama import Fore, Back, Style
#from termcolor import colored
colorama.init()

#operators = {
    #'+': operator.add,
    #'-': operator.sub,
    #'*': operator.mul,
    #'/': operator.truediv,
    #'^': operator.pow,
    #'%': operator.mod,
#}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            if token  == '+':
                arg2 = stack.pop()
                arg1 = stack.pop()
                result = operator.add(arg1, arg2)
                stack.append(result)
            if token  == '-':
                arg2 = stack.pop()
                arg1 = stack.pop()
                result = operator.sub(arg1, arg2)
                stack.append(result)
            if token  == '*':
                arg2 = stack.pop()
                arg1 = stack.pop()
                result = operator.mul(arg1, arg2)
                stack.append(result)
            if token  == '/':
                arg2 = stack.pop()
                arg1 = stack.pop()
                result = operator.truediv(arg1, arg2)
                stack.append(result)
            if token  == '^':
                arg2 = stack.pop()
                arg1 = stack.pop()
                result = operator.pow(arg1, arg2)
                stack.append(result)
            if token  == '%':
                arg2 = stack.pop()
                arg1 = stack.pop()
                result = operator.mod(arg1, arg2)
                stack.append(result)
        #print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        if result < 0:
            print("Result: " + Fore.RED + str(result))
            print(Style.RESET_ALL)
        else:
            print("Result: ", result)

if __name__ == '__main__':
    main()
