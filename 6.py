# 6. Необходимо создать (не программно) текстовый файл, 
# где каждая строка описывает учебный предмет и наличие лекционных, 
# практических и лабораторных занятий по этому предмету и их количество. 
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
#  Сформировать словарь, содержащий название предмета и общее количество занятий по нему. 
#  Вывести словарь на экран.

src = open("./text_6.txt",encoding="utf8",mode="r")



p = []
for line in src:
    p=''.join(s if s in '1234567890' else " " for s in line  )
    p = [int(i) for i in p.split()]
    print(line.split(":")[0],sum(p))



