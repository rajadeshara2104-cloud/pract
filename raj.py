
print("HEllo word")

name="raj"
age=18
price=20

print(age)

print("my name is:",name)
print("my age is:",age)
print("price is:",price)

print(type(name))
print(type(age))
print(type(price))

#using a whilew loop
i = 1
while i < 11:
  print(i)
  i += 1
  
#using a for loop:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
  
  i = 1

while i <= 6:
    print("*" * i)
    i += 1
    

#function
def my_function():
  print("hi my name is raj")
  
  
  def print_numbers():
    i = 1
    while i <= 10:
        print(i)
        i += 1

print ()


def print_numbers():
    i = 1
    while i <= 10:
        print(i)
        i += 1

print_numbers()

def my_function():
  print("hello")
  return"function execute succefully"
x=my_function()
print(x)

#fun in for:
for i in range(10):
  my_function()

def sum():
    a=20
    b=30
    c=a+b
    return c
res=sum()
print(res)q


def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       
boat1 = Boat("Ibiza", "Touring 20") 
plane1 = Plane("Boeing", "747")     

for x in (car1, boat1, plane1):
  x.move()





  
  
    







