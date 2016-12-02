#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    Criado em 2 de Dezembro de 2016  
    Descricao: este modulo visa dividir a lista de imagens em partes minores para evitar sobrecarga de memoria no python.
    
    @author: Denis Varise Bernardes & Eder Martioli
    
    Laboratorio Nacional de Astrofisica, Brazil.

    
	example: ./biasCompleto.py --list=list
   
    """

__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.

    """
import astropy.io.fits as fits


def calcIteracao(lista):
	imagem = fits.getdata(lista[0])
	qtdElementos =len(lista)*len(imagem[0])*len(imagem[0][0])
	#500.000.000 e aproximadamento o numero maximo de elementos dentro de cada array suportados pelo python.
	qtdIteracoes = qtdElementos/500000000 + 1
	qtdImagens = 500000000/(len(imagem[0])*len(imagem[0][0]))
	i, listaSeparada = 0, []	
	while i < qtdIteracoes:
		listaSeparada.append(lista[i*qtdImagens:(i+1)*qtdImagens])
		i+=1
	return listaSeparada

		
