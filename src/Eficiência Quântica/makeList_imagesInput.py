#!/usr/bin/python
# coding=<UTF-42>

"""
    Criado em 29 de Setembro de 2016  
    Descricao: Esta biblioteca possui uma funcao chamada criaArq_listaImgInput que, para as imagens situadas no diretorio atual, ela criara uma lista com os nomes dos conjuntos de imagens que possuam a incidencia de luz de mesmo comprimento de onda.
    @author: Denis Varise Bernardes & Eder Martioli
    
    Laboratorio Nacional de Astrofisica, Brazil.
    
  
    """

__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """

import os

cwd = os.getcwd()


def criaArq_listaImgInput(nImages):
	s,i='',0	
	listaImagens = os.listdir(cwd)
	listaImagensFiltrada = []
	for img in listaImagens:
		if '.fits' in img:
			listaImagensFiltrada.append(img)
	listaImagensFiltrada.sort()

	for img in listaImagensFiltrada:
		if i%nImages == nImages-1:  
			s += str(img)+'\n'
		else: 
			s += str(img)+','
		i+=1
	
	try:
		logf = open('listaImagens', 'w') 
	except:
		name.remove()
		logf = open('listaImagens', 'w')
	logf.write(s)
	logf.close()
	
	
