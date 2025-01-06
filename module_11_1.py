import numpy as np
from PIL import Image

'''Создание массива чисел'''

arr = np.array([5,10,25,50,18,36,100])
print (arr)

'''Возвращение общего числа элементов массива'''

arr = np.array([5,10,25,50,18,36,100])
print (arr.size)

'''Умножить все элементы массива на 5 и вычесть 5'''

arr = arr * 5 - 5
print (arr)

'''Изменение размера на 400 x 550 пикселей'''

image = Image.open(r'D:\Диана\PythonProjects\Модуль №11\izo.jpg')
resized_image = image.resize((400, 550))  # (был 540 x 642 пикс.)
resized_image.show()
resized_image.save('resized_image.jpg')

'''Переворот на 180 градусов'''

transposed_image = image.transpose(Image.FLIP_TOP_BOTTOM)
transposed_image.show()
transposed_image.save('transposed_image.jpg')

'''Сохранение в другой формат'''

image.save('converted_image.bmp')  # формат BMP
image.save('converted_image.gif')  # формат GIF








