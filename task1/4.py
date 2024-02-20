# Создайте двумерный массив размером 10x10 и заполните его случайными числами от 1 до 100. Замените все элементы массива, которые меньше 50, на -1, а все элементы, которые больше или равны 50, на 1. Запишите результат в файл "result.txt".

import numpy as np

arg = []

for i in range(0, 10):
  buffer = np.random.sample(10) * 100
  arg.append(buffer)

for i in range(0, 10):
  for j in range(0, 10):
    if arg[i][j] < 50:
      arg[i][j] = -1
    else:
      arg[i][j] = 1

np.savetxt('result.txt', arg)
