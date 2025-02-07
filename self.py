class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def eat(self):
        print("im eating")

class Student(Person):
    def __init__(self, name,age):
        super().__init__(name,age)

    def gotoschool(self):
        print("Im going to school")

def main():
    robert = Student("Robert", 18)
    robert.gotoschool()
    robert.eat()

if __name__ == '__main__':
    main()