import numpy as np
from skimage.io import imread
import matplotlib.pyplot as plt

url = 'https://img.razrisyika.ru/kart/90/356661-krome-hellou-kitti-33.jpg'
image = imread(url)

def pixel(img, min_y, max_y, min_x, max_x, k):
    if max_y < min_y:
        return img

    if max_x < min_x:
        return img

    y_size = (max_y - min_y) // k
    x_size = (max_x - min_x) // k

    pixel_image = img.copy()

    for j in range(min_x, max_y - max_y % x_size, x_size):
        for i in range(min_y, max_y - max_y % y_size, y_size):
            slic = img[i:i + y_size, j:j + x_size, :]

            avg = np.sum(slic, axis=(0, 1)) // (x_size * y_size)
            pixel_image[i:i + y_size, j:j + x_size, :] = avg

    return pixel_image

pix = pixel(image, 600, 1250, 100, 110, 4)

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image)
plt.axis('off')
plt.subplot(1, 2, 2)
plt.title('Result Image')
plt.imshow(pix)
plt.axis('off')
plt.show()

