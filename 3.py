# Создать текстовый файл (не программно). 
# Построчно записать фамилии сотрудников и величину их окладов 
# (не менее 10 строк). 
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, 
# вывести фамилии этих сотрудников. 
# Выполнить подсчёт средней величины дохода сотрудников.

with open("./sotrudniki.txt",encoding="utf8",mode="r") as fin:
    spisok = [line.split() for line in fin]
    spisok = {person:int(plata) for person, plata in spisok}
    print("Cотрудники еоторые имеют оклад менее 20 тысяч")
   
    for name, plata in spisok.items():
        if int(plata)<20000:
            print(name)
    
    average = sum(spisok.values())/len(spisok.values())
    print(f"Средней доход сотрудников равен: {average:.2f} руб.")
    


    

    


    

