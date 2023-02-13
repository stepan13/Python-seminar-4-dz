# | Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств. | 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12 |
# | --- | --- |

n = int(input("Введите размер первого множества: "))
m = int(input("Введите размер второго множества: "))

def inputList(length, name):
    res = []
    for i in range(length):
        number = int(input(f"Множество {name}. Число {i+1} из {length}:" ))
        res.append(number)
    return res

list1 = inputList(n,1)
list2 = inputList(m,2)
set1 = set(list1)
set2 = set(list2)
cross_set = set1.intersection(set2)
cross_list = list(cross_set)
cross_list.sort()

print(list1)
print(list2)
print(cross_list)
