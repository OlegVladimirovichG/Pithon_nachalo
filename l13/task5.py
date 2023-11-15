import json
from task3_4 import User

class AccessError(Exception):
    pass

class LevelError(Exception):
    pass

class Project:
    """Класс проекта.
    :parameter admin: Администратор проекта
    """
    def __init__(self, admin, users=None):
        self.admin = admin
        self.users = users if users is not None else []

    @classmethod
    def load_from_json(cls, json_file):
        with open(json_file, 'r') as file:
            data = json.load(file)
            admin_data = data.get("admin")
            admin = User(**admin_data)
            users_data = data.get("users", [])
            users = [User(**user_data) for user_data in users_data]
            return cls(admin, users)

    def login(self, name, id_):
        new_user = User(name, id_)
        if new_user not in self.users:
            raise AccessError("Доступ запрещен. Пользователь не является членом проекта.")
        else:
            existing_user = self.users[self.users.index(new_user)]
            existing_user.level = new_user.level
            self.admin = existing_user

    def add_user(self, user):
        if user.level is None:
            raise ValueError("Уровень доступа пользователя должен быть указан.")

        if self.admin.level is None:
            self.admin.level = user.level
        elif not isinstance(self.admin.level, int) or not isinstance(user.level, int):
            raise ValueError("Уровни доступа пользователей должны быть целочисленными значениями.")
        elif user.level < self.admin.level:
            raise ValueError("Уровень доступа пользователя ниже, чем уровень администратора.")

        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    def save_to_json(self, json_file):
        data = {
            "admin": self.admin.__dict__,
            "users": [user.__dict__ for user in self.users]
        }
        with open(json_file, 'w') as file:
            json.dump(data, file)

if __name__ == "__main__":
    project = Project(User("Admin", 1, 7), [User("User1", 2, 4), User("User2", 3, 3)])
    
    try:
        project.login("User1", 2)
        print(f"Пользователь {project.admin.name} с уровнем доступа {project.admin.level} вошел в систему.")
    except AccessError as e:
        print(e)

    new_user = User("NewUser", 4, 2)
    try:
        project.add_user(new_user)
        print(f"Пользователь {new_user.name} с уровнем доступа {new_user.level} добавлен в проект.")
    except LevelError as e:
        print(e)

    project.remove_user(User("User1", 2, 4))
    project.save_to_json("project_data.json")
