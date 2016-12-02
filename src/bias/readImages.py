#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    Criado em 2 de Dezembro de 2016  
    Descricao: este modulo tem como funcao ler as imagens fornecidas e retornar as listas apropriadamente separadas.
    
    @author: Denis Varise Bernardes & Eder Martioli
    
    Laboratorio Nacional de Astrofisica, Brazil.

    
	example: ./biasCompleto.py --list=list
   
    """

__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.

    """

from divideLista import calcIteracao
import astropy.io.fits as fits


def Lefragmentos(lista):
	#separada a lista total e fragmentos menores 
	listaSeparada = calcIteracao(lista)
	dados1, dados2, dados3, dados4, dados5, dados6, contador = [], [], [], [], [], [], 1
	for lista in listaSeparada:		
		for img in lista:
			if contador==1:
				dados1.append(fits.getdata(img, 0)[0])
			if contador==2:
				dados2.append(fits.getdata(img, 0)[0])
			if contador==3:
				dados3.append(fits.getdata(img, 0)[0])
			if contador==4:
				dados4.append(fits.getdata(img, 0)[0])
			if contador==5:
				dados5.append(fits.getdata(img, 0)[0])
			if contador==6:
				dados6.append(fits.getdata(img, 0)[0])
		contador +=1
		
	print len(dados1),len(dados2),len(dados3),len(dados4),len(dados5), len(dados6)

		

