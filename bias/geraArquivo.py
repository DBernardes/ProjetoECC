#!/usr/bin/python
# coding=UTF-8

"""
    Criado em 20 de Setembro de 2016.
    
    Descricão: este modulo tem pode input uma serie imagens obtidas pelo CCD, retornando uma imagem combinada de uma amostra dessa serie. Sobre os dados, foi realizada uma mediana para cada pixel em funcao do tempo; este resultado é utilizado pelos script gradiente.py e biashistogram.py no cálculo dos parâmetros de saída.
    
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



def geraArquivo(inputlist, Reduce=False):
	#vetor com os dados
	scidata = []
	if Reduce == True:
		Imin = len(inputlist)
		for img in inputlist:
			scidata.append(img)

	else:
		Imin=-10
		for img in inputlist[Imin-8:-8]:
			scidata.append(img)
	
	#gera um outro vetor na classe CCDData
	x = []
	i = 0	
	while i < np.abs(Imin):
		x.append(CCDData(scidata[i], unit = 'adu'))
		i+=1
	
	combinedImage = Combiner(x)
	combinedImageMedian = combinedImage.average_combine() #average_median
	NPcombinedImage = np.asarray(combinedImageMedian)
		
	try:
		fits.writeto('VariacaoMediana.fits',NPcombinedImage, clobber=True)	
	except:
		print 'Erro ao salvar o arquivo.'
	
	return NPcombinedImage





