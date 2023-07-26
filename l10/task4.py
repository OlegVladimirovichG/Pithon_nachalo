from task3 import Person


class Employee(Person):
    def __init__(self, last_name, first_name, middle_name, age, id_):
        super().__init__(last_name, first_name, middle_name, age)
        self.id_ = id_
        self.access = self._calculate_access()

    def _calculate_access(self):
        return sum(map(int, str(self.id_))) % 7

e1 = Employee('Олег', 'Голубев', 'Владимирович', 34, 123456)
print(e1.access)