#task-1:



# Integer (int)
age = 18

# Float
height = 5.8

# String (str)
name = "Raj"

# Boolean (bool)
is_student = True

# List
fruits = ["Apple", "Banana", "Mango"]

# Tuple
colors = ("Red", "Green", "Blue")

# Set
numbers = {1, 2, 3, 4}

# Dictionary
student = {
    "name": "Raj",
    "age": 18
}

print(type(age))
print(type(height))
print(type(name))
print(type(is_student))
print(type(fruits))
print(type(colors))
print(type(numbers))
print(type(student))


#task-2:
# arithmatic operator:
a = 10
b = 5

print(a + b)   
print(a - b)   
print(a * b)   
print(a / b)   
print(a % b)   
print(a ** b)  
print(a // b)  

#assingment operator:
x = 10

x += 5
print(x)
x -= 2
print(x)
x *= 3
print(x)
x /= 2
print(x)

#ternary operator:
a = 10
b = 20

greater = a if a > b else b

print("Greater Number =", greater)

#Comparison Operators:
a = 10
b = 5

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

#logical operator:
a = True
b = False

print(a and b)
print(a or b)
print(not a)

#identity operator:
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)
print(a is c)
print(a is not c)

#membership operator:
fruits = ["Apple", "Banana", "Mango"]

print("Apple" in fruits)
print("Orange" in fruits)

#Bitwise Operators:
a = 5    
b = 3    

print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << 1)
print(a >> 1)

#task-3
#list:

#create a list:
fruits = ["Apple", "Banana", "Mango"]
print(fruits)
#add items:
fruits = ["Apple", "Banana", "Mango"]
fruits.append("Orange")
print(fruits)
#print:
fruits = ["Apple", "Banana", "Mango"]
print(fruits)
#update:
fruits = ["Apple", "Banana", "Mango"]
fruits[1] = "Orange"
print(fruits)
#remove:
fruits = ["Apple", "Banana", "Mango"]
fruits.remove("Banana")
print(fruits)
#delet intire list:
fruits = ["Apple", "Banana", "Mango"]
del fruits

#task-4:
#Tuple

#create a tuple:
fruits = ("Apple", "Banana", "Mango")
print(fruits)
#add items:
fruits = ("Apple", "Banana")
fruits = fruits + ("Mango",)
print(fruits)
#update:
fruits = ("Apple", "Banana", "Mango")
temp = list(fruits)
temp[1] = "Orange"
fruits = tuple(temp)
print(fruits)
#remove:
fruits = ("Apple", "Banana", "Mango")
temp = list(fruits)
temp.remove("Banana")
fruits = tuple(temp)
print(fruits)
#delete intire tuple:
fruits = ("Apple", "Banana", "Mango")
del fruits


#task-5:
#Set:

#create a set:
fruits = {"Apple", "Banana", "Mango"}
print(fruits)
#add items:
fruits = {"Apple", "Banana", "Mango"}
fruits.add("Orange")
print(fruits)
#update:
fruits = {"Apple", "Banana"}
fruits.update(["Mango", "Orange"])
print(fruits)
#remove:
fruits = {"Apple", "Banana", "Mango"}
fruits.remove("Apple")
print(fruits)
#delete intire set:
fruits = {"Apple", "Banana", "Mango"}
del fruits




#task-6:
#dictionary:

#create a dictionary:
student = {
    "name": "Raj",
    "age": 18,
    "city": "Ahmedabad"
}
print(student)
#add items:
student = {
    "name": "Raj",
    "age": 18
}
student["city"] = "Ahmedabad"
print(student)
#update:
student = {
    "name": "Raj",
    "age": 18
}
student["age"] = 20
print(student)
#remove:
student = {
    "name": "Raj",
    "age": 18,
    "city": "Ahmedabad"
}
student.pop("age")
print(student)
#delete intire dictionary:
student = {
    "name": "Raj",
    "age": 18,
    "city": "Ahmedabad"
}
del student



#tasl-7: 
#1:
# use if, if elsif,else create a program:
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
  
#2
#using nested if else create a program:
age = int(input("Enter your age: "))

if age >= 18:
    if age >= 60:
        print("You are a Senior Citizen.")
    else:
        print("You are an Adult.")
else:
    print("You are a Minor.")
    
#3
#use match and create a program:
day = int(input("Enter day number (1-7): "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day number")
    
    #task-8
    #while loop:
    i = 1
while i < 6:
  print(i)
  i += 1
    
    







    
    

