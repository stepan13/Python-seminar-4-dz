# | Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число 
# ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной 
# во входном файле грядки. 
# | 4 -> 1 2 3 4
# 9 |

from random import randint
N = randint(3,100)
N = 10
gryadka = [randint(0, 100) for i in range(N)]

max = 0
res = {}
print(gryadka)
for _ in gryadka:
    current_sum = gryadka[0] + gryadka[1] + gryadka[2]

    if current_sum > max:
        max = current_sum
        res = [gryadka[0], gryadka[1], gryadka[2]]
    elem = gryadka.pop(0)
    gryadka.append(elem)
print(res)
print(max)