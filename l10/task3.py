class Person:
    def __init__(self, last_name, first_name, middle_name, age):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.age = age
        
    def check_birthday(self):
        return self.age
    
    def change_birthday(self):
        self.age += 1
    
    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'


a = Person('Олег', 'Голубев', 'Владимирович', 34)
print(a.full_name)
print(a.check_birthday)
print(a.change_birthday)