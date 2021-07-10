import time

from Аlg_sort import *


def bench(*funcs, arr, count_iter=10):
    # Замеряет скорость работы функции(функций) для заданного списка

    dict_bench = {}
    for func in funcs:
        time_sum = 0
        for i in range(count_iter):
            arr_copy = arr[:]

            start = time.time()

            s = func(arr_copy)

            time_work = time.time() - start
            time_sum = time_sum + time_work
        dict_bench[func.__name__] = time_sum / count_iter
    return dict_bench


def all_bench(arr, count_iter=10):
    # Возвращает словарь с временем работы для всех функций

    return bench(buble_sort, insertion_sort, selection_sort, shell_sort, merge_sort, quick_sort, heap_sort, tim_sort,
                 arr=arr, count_iter=count_iter)


def ratio_value(dict_input):
    # Находим отношение всех времен сортировок

    for i in sorted(dict_input.values()):
        if i > 0:
            min_value = i
            break
        else:
            min_value = 1

    for key in dict_input:
        dict_input[key] = dict_input[key] / min_value
    return dict_input


def print_fresult(dict_input):
    # Форматированный вывод cловаря
    sorted_arr = sorted(dict_input.items(), key=lambda x: x[1])
    print("| Алгоритм          | Время сортировки  |")
    print("|___________________|___________________|")
    for k, v in sorted_arr:
        print(f"| {k:17s} | {v:17f} |")
    print("|___________________|___________________|\n")
