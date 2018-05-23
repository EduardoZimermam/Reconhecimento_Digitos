# -*- coding: utf-8 -*-

from digits import *
import sys

# CONSTANTES DA APLICAÇÃO
NCLASSES = 10
TAMCLASSES = 200
TAMBASES = 100


# INICIALIZAÇÃO DAS VÁRIAVEIS
imgsClassificadas = [[0 for i in range(TAMCLASSES)] for j in range(NCLASSES)]
imgsTreinamento = [[0 for i in range(TAMCLASSES)] for j in range(NCLASSES)]
imgsReconhecimento = [[0 for i in range(TAMCLASSES)] for j in range(NCLASSES)]

listaLinhas = leArquivo(sys.argv[1])

imgsClassificadas = imagesByClass(listaLinhas, NCLASSES, TAMCLASSES)

for i in range(1, len(imgsClassificadas)):
	for j in range(1, len(imgsClassificadas[i])):
		if(j < TAMBASES):
			imgsTreinamento.append(imgsClassificadas[i][j])
		else:
			imgsReconhecimento.append(imgsClassificadas[i][j])

print(imgsReconhecimento[2])