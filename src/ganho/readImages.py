#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    Criado em 08 de Novembro de 2016  
    
    @author: Denis Varise Bernardes & Eder Martioli
    Descricao: este modulo tem como entrada uma lista de imagens fits, retornando um vetor das imagens em um array formato numpy, um vetor com os tempos de exposicao e o cabecalho das imagens.

    Laboratorio Nacional de Astrofisica, Brazil.

    
	example: ./biasCompleto.py --list=list
   
    """

__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """

import astropy.io.fits as fits


def readImages(lista):
	#le uma lista de imagens e retorna um vetor
	vetor = []	
	for img in lista:
		data, hdr = fits.getdata(img, header=True)
		vetor.append(data[0].astype(float))
	return vetor, hdr
