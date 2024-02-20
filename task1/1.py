# Создайте одномерный массив размером 100 и заполните его случайными числами от 1 до 100. Найдите все элементы массива, которые больше среднего значения элементов массива и замените их на 0.
import numpy as np

arg = np.random.sample(100) * 100

medium = 0

for i in range(0, 100):
  medium += arg[i]

medium = medium / 100

for i in range(0, 100):
  if arg[i] > medium:
    arg[i] = 0

print(arg)



