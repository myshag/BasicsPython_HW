# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать
# данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    def __init__(self, name: str, surname: str, position: str, wage: int = 0, bonus: int = 0):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

    def __str__(self):
        return f"Имя:  {self.name} \n"\
               f"Фамилия:  {self.surname} \n" \
               f"Должность:  {self.position} \n"\
               f"Оклад:  {self._income['wage']} \n" \
               f"Премия:  {self._income['bonus']} \n"




class Position(Worker):
    def get_full_name(self):
        return " ".join([self.name, self.surname])

    def get_total_income(self):
        return self._income["wage"]+self._income["bonus"]


worker1 = Position("Михаил", "Иванов", position="Инженер", wage=90000, bonus=8000)
print(worker1)
print("Полное имя",worker1.get_full_name())
print("доход с учетом премии",worker1.get_total_income())












