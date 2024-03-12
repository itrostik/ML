import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread

url = 'https://img.razrisyika.ru/kart/90/356661-krome-hellou-kitti-33.jpg'


image = imread(url)


def compress_image(img, k):
    height, width, channels = img.shape
    new_height = int(height // k)
    new_width = int(width // k)
    compressed_image = np.zeros((new_height, new_width, channels))

    for i in range(new_height):
        for j in range(new_width):
            compressed_image[i, j] = np.mean(img[i * k:(i + 1) * k, j * k:(j + 1) * k], axis=(0, 1))

    return compressed_image


compressed_image = compress_image(image, 15)
compressed_image1 = compress_image(image, 30)


plt.subplot(1, 3, 1)
plt.imshow(image)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(compressed_image.astype(np.uint8))
plt.title(f'Comp. Img (k={15})')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(compressed_image1.astype(np.uint8))
plt.title(f'Comp. Img (k={30})')
plt.axis('off')

plt.show()

