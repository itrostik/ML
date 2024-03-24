import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread


url = 'https://www.osp.ru/FileStorage/DOCUMENTS_ILLUSTRATIONS/13234504/original.jpg'
orig_img = imread(url)

# определяем размеры квадрата
img_height, img_width, _ = orig_img.shape
square_size = min(img_height, img_width) // 10

# создаем квадрат
white_square = np.ones((square_size, square_size, 3), dtype=np.uint8) * 255

# определяем координаты квадрата
top = (img_height - square_size) // 2
left = (img_width - square_size) // 2
bottom = top + square_size
right = left + square_size

# вставка квадрата в центр картинки
processed_img = np.copy(orig_img)
processed_img[top:bottom, left:right] = white_square

plt.imshow(processed_img)
plt.show()
