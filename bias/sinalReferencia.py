import numpy as np
from scipy.fftpack import fft, fftfreq

#gera um sinal de referencia para FFT em torno da media +/- 2 desvios
def sinalReferencia(vetor,interv):		
	np.random.seed(1)
	sinal =	np.random.normal(np.mean(vetor),np.std(vetor), len(vetor))
	sinalf = np.abs(fft(sinal))
	sinalf = sinalf[1:interv]
	xs = fftfreq(sinalf.size)
	return sinalf, xs
