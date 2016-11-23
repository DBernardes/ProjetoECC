import numpy as np

#retorna porcentagem de pixels dentro de um intervalo
def porcentPixel(dados):
	mean = np.mean(dados)
	std = np.std(dados)
	contador = 0

	for d in dados:
		if mean - std < d < mean + std:
			contador+=1
	contador = contador/float(len(dados))*100
	return contador


