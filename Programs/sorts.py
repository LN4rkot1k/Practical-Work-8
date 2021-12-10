import random


def bubble_sort(lst):
    for num in range(len(lst) - 1, 0, -1):
        for item in range(num):
            if lst[item] > lst[item + 1]:
                lst[item], lst[item + 1] = lst[item + 1], lst[item]
    return lst


def shell_sort(lst):
    gap = len(lst) // 2
    while gap > 0:
        for val in range(gap, len(lst)):
            curr_val = lst[val]
            pos = val

            while pos >= gap and lst[pos - gap] > curr_val:
                lst[pos] = lst[pos - gap]
                pos -= gap
                lst[pos] = curr_val
        gap //= 2
    return lst


def quick_sort(lst):
    if len(lst) > 1:
        x = lst[random.randint(0, len(lst) - 1)]
        smaller = [i for i in lst if i < x]
        bigger = [i for i in lst if i > x]
        equal = [i for i in lst if i == x]
        lst = quick_sort(smaller) + equal + quick_sort(bigger)
    return lst
