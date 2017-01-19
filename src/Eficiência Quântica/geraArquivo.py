#!/usr/bin/python
# coding=UTF-8

"""
    Criado em 20 de Setembro de 2016.
    
    Descricão: este modulo tem pode input uma serie imagens obtidas pelo CCD, retornando uma imagem combinada de uma amostra dessa serie. Sobre os dados, e realizada uma mediana para cada pixel, salvando a imagem resultante no formato .fits

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



def geraArquivo(inputlist,n):
	scidata = []
	#vetor com os dados	
	for img in inputlist:
		scidata.append(img)
	
	#gera um outro vetor na classe CCDData
	x = []
	i = 0	
	while i < len(inputlist):
		x.append(CCDData(scidata[i], unit = 'adu'))
		i+=1
	
	combinedImage = Combiner(x)
	combinedImageMedian = combinedImage.median_combine() #average_combine
	NPcombinedImage = np.asarray(combinedImageMedian)

	if n < 10: string = '00%i'%(n)
	if 10 <= n < 99: string = '0%i'%(n)
	if n >= 100: string = '%i'%(n)

	try:
		fits.writeto('ImagemCombinada%s.fits'%(string),NPcombinedImage, clobber=True)
		print 'ImagemCombinada%s.fits'%(string)
	except:
		print 'Erro ao salvar o arquivo.'	
	return 





