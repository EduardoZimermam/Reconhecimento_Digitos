# coding = utf-8

import cv2
import numpy as np

img = cv2.imread("cdf0000_14_4_3.tif", 0)

linhas, colunas = img.shape

_, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

if(linhas < colunas):
	tamHistogramas = linhas
else:
	tamHistogramas = colunas

histHorizontal = [0] * tamHistogramas
histVertical = [0] * tamHistogramas

histAcumulHorizontal = [0] * tamHistogramas
histAcumulVertical = [0] * tamHistogramas

dissimilaridade = 0


for i in range(0, tamHistogramas):
	for j in range(0, tamHistogramas):
		if(thresh[i][j] == 0):
			histVertical[i] += 1

for j in range(0, tamHistogramas):
	for i in range(0, tamHistogramas):
		if(thresh[i][j] == 0):
			histHorizontal[j] += 1

histAcumulVertical[0] = histVertical[0]

for i in range(1, tamHistogramas):
	histAcumulVertical[i] = histAcumulVertical[i - 1] + histVertical[i]

histAcumulHorizontal[0] = histHorizontal[0]

for i in range(1, tamHistogramas):
	histAcumulHorizontal[i] = histAcumulHorizontal[i - 1] + histHorizontal[i]

for i in range(tamHistogramas):
	dissimilaridade += abs(histAcumulVertical[i] - histAcumulHorizontal[i])

print('Dissimilaridade: {}'.format(dissimilaridade))


