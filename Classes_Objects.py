#create a class with a property named x.
class MyClass:
    x = 5

#create an object named p1, and print the value of x.
p1 = MyClass()
print(p1.x)

#__init__() Method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

#without the __str__() Method
class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = People("John", 36)

print(p1)

#with the __str__() Method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"
    
p1 = Person("John", 36)

print(p1)

#insert a function that prints a greeting, and execute it on the p1 object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

#The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
#It doesn't have to named self, you can call it what you like, but it has to be the first parameter of any function in the class.

#Use the words mysillyobject and abc instead of self
class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

#Modify object properties
p1.age = 40

#Delete object properties
del p1.age

#Delete objects
del p1

#class definitions can't be empty
#if for some reason you ahve a class with no content,
#put in the pass statement to avoid getting an error
class Person:
    pass