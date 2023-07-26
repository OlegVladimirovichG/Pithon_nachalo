# dz1.py
from task5 import Fish, Bird, Mammal

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, name, age, *args):
        if animal_type == 'Fish':
            return Fish(name, age, *args)
        elif animal_type == 'Bird':
            return Bird(name, age, *args)
        elif animal_type == 'Mammal':
            return Mammal(name, age, *args)
        else:
            raise ValueError('Invalid animal type. Supported types: Fish, Bird, Mammal')


# Example usage of the AnimalFactory
animal_type = 'Fish'
name = 'Nemo'
age = 2
water_type = 'freshwater'

factory = AnimalFactory()
animal_instance = factory.create_animal(animal_type, name, age, water_type)
print(animal_instance.info())  # Output: Fish. Name: Nemo, Age: 2, Water type: freshwater
