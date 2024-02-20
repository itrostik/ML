# Создайте двумерный массив размером 6x6 и заполните его случайными числами от 1 до 100. Найдите все элементы массива, которые больше 50 и меньше 75, и замените их на 0.

import numpy as np

arg = []

for i in range(0, 6):
  buffer = np.random.sample(6) * 100
  arg.append(buffer)

for i in range(0, 6):
  for j in range(0, 6):
    if arg[i][j] > 50 and arg[i][j] < 75:
      arg[i][j] = 0

print(arg)