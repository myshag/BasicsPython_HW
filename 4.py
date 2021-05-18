# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и 
# считывающую построчно данные. 
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

input_list = []
mydict={'One':"Один","Two":"Два","Three":"Три","Four":"Четыре"}

with open("text_4.txt","r",encoding="utf8") as src_file:
    for line in src_file:
        s= [w.rstrip() for w in line.split('-')]
        input_list.append(s)

print(input_list)

with open("text_4_translate.txt","w",encoding="utf8") as out_file:
    for line in input_list:
        print(mydict[line[0]],line[1],sep=" - ",file=out_file)


