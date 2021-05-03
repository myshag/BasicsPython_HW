#2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате
#чч:мм:сс. Используйте форматирование строк.

print ("Введите время в секундах: ")
timesec = int(input())

hours = timesec//3600
hours_sec = hours*3600

minutes = (timesec-hours_sec)//60
secs = timesec-(hours_sec+minutes*60)

print(f" Время - {hours:02d}:{minutes:02d}:{secs:02d}")

