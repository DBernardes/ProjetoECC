#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    Criado em 19 de Novembro de 2016  
    
    @author: Denis Varise Bernardes & Eder Martioli
    Descricao: esta biblioteca possui as seguintes funcoes:

		LeBackgroundImagens_saveArquivoMedianBackground: esta funcao tem como entrada o header de uma unica imagem,  utilizando-o para criar uma mascara de pixels. Essa mascara é fornecida para a funcao geraVetor_Background_Std;

		geraVetor_Background_Std: esta funcao tem como input uma mascara de pixels, usando-a para calcular o valor da mediana e do desvio padrao do background de uma lista de imagens para a regiao externa a essa mascara. A saida e um vetor contendo tais dados.
		
		CriaAqruivo_dadosBackground: esta funcao recebe uma lista de dois vetores, escrevendo em um arquivo chamado dadosBackground.dat o conteudo deste vetores separados em colunas.

    Laboratorio Nacional de Astrofisica, Brazil.   
	
   
    """

__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """

import os
import astropy.io.fits as fits
import numpy as np
import matplotlib.pyplot as plt


cwd = os.getcwd()
chdir = cwd + '/' + 'Mediana das Imagens'


def LeBackgroundImagens_saveArquivoMedianBackground(header):
	imgShape = (header['naxis1'], header['naxis1'])

	print 'Calculando o ruido de fundo de cada imagem...'
	coordx, coordy, d = imgShape[0]/2, imgShape[1]/2, 815/2	
	working_mask = np.ones(imgShape,bool)
	ym, xm = np.indices(imgShape, dtype='float16') 
	A = (ym < coordy-d)+(coordy+d < ym)
	B = (xm < coordx-d)+(coordx+d < xm)
	An = (coordy-d < ym)*(ym < coordy+d)
	Bn = (coordx-d < xm)*(xm < coordx+d)
	mask = [An*B+Bn*A+A*B]*working_mask
	mask = mask[0]
	vetorBackground, vetorStd = geraVetor_Background_Std(mask)
	dadosBackground = [vetorBackground, vetorStd]
	CriaAqruivo_dadosBackground(dadosBackground)



def geraVetor_Background_Std(mask):
	os.chdir(chdir)
	vetorBackground, vetorStd = [], []
	with open('listaImagensCombinadas') as arq:
		listaImagens = arq.read().splitlines()
		for img in listaImagens:
			data = fits.getdata(img)[0]
			pixelsBackground = data[np.where(mask)]
			#inverseMask = np.logical_not(mask)
			medianBackground = np.median(pixelsBackground)
			stdBackground = np.std(np.abs(pixelsBackground - medianBackground))
			vetorBackground.append(medianBackground)
			vetorStd.append(stdBackground)
		arq.close()
	os.chdir(cwd)

	return vetorBackground, vetorStd




def CriaAqruivo_dadosBackground(dadosBackground):
	print '\tCriando arquivo dadosBackground.dat'
	name = 'dadosBackground.dat'
	try: logf = open(name,'w')
	except:
		name.remove()
		logf = open(name,'w')

	logf.write('Mediana (adu) \t\t Std (adu)\n')
	for i in range(len(dadosBackground[0])):
		Str = ' %f \t\t %f\n'%(dadosBackground[0][i], dadosBackground[1][i])
		logf.write(Str)		
	logf.close()
