# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(arg0, arg1, arg2):
    args = [arg0, arg1, arg2]
    min_arg = min(args)
    args.pop(args.index(min_arg))
    return sum(args)

print(my_func(100,9,8))



