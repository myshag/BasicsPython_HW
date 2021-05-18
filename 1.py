# 1. Создать программно файл в текстовом формате, 
# записать в него построчно данные, вводимые пользователем.
#  Об окончании ввода данных свидетельствует пустая строка.

# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, 
# выполнить подсчет количества строк, количества слов в каждой строке.

try:
    with open("out.txt","w",encoding="utf8") as outfile:
        while True:
            inp = input("Строка: ")
            if inp=="":
                break
            print(inp,file=outfile)

except IOError as ioerror:
    print(ioerror)

try:
    with open("out.txt","r",encoding="utf8") as infile:
        for i,s in enumerate(infile):
            print(f"Строка {i+1} Количество слов {len(s.split())}")

except IOError as ioerror:
    print(ioerror)















