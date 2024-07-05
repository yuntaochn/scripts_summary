'''
Author: maying maying@efort.com.cn
Date: 2022-07-14 08:30:28
LastEditors: maying maying@efort.com.cn
LastEditTime: 2022-08-01 17:02:40
FilePath: /GetImage-python/get_src_image.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import csv
import cv2 as cv
import numpy as np

img = np.zeros((1500, 1500, 3), np.uint8)

r_list = []
x_list = []
z_list = []
with open('scan_res12.csv', encoding='utf-8-sig') as f:
    for row in csv.reader(f, skipinitialspace=True):
        # print(row)
        r_list.append(int(row[0]))  # 表示行数
        # point_num = int(row[1])  # 表示行上的点
        # print(row[2])
        if row[2].startswith('-'):
            x_list.append(250 - int(np.round(float(row[2][1:]))))
        else:
            x_list.append(int(np.round(float(row[2])) + 250))

        z = float(row[3])
        z_list.append(int(np.round(z)))

z_max = max(z_list)
z_min = min(z_list)
print(z_max, z_min)

l = len(z_list)
for i in range(l):
    y = r_list[i]
    x = x_list[i]
    h_gray = (z_list[i] - z_min) / (z_max - z_min)
    h_gray = 255 - h_gray * 255
    img[y, x] = h_gray

# cv.imwrite('file/5.bmp', img)


cv.namedWindow('src', cv.WINDOW_NORMAL)
cv.imshow('src', img)
cv.waitKey()
cv.destroyAllWindows()

