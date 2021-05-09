# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры
# как именованные аргументы. Реализовать вывод данных о пользователе
# одной строкой.

def printuser(fistname: str, lastname: str, yearofbirth: str,
              city: str, email: str, phone: str):
    """
    Вывод данных о пользователе одной строкой.



    :param fistname: Имя пользователя
    :param lastname: Фамилия пользователя
    :param yearofbirth: Год рождения пользователя
    :param city: Город проживания пользователя
    :param email: email пользователя
    :param phone: Номер телефона пользователя
    :return: None
    """
    print(f"{fistname} {lastname}, год рожд. {yearofbirth}, "
          f"город: {city}, email: {email}, phone: {phone}")


printuser(fistname="Максим", lastname="Абрамов", yearofbirth="1990",
          city="Москва", email="abramov@mail.ru", phone="+79003451233")

