from myfunctions import *
import random

def say_hello(name):
    print("Hello {0}!".format(name))

def say_hello_1(name):
    print("Hello %s!" %name)

def say_hello_2(name):
    print("Hello"+" "+name+"!")

#functiondefinition
def print_hello_world():
    print("Hello World")

def print_name(forename, surname):
    print(forename+" "+surname)

#functioncall
print_hello_world()
print_name("Raphael","Schermann")
print_name("Max","Müller")
say_hello("Raphael")
say_hello_1("Raphael")
say_hello_2("Raphael")
num1 = int(input("Enter a number 1"))
num2 = int(input("Enter a number 2"))
opt = input("enter a operaton (+ or *)")
result = 0
if(opt =="+"):
    result = my_addition(num1, num2)
elif(opt =="*"):
    result = my_multiplication(num1, num2)
else:
    print("wrong operation")
print(result)

print(my_addition(random.randint(1,20),random.randint(1,20)))

#recap
def my_recap_hello_world():
    print("Hello World")

my_recap_hello_world()

def my_recap_input_summazion(a,b):
    print(a+b)

def my_recap_input_output_summazion(a,b):
    return (a+b)


my_recap_input_summazion(1,2)
result = my_recap_input_output_summazion(1,2)
print(result)
result = my_recap_input_output_summazion(result,3)
print(result)


