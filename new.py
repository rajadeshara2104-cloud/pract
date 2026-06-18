a = 33
b = 200
if b>a:
  print("b is greater than a")
  
a = 33
b = 200
if b > a:
    print("b is greater than a") 


a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
  
  thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
  
  
  student = {
    "name": "Raj",
    "age": 18,
    "city": "Ahmedabad"
}

print(student)



student = {
    "name": "Raj",
    "age": 18,
    "city": "Ahmedabad"
}

student.clear()

print(student)


student = {
    "name": "Raj",
    "age": 18,
    "city": "Ahmedabad"
}

new_student = student.copy()

print(new_student)


student = {
    "name": "Raj",
    "age": 18,
    "city": "Ahmedabad"
}

print(student.get("name"))




student = {
    "name": "Raj",
    "age": 18,
    "city": "Ahmedabad"
}

print(student.items())






student = {
    "name": "Raj",
    "age": 18,
    "city": "Ahmedabad"
}

print(student.keys())




student = {
    "name": "Raj",
    "age": 18,
    "city": "Ahmedabad"
}

value = student.pop("age")

print(value)
print(student)


student = {
    "name": "Raj",
    "age": 18,
    "city": "Ahmedabad"
}

x = student.popitem()

print(x)
print(student)



student = {
    "name": "Raj",
    "age": 18
}

student.update({"age": 19})

print(student)


student = {
    "name": "Raj",
    "age": 18,
    "city": "Ahmedabad"
}

print(student.values())






a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
  
  
  
  age = int(input("Enter your age: "))

if age >= 18:
    if age >= 60:
        print("You are a Senior Citizen.")
    else:
        print("You are an Adult.")
else:
    print("You are a Minor.")
    
    
    

day = 4
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
