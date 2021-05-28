# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
# строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать
# их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class MyDate():
    date = ""

    def __init__(self,date:str):
        MyDate.date = date

    @classmethod
    def to_int(cls):
        return tuple(int(v) for v in MyDate.date.split("-"))

    @staticmethod
    def validate(date):
        if len(date)!=3:
            raise ValueError(f"Len of param tupple must == 3, len={len(date)}")

        day, mounth, year = date

        if day>=31:
            raise ValueError("Days must <= 31")

        if mounth>= 12:
            raise ValueError("mounth must <= 12")

        if year <0:
            raise ValueError("year must >= 0")

        return  date


date1 = MyDate("19-05-2000")
int_date = date1.to_int()
print(int_date)
print(MyDate.validate(int_date))

date1 = MyDate("32-05-2000")
int_date = date1.to_int()
print(int_date)
print(MyDate.validate(int_date))





