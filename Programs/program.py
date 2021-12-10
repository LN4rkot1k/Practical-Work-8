from prettytable import PrettyTable
from datetime import datetime
import sorts
import random as rd

N = 30000  # Длина последовательности
sortedList = [x for x in range(10, 10 + N)]
randList = [x * 0 + rd.randint(10, 10 + N) for x in range(N)]
reversedList = sortedList[:]
reversedList.reverse()

sortedListDefault = sortedList.copy()  # Создание копий изначальных массивов
randListDefault = randList.copy()
reversedListDefault = reversedList.copy()


def check(arr):  # Функция, которая проверяет, отсортирован ли массив
    sort_arr = arr.copy()
    sort_arr.sort()
    return sort_arr == arr


myTable = PrettyTable()
myTable.field_names = ["Метод сортировки", "Отсортированная", "Случайная", "Отсортированная в обратном порядке"]

Time_1 = datetime.now()
lists = sorts.bubble_sort(sortedList)
Time_1 = datetime.now() - Time_1
if not check(lists):
    Time_1 = "Error"

Time_2 = datetime.now()
lists = sorts.bubble_sort(randList)
Time_2 = datetime.now() - Time_2
if not check(lists):
    Time_2 = "Error"

Time_3 = datetime.now()
lists = sorts.bubble_sort(reversedList)
Time_3 = datetime.now() - Time_3
if not check(lists):
    Time_3 = "Error"

myTable.add_row(["Сортировка пузырьком", Time_1.total_seconds(), Time_2.total_seconds(), Time_3.total_seconds()])

sortedList = sortedListDefault.copy()
randList = randListDefault.copy()
reversedList = reversedListDefault.copy()

Time_1 = datetime.now()
lists = sorts.shell_sort(sortedList)
Time_1 = datetime.now() - Time_1
if not check(lists):
    Time_1 = "Error"

Time_2 = datetime.now()
lists = sorts.shell_sort(randList)
Time_2 = datetime.now() - Time_2
if not check(lists):
    Time_2 = "Error"

Time_3 = datetime.now()
lists = sorts.shell_sort(reversedList)
Time_3 = datetime.now() - Time_3
if not check(lists):
    Time_3 = "Error"

myTable.add_row(
    ["Сортировка методом Шелла", Time_1.total_seconds(), Time_2.total_seconds(), Time_3.total_seconds()])

sortedList = sortedListDefault.copy()
randList = randListDefault.copy()
reversedList = reversedListDefault.copy()

Time_1 = datetime.now()
lists = sorts.quick_sort(sortedList)
Time_1 = datetime.now() - Time_1
if not check(lists):
    Time_1 = "Error"

Time_2 = datetime.now()
lists = sorts.quick_sort(randList)
Time_2 = datetime.now() - Time_2
if not check(lists):
    Time_2 = "Error"

Time_3 = datetime.now()
lists = sorts.quick_sort(reversedList)
Time_3 = datetime.now() - Time_3
if not check(lists):
    Time_3 = "Error"

myTable.add_row(
    ["Быстрая сортировка", Time_1.total_seconds(), Time_2.total_seconds(), Time_3.total_seconds()])

sortedList = sortedListDefault.copy()
randList = randListDefault.copy()
reversedList = reversedListDefault.copy()

Time_1 = datetime.now()
sortedList.sort()
Time_1 = datetime.now() - Time_1
lists = sortedList[:]
if not check(lists):
    Time_1 = "Error"

Time_2 = datetime.now()
randList.sort()
Time_2 = datetime.now() - Time_2
lists = randList[:]
if not check(lists):
    Time_2 = "Error"

Time_3 = datetime.now()
reversedList.sort()
Time_3 = datetime.now() - Time_3
lists = reversedList[:]
if not check(lists):
    Time_3 = "Error"

myTable.add_row(
    ["Встроенная сортировка", Time_1.total_seconds(), Time_2.total_seconds(), Time_3.total_seconds()])

file = open("output.txt", "w")
file.write(f"Количество элементов: {N}\n")
file.write(f'Случайная последовательность, сгенерированная программно: {randListDefault}\n')
file.write(str(myTable))