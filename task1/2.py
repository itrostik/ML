# Создайте двумерный массив размером 5x5 и заполните его случайными числами от 1 до 100. Используя функцию reshape(), преобразуйте массив в одномерный массив и отсортируйте его по возрастанию.

import numpy as np

arg = []

for i in range(0, 5):
  buffer = np.random.sample(5) * 100
  arg.append(buffer)

result = np.reshape(arg, -1)

result.sort()

print(result)




