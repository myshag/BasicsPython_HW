# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки
# (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы
# в расчете на одного сотрудника.

proceed = int(input("Выручка фирмы: "))
outlay = int(input("Издержки фирмы: "))
if proceed > outlay:
    profitability = proceed-outlay
    rent = profitability/proceed
    print(f"Хорошая работа. У вас рентабельность {profitability} ")
    worker = int(input("Численность сотрудников фирмы: "))
    print(f"{profitability/worker} прибыль фирмы в расчете на одного сотрудника.")
elif proceed == outlay:
    print("Прибыль и издержки равны")
else:
    print("Убыток — издержки больше выручки")
