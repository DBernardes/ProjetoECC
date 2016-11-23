import numpy as np
import matplotlib.pyplot as plt

from porcentPixel import porcentPixel as porcent


#biblioteca para binagem dos dados, fornecidos os vetores x e y, com um passo binsize
def binagem(x,y):
	i=0
	binsize= 50
	lenDados=len(y)
	vetorBinMean = []
	xbin = []
	stdBin = []
	while i < lenDados:
		binmean = np.mean(y[i:i+binsize])
		vetorBinMean.append(binmean)
		xbin.append(np.mean(x[i:i+binsize]))
		stdBin.append(np.std(np.abs(y[i:i+binsize]-binmean)))
		i+=binsize

	plt.plot(xbin,vetorBinMean,linewidth=1.5, c='blue')
	plt.errorbar(xbin, vetorBinMean, stdBin, marker='o', c='blue',linewidth=1.5)

	meanBin = np.mean(vetorBinMean)
	meanStdbin = np.mean(stdBin)
	porcentBin = porcent(vetorBinMean)
	return meanBin, meanStdbin, porcentBin
