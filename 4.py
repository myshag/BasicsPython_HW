# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

# n = int(input("Введите число: "))
n = 1567
numbers = []
while n > 0:
    numbers.append(n % 10)
    n //= 10
print(max(numbers))
