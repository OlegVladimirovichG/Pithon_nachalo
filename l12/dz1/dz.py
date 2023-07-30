import csv
import re

class NameDescriptor:
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if not re.match(r'^[A-Z][a-z]+$', value):
            raise ValueError(f"Неверный формат для {self.name}. Должно начинаться с заглавной буквы и содержать только буквы.")
        instance.__dict__[self.name] = value

class GradeDescriptor:
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if not (2 <= value <= 5):
            raise ValueError(f"Недопустимое значение для {self.name}. Оценка должна быть от 2 до 5.")
        instance.__dict__[self.name] = value

class TestResultDescriptor:
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError(f"Недопустимое значение для {self.name}. Результат теста должен быть от 0 до 100.")
        instance.__dict__[self.name] = value

class Student:
    def __init__(self, subjects_file): 
        self.name = NameDescriptor()
        self.subjects = self.load_subjects_from_csv(subjects_file)
        self.scores = {subject: {"grades": [], "test_results": []} for subject in self.subjects}

    @staticmethod
    def load_subjects_from_csv(file_path):
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            return [subject for row in reader for subject in row]


    def add_grade(self, subject, grade):
        if subject not in self.subjects:
            raise ValueError(f"Недопустимый предмет '{subject}'. Доступные предметы: {', '.join(self.subjects)}")
        self.scores[subject]["grades"].append(grade)

    def add_test_result(self, subject, result):
        if subject not in self.subjects:
            raise ValueError(f"Недопустимый предмет '{subject}'. Доступные предметы: {', '.join(self.subjects)}")
        self.scores[subject]["test_results"].append(result)

    def get_subject_average_grade(self, subject):
        if subject not in self.subjects:
            raise ValueError(f"Недопустимый предмет '{subject}'. Доступные предметы: {', '.join(self.subjects)}")
        grades = self.scores[subject]["grades"]
        return sum(grades) / len(grades) if grades else 0

    def get_overall_average_grade(self):
        total_grades = []
        for subject in self.subjects:
            total_grades.extend(self.scores[subject]["grades"])
        return sum(total_grades) / len(total_grades) if total_grades else 0


if __name__ == "__main__":
    subjects_file_path = "subjects.csv"  

    student = Student(subjects_file_path)
    student.name = "Иван Иванов"

    student.add_grade("Математика", 4)
    student.add_grade("Математика", 5)
    student.add_test_result("Математика", 90)
    student.add_test_result("Математика", 80)

    student.add_grade("История", 3)
    student.add_grade("История", 4)
    student.add_test_result("История", 70)
    student.add_test_result("История", 85)

    print(f"Средний балл {student.name} по Математике: {student.get_subject_average_grade('Математика')}")
    print(f"Средний балл {student.name} по Истории: {student.get_subject_average_grade('История')}")
    print(f"Общий средний балл {student.name}: {student.get_overall_average_grade()}")