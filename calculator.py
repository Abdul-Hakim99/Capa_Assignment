#! /usr/bin/python3

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiple(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."
