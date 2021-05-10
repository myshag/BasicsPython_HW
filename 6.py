# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
#     Необходимо предусмотреть условие его завершения.

from itertools import count
from itertools import takewhile
from itertools import cycle

start = 3
end = 11

for i in takewhile(lambda i: i < end, count(start)):
    print(i)

max = 10
N = 0
for i in cycle(["python", "java", "perl", "javascript"]):
    N += 1
    print(i)
    if N > max:
        break
