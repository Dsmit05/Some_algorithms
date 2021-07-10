import random


def buble_sort(arr):
    # Пузырьковая сортировка
    # от O(n^2) до O(n)

    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def insertion_sort(arr):
    # Сортировка вставками
    # от O(n^2) до O(n)

    for i in range(1, len(arr)):
        j = i - 1
        next_element = arr[i]

        while (arr[j] > next_element) and (j >= 0):
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = next_element
    return arr


def selection_sort(arr):
    # Сортировка выбором
    # от O(n^2)

    for i in range(len(arr)):
        min_i = i
        for j in range(i + 1, len(arr)):
            if arr[min_i] > arr[j]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]
    return arr


def shell_sort(arr):
    # Сортировка Шелла: малая деградация, мало потребляет памяти
    # от O(n^2) до O(n log^2 n)

    distance = len(arr) // 2
    while distance > 0:
        for i in range(distance, len(arr)):
            temp = arr[i]
            j = i
            while j >= distance and arr[j - distance] > temp:
                arr[j] = arr[j - distance]
                j = j - distance
            arr[j] = temp

        distance = distance // 2
    return arr


def merge_sort(arr):
    # Сортировка слиянием
    # В среднем O(n log n)

    def _merge(left, right, merged):

        left_cursor, right_cursor = 0, 0
        while left_cursor < len(left) and right_cursor < len(right):
            if left[left_cursor] <= right[right_cursor]:
                merged[left_cursor + right_cursor] = left[left_cursor]
                left_cursor += 1
            else:
                merged[left_cursor + right_cursor] = right[right_cursor]
                right_cursor += 1

        for left_cursor in range(left_cursor, len(left)):
            merged[left_cursor + right_cursor] = left[left_cursor]
        for right_cursor in range(right_cursor, len(right)):
            merged[left_cursor + right_cursor] = right[right_cursor]
        return merged

    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    return _merge(left, right, arr)


def quick_sort(arr):
    # Быстрая сортировка
    # O(n log n)
    if len(arr) <= 1:
        return arr
    else:
        mid = random.choice(arr)
        left = [elem for elem in arr if elem < mid]
        M = [mid] * arr.count(mid)
        right = [elem for elem in arr if elem > mid]
        return quick_sort(left) + M + quick_sort(right)


def heap_sort(arr):
    #
    def _heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[i] < arr[left]:
            largest = left

        if right < n and arr[largest] < arr[right]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            _heapify(arr, n, largest)

    n = len(arr)
    for i in range(n, -1, -1):
        _heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        _heapify(arr, i, 0)
    return arr


def tim_sort(arr):
    # Сортировка Тима
    arr.sort()
    return arr
