class Archive:
    """Реализация паттерна Singleton"""

    _instance = None

    def __new__(cls, *args):
        """
        Проверка на наличие экземпляра

        :param num: Номер ячейки
        :param value: Содержимое ячейки
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive = []
        else:
            cls._instance.archive.append((cls._instance.num, cls._instance.value))
        return cls._instance

    def __init__(self, num, value):
        self.num = num
        self.value = value

    def __str__(self):
        return f'{self.num}, {self.value}, {self.archive}'

    def __repr__(self):
        return 'Archive({}, {})'.format(self.num, (self.value, "'" + self.value + "'")[isinstance(self.value, str)])