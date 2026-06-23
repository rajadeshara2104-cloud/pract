class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Student Name:", self.name)


class Teacher:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Teacher Name:", self.name)


class Employee:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Employee Name:", self.name)


# 2 Objects of Student Class
s1 = Student("Raj")
s2 = Student("Prem")

# 2 Objects of Teacher Class
t1 = Teacher("Ravi")
t2 = Teacher("Neha")

# 2 Objects of Employee Class
e1 = Employee("Karan")
e2 = Employee("Priya")

# Display Data
s1.display()
s2.display()

t1.display()
t2.display()

e1.display()
e2.display()