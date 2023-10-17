a=9
b="misty"
print(a)
print(b)
print(type(a))
print(type(b))
c=a
a=b
b=c
print(a)
print(b)
print(type(a))
print(type(b))

d=45.78
e=100
f=23.65
print(d)
print(e)
print(f)
print(type(d))
print(type(e))
print(type(f))

g=int(d)
h=float(e)
i=str(f)
print(g)
print(h)
print(i)
print(type(g))
print(type(h))
print(type(i))

Number_1=575
Number_2=275
add_result=Number_1 + Number_2
print(add_result)
Minus_result=Number_1 - Number_2
print(Minus_result)
Divide_result=Number_1 / Number_2
print(Divide_result)
Times_result=Number_1 * Number_2
print(Times_result)

Number_1= input("Enter a number:")
Number_2= input("Enter another number:")
result= float(Number_1) + float(Number_2)
print(result)

num1 = 78
num2 = 125
result = add(num1, num2)
print(result)
num1 = 321
num2= 122
result = add(num1, num2)
print(result)

def add(num1, num2):
    result = float(num1) + float(num2)
    print(result)

def subtract(num1, num2):
    result = float(num1) - float(num2)
    print(result)

def multiply(num1, num2):
    result = float(num1) 
