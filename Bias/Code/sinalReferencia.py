#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    Criado em 10 de Outubro de 2016  
    Descricao: este modulo tem como entrada uma serie de dados e o valor maximo do intervalo de pontos desejado, retornando um transformada de fourier baseada em uma distribuicao normal gerada pela media e desvio padrao do vetor fornecido; retorna tambem o intervalo de frequencias dessa serie.
    
    Laboratorio Nacional de Astrofisica, Brazil.    
"""
__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """


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
