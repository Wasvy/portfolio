class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.wheels = 4

    def printCar(self):
        print(f"I am a {self.brand} {self.model}")


def main():
    sport = Car("Audi","R8")
    sport.printCar()
    NSX = Car("Acura", "NSX")
    NSX.printCar()


if __name__ == '__main__':
    main()
