#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    Criado em 17 de Agosto de 2016.
    
    Descricao: esta biblioteca possui as seguintes funcoes:

		geraDados: esta funcao gera um histograma dos dados fornecida uma imagem em formato numpy (imagem esta resultante da combinacao de uma amostra de imagens da serie de dados). Sobre esses dados e calculado a media, mediana, desvio padrao e desvio padrao absoluto. Alem disso, e gerado um segundo histograma normalizado em relacao a media e desvio padrao obtidos para servir de comparacao. Um intervalo de 7 sigmas e estipulado ao redor da mediana para o calculo do histograma e de suas informacoes.

		plothist: esta funcao e responsavel pelo plot do histograma dos dados e do shitograma normalizado; sobre ele sao expressao informacoes como valor medio e intervalo de valores dentro da media +/- sigma. Essas dados sao obtidos atraves de uma interpolacao cubica, retornando-os a um vetor para posterior exibicao.

		returnIndex: esta funcao retorna o indice de um vetor para qual seu valor seja igual a de um parametro fornecido.

		drawLine: esta funcao desenha uma linha vertical sobre o grafico, identificando seu valor do par coordenado.

		histograma: esta funcao faz a chamada de todas as outras funcoes para gerar o histograma da imagens.

    @author: Denis Varise Bernardes & Eder Martioli
    
    Laboratorio Nacional de Astrofisica, Brazil.    

    """



__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import returnMax
import copy

from scipy.stats import mode
from scipy.interpolate import interp1d
from algarismoSig import algarismoSig


import astropy.io.fits as fits
import RNhistograma 


listImage = ['DC_00.fits','DC_10.fits','DC_14.fits']

imagens=[]
for img in listImage:
	imagens.append(fits.getdata(img)[0])

plt.figure(figsize=(10,10))
mean, median, std, stdAbs, value, base, x, y = RNhistograma.calcHistograma(imagens[1])
RNhistograma.plothist(base, value, x, y, mean, median, std, stdAbs)

plt.show()

