import random

from benchmark_sort import *

# Точность измерений
n = 2

# Отсортированные значения
data_sort = [x for x in range(1000)]
data_reversed_sort = list(reversed(data_sort))

print("Входные данные: Отсортированные значения от 0 до 999")
time_data_sort = all_bench(data_sort, n)
print_fresult(time_data_sort)
print("В относительных единицах:")
print_fresult(ratio_value(time_data_sort))

print("Входные данные: Отсортированные значения от 999 до 0")
time_data_reversed_sort = all_bench(data_reversed_sort, n)
print_fresult(time_data_reversed_sort)
print("В относительных единицах:")
print_fresult(ratio_value(time_data_reversed_sort))

# float массивы с возрастающим и убывающим рандомом
data_rand_up = [random.uniform(0, x) for x in range(1000, 2000)]
data_rand_down = [random.uniform(0, x) for x in range(2000, 1000, -1)]

print("Входные данные: Cлучайные значения с возрастанием от (0 - 1000) до (0 - 1999)")
time_data_rand_up = all_bench(data_rand_up, n)
print_fresult(time_data_rand_up)
print("В относительных единицах:")
print_fresult(ratio_value(time_data_rand_up))

print("Входные данные: Cлучайные значения с убыванием от (0 - 1999) до (0 - 1000)")
time_data_rand_down = all_bench(data_rand_down, n)
print_fresult(time_data_rand_down)
print("В относительных единицах:")
print_fresult(ratio_value(time_data_rand_down))

# Массив со случайными целыми числами
data_randint = [random.randint(0, 1000) for _ in range(1000)]

print("Входные данные: Cлучайные значения от 0 до 1000")
time_data_randint = all_bench(data_randint, n)
print_fresult(time_data_randint)
print("В относительных единицах:")
print_fresult(ratio_value(time_data_randint))
