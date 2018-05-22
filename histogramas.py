import cv2
import numpy as np

img = cv2.imread("cdf0000_14_4_3.tif", 0)

linhas, colunas = img.shape

_, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

if(linhas > colunas):
	tamHistogramas = linhas
else:
	tamHistogramas = colunas

histColunas = [0] * tamHistogramas
histLinhas = [0] * tamHistogramas



for i in range(0, linhas):
	for j in range(0, colunas):
		if(thresh[i][j] == 255):
			histLinhas[i] += 1

for j in range(0, colunas):
	for i in range(0, linhas):
		if(thresh[i][j] == 255):
			histColunas[j] += 1

for i in range(tamHistogramas):
