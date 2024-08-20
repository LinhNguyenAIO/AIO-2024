# XỬ LÝ ẢNH TRONG NUMPY

import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

# 12: Hoàn thành đoạn code sau đây để chuyển ảnh màu sang ảnh xám dựa vào phương pháp Lightness:


def color2gray(rgb):
    return (np.max(rgb)*0.5 + np.min(rgb)*0.5)


img = mpimg.imread(
    'C:\AIO2024\GitHub\AIO-2024\Module02\Week01\data\dog.jpeg')

gray_img_01 = np.apply_along_axis(color2gray, 2, img)
print(gray_img_01[0, 0])

# Câu hỏi 13: Hoàn thành đoạn code sau đây để chuyển ảnh màu sang ảnh xám dựa vào phương pháp Average:


def color2gray2(rgb):
    return np.sum(rgb)/3


gray_img_02 = np.apply_along_axis(color2gray2, 2, img)
print(gray_img_02[0, 0])

# Câu hỏi 14: Hoàn thành đoạn code sau đây để chuyển ảnh màu sang ảnh xám dựa vào phương pháp Luminosity:

gray_img_03 = 0.21*img[:, :, 0] + 0.72*img[:, :, 1] + 0.07*img[:, :, 2]
print(gray_img_03[0, 0])

plt.imshow(gray_img_01, cmap='gray')
plt.show()
