#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    Criado em 08 de Novembro de 2016  
    Descricao: este modulo tem como entrada duas series de dados flat, retornando a intensidade do sinal e a variancia da serie apos a correcao do flat field, alem da dimensao da caixa de pixels utilizada para o calculo destes parametros.
    
    Laboratorio Nacional de Astrofisica, Brazil.    
"""



import numpy as np

def flatCorrection(flatA, flatB, box=50):
	b = box/2
	sinal = []
	Vetorvariance = []
	img = 0
	vetor = np.zeros((box,box))
	centerX = len(flatA[0])/2
	centerY = len(flatA[0][0])/2	

	while img < len(flatA):
		boxA = flatA[img][centerX-b:centerX+b,centerY-b:centerY+b]
		boxB = flatB[img][centerX-b:centerX+b,centerY-b:centerY+b]
		meanA = np.mean(boxA)
		meanB = np.mean(boxB)
		r = meanA/meanB	
		i=0
		while i < box:
			j=0
			while j < box:
				vetor[i][j] = boxB[i][j]*r
				j+=1
			i+=1
		subtract = boxA - vetor 		
		variance = (np.std(subtract)**2)/2
		sinal.append(meanA)
		Vetorvariance.append(variance)
		img+=1
	return sinal, Vetorvariance, box
