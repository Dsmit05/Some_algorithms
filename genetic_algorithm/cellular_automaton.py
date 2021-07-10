import collections

import numpy as np


class Game_of_life:
    north_West, north, north_East = (-1, -1), (-1, 0), (-1, 1)
    west, centr, east = (0, -1), (0, 0), (0, 1)
    south_West, south, south_East = (1, -1), (1, 0), (1, 1)

    neighborhood_Moore = north_West, north, north_East, west, east, south_West, south, south_East  # Окрестность Мура
    neighborhood_Neumann = north, west, east, south  # Окрестность фон Неймана

    def __init__(self, matrix, n=8):
        self.matrix = matrix
        self.buffer = np.zeros(self.matrix.shape, dtype=int)
        self.stack = collections.deque(maxlen=2)  # кольцевой буфер для записи поколений
        if n == 8:
            self.neighbours = self.neighborhood_Moore
        if n == 4:
            self.neighbours = self.neighborhood_Neumann

    def count_neighbour(self, index):
        count = 0
        for i in self.neighbours:
            try:
                count = count + self.matrix[
                    index[0] + i[0], index[1] + i[1]]  # тут индексы принимают отрицательные значения(бесшовный мир)
            except:
                continue
        return count

    def life_or_death(self, index):
        # Применяет правила игры к матрице и записывает новое значение в self.buffer
        count = self.count_neighbour(index)

        if self.matrix[index[0], index[1]]:  # Попалась живая клетка
            if count in (2, 3):  # У клетки 2 или 3 соседа
                self.buffer[index[0], index[1]] = 1
            else:
                self.buffer[index[0], index[1]] = 0
        else:
            if count == 3:  # у мертвой клетки 3 соседа - клетка оживает
                self.buffer[index[0], index[1]] = 1
            else:
                self.buffer[index[0], index[1]] = 0

    def __next__(self):
        self.stack.append(self.matrix)

        for i in np.ndenumerate(self.matrix):
            self.life_or_death(i[0])
        # Сравнивает обновленную матрицу с матрицами хранящимися в стаке, если хоть одна True выходит из цикла итератора
        if any(map(lambda x: np.all(self.buffer == x),
                   self.stack)):
            raise StopIteration
        else:
            self.matrix = self.buffer.copy()

        return self.matrix

    def __iter__(self):
        return self
