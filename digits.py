# -*- coding: utf-8 -*-

import cv2
import numpy as np

# Método que lê um arquivo e retorna uma lista contendo cada linha do arquivo
def leArquivo(nomeArquivo):
	listalinhas = open(nomeArquivo, 'r').read().splitlines()

	return(listalinhas)

# Método que separa imagens que foram passadas atraves de uma lista por classes definidas.
# Para utilizar, a classe de cada imagem deve estar no final de cada linha. 
def imagesByClass(listaDeImagens, nClass, sizeClass):

	imagesByClass = [[0 for i in range(sizeClass)] for j in range(nClass)]

	for linha in listaDeImagens:
		sizelin = len(linha)
		imagesByClass[int(linha[sizelin - 1])] = linha[:-2]

	return(imagesByClass)

def dissimPorHistograma(imagem):
	img = cv2.imread(imagem, 0)

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
	
	return(dissimilaridade)