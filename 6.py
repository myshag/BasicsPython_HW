# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
# и возвращающую его же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().



def int_func(word: str):
    if word.islower():

        success=True
        for ch in word:
            if not ('a'<=ch<='z'):
                success=False
                break
        if success:
            return word.capitalize()

src = input("Исходная строка: ")
out = [int_func(s) for s in src.split() if s.isascii()]
#print(out)
print(" ".join(out))

