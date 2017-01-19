#!/usr/bin/python
# coding=UTF-8

"""
    Criado em 20 de Setembro de 2016.
    
    Descricão: este modulo tem pode input uma serie imagens obtidas pelo CCD, retornando uma imagem combinada de uma amostra dessa serie. Sobre os dados, foi realizada uma mediana para cada pixel, retornando um array no formato numpy.
    
    @author: Denis Varise Bernardes & Eder Martioli
    
    Laboratorio Nacional de Astrofisica, Brazil.    
 
    """

__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """

import numpy as np
import astropy.io.fits as fits

from ccdproc import Combiner, CCDData



def geraArquivo(inputlist):
	newlist, dados = [], []
	step,i = len(inputlist)/10, 0
	while i < 10:
		newlist.append(inputlist[i*step])
		i+=1
	for img in newlist:
		dados.append(fits.getdata(img, 0)[0])		
	#gera um outro vetor na classe CCDData
	x, i = [], 0
	while i < len(dados):
		x.append(CCDData(dados[i], unit = 'adu'))
		i+=1
	
	combinedImage = Combiner(x)
	combinedImageMedian = combinedImage.average_combine() #average_median
	NPcombinedImage = np.asarray(combinedImageMedian)	
	
	return NPcombinedImage





