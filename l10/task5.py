class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return f'Name: {self.name}, Age: {self.age}'


class Fish(Animal):
    def __init__(self, name, age, water_type):
        super().__init__(name, age)
        self.water_type = water_type

    def info(self):
        return f'Fish. {super().info()}, Water type: {self.water_type}'


class Bird(Animal):
    def __init__(self, name, age, beak_type):
        super().__init__(name, age)
        self.beak_type = beak_type

    def info(self):
        return f'Bird. {super().info()}, Beak type: {self.beak_type}'


class Mammal(Animal):
    def __init__(self, name, age, milk_type):
        super().__init__(name, age)
        self.milk_type = milk_type

    def info(self):
        return f'Mammal. {super().info()}, Milk type: {self.milk_type}'


# Example usage
fish = Fish('Nemo', 2, 'freshwater')
bird = Bird('Kea', 5, 'hooked')
mammal = Mammal('Rex', 3, 'full-cream milk')

print(fish.info())
print(bird.info())
print(mammal.info())
