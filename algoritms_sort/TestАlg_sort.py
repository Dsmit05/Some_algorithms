import unittest

import Аlg_sort as Alg


class TestSort(unittest.TestCase):
    arr = []
    arr_sort = [-31, -2, 2.5, 6, 7, 11, 19, 27, 45, 121, 158]

    start, end = 100 ** 3, -150 ** 3

    arr_big = [x for x in range(start, end, -10 ** 3)]
    arr_big_sort = list(reversed(arr_big))

    def setUp(self):
        self.arr = [19, -2, -31, 45, 6, 11, 121, 27, 158, 2.5, 7]

    def test_buble_sort(self):
        arr1 = Alg.buble_sort(self.arr)
        self.assertEqual(arr1, self.arr_sort)

        arr2 = Alg.buble_sort([])
        self.assertEqual(arr2, [])

        arr3 = Alg.buble_sort(self.arr_big[:])
        self.assertEqual(arr3, self.arr_big_sort)

    def test_insertion_sort(self):
        arr1 = Alg.insertion_sort(self.arr)
        self.assertEqual(arr1, self.arr_sort)

        arr2 = Alg.insertion_sort([])
        self.assertEqual(arr2, [])

        arr3 = Alg.insertion_sort(self.arr_big[:])
        self.assertEqual(arr3, self.arr_big_sort)

    def test_selection_sort(self):
        arr1 = Alg.selection_sort(self.arr)
        self.assertEqual(arr1, self.arr_sort)

        arr2 = Alg.selection_sort([])
        self.assertEqual(arr2, [])

        arr3 = Alg.selection_sort(self.arr_big[:])
        self.assertEqual(arr3, self.arr_big_sort)

    def test_shell_sort(self):
        arr1 = Alg.shell_sort(self.arr)
        self.assertEqual(arr1, self.arr_sort)

        arr2 = Alg.shell_sort([])
        self.assertEqual(arr2, [])

        arr3 = Alg.shell_sort(self.arr_big[:])
        self.assertEqual(arr3, self.arr_big_sort)

    def test_merge_sort(self):
        arr1 = Alg.merge_sort(self.arr)
        self.assertEqual(arr1, self.arr_sort)

        arr2 = Alg.merge_sort([])
        self.assertEqual(arr2, [])

        arr3 = Alg.merge_sort(self.arr_big[:])
        self.assertEqual(arr3, self.arr_big_sort)

    def test_quick_sort(self):
        arr1 = Alg.quick_sort(self.arr)
        self.assertEqual(arr1, self.arr_sort)

        arr2 = Alg.quick_sort([])
        self.assertEqual(arr2, [])

        arr3 = Alg.quick_sort(self.arr_big[:])
        self.assertEqual(arr3, self.arr_big_sort)

    def test_heap_sort(self):
        arr1 = Alg.heap_sort(self.arr)
        self.assertEqual(arr1, self.arr_sort)

        arr2 = Alg.heap_sort([])
        self.assertEqual(arr2, [])

        arr3 = Alg.heap_sort(self.arr_big[:])
        self.assertEqual(arr3, self.arr_big_sort)

    def test_tim_sort(self):
        arr1 = Alg.tim_sort(self.arr)
        self.assertEqual(arr1, self.arr_sort)

        arr2 = Alg.tim_sort([])
        self.assertEqual(arr2, [])

        arr3 = Alg.tim_sort(self.arr_big[:])
        self.assertEqual(arr3, self.arr_big_sort)


unittest.main()
