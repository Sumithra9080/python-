##Functions in Python
What is a Function?

A function is a block of code used to perform a specific task.

Instead of writing the same code again and again, we can create a function and call it whenever we need it.


               Basic Syntax
               def function_name():
              # code

Types of Functions in Python

1. Pre-defined / Built-in Functions

These functions are already provided by Python. We don't need to create them.
name = "Sumithra"

print(len(name))
print(type(name))


print()
len()
type()
max()
min()
sum()
input()
Simple example
numbers = [10, 20, 30]

print(max(numbers))
print(min(numbers))
print(sum(numbers))
2. User-defined Function
A user-defined function is a function created by the programmer using def
def greet():
    print("Hello")

greet()
With arguments
def add(a, b):
    print(a + b)

add(10, 20)
3. Lambda Function
A lambda function is a small function written in one line.
square = lambda x: x * x

print(square(5))
Two arguments
add = lambda a, b: a + b

print(add(10, 20))
Lambda = Small one-line function

4. Return Function

return is used to send a result back from a function.
def add(a, b):
    return a + b

result = add(10, 20)

print(result)


Difference between print and return

Using print:

def add(a, b):
    print(a + b)

add(10, 20)

Using return:
def add(a, b):
    return a + b

x = add(10, 20)
print(x)
The result can be stored and used later.
5. Recursive Function
Recursion means a function calls itself.

It must have a stopping condition.
def count(n):
    if n == 0:
        return

    print(n)
    count(n - 1)

count(5)


Recursive Example – Factorial
def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))
Type	                  Meaning	                                   Example
Pre-defined	   Already available in Python	    len(), sum()
User-defined	   Created by programmer	    def add()
Lambda	                   Small one-line function	   lambda x: x*x
Return	                  Sends result back	                   return a+b
Recursion	Function     calls itself	                    factorial()

















1. Function without Arguments
A function that does not take any input.
def greet():
    print("Hello")

greet()    #greet() is the function call.


2. Function with Arguments
A function that receives values as input.

def greet(name):
    print("Hello", name)

greet("Sumithra")

Here, name is an argument/parameter.


3. Function with Return Value

A function can return a result using return.

def add(a, b):
    return a + b

result = add(10, 20)
print(result)

return sends the result back to the calling statement.




