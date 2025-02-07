class Monkeys:
    def __init__(self, name,age):
        self.name = name
        self.age = age


    def eat (self):
        print("eat Berries")

    def sleep(self):
        print("im sleeping")



def main():
     monkey = Monkeys("baboon",45)
     monkey.eat()
     monkey.sleep()


if __name__ == '__main__':
    main()