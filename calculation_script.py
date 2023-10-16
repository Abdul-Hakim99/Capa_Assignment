#! /usr/bin/python3

import calculator

num1 = 15
num2 = 10

result_add = calculator.add(num1, num2)
result_sub = calculator.subtract(num1, num2)
result_multiple = calculator.multiple(num1, num2)
result_divide = calculator.divide(num1, num2)

print("Addition:", result_add)
print("Subtraction:", result_sub)
print("Multiplication", result_multiple)
print("Division:", result_divide)
