import time

import numpy as np
import pandas as pd
import plotly.express as px
from cellular_automaton import Game_of_life


def show_game_life(arr=np.random.randint(0, 2, size=(50, 50)), max_life_len=350):
    x = []  # Положение клетки по оси x
    y = []  # Положение клетки по оси y
    z = []  # Размер клетки
    year = []  # Количество поколений

    my_game = iter(Game_of_life(arr, 8))

    count_generations = 0  # Счетчик поколений

    for count in my_game:

        for i in np.ndenumerate(count):
            x.append(i[0][0])
            y.append(i[0][1])
            z.append(i[1])
            year.append(count_generations)

        count_generations += 1

        if count_generations > max_life_len:
            break

    data = {'x': x, 'y': y, 'z': z, 'year': year}
    frame = pd.DataFrame(data)

    fig = px.scatter(frame, x="x", y="y", size="z", animation_frame="year", template="plotly_dark")
    fig.show()


# show_game_life()

def show_game_life_consul(arr=np.random.randint(0, 2, size=(15, 15))):
    my_game = iter(Game_of_life(arr, 8))
    count_generations = 0  # Счетчик поколений

    for i in my_game:
        s = np.where(my_game.matrix == 1, "X", i)
        s = np.where(s == "0", " ", s)
        time.sleep(0.3)
        count_generations += 1
        print(s, "\n\n")

    print("колония прожила:", count_generations)


show_game_life_consul()
