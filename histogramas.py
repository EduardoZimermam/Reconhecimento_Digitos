import cv2
import numpy as np

img = cv2.imread("cdf0000_14_4_3.tif", 0)

linhas, colunas = img.shape

_, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

histLinhas = [0] * linhas 
histColunas = [0] * colunas

for i in range(0, linhas):
	for j in range(0, colunas):
		if(thresh[i][j] == 255):
			histLinhas[i] += 1

for j in range(0, colunas):
	for i in range(0, linhas):
		if(thresh[i][j] == 255):
			histColunas[j] += 1


print(histLinhas)
print(histColunas)