class Student:
    def __init__(self,name="maddy", age=29):
        self.name = name
        self.age = age
        print("Adding student in database")

    @staticmethod
    def greet():
        print("Hello All")

s1 = Student()
print(f"My name is {s1.name} and my age is {s1.age}")

s2 = Student("Arshad",30)
print("This is my friend", s2.name, "and this age is something ",s2.age)

s2.greet()
