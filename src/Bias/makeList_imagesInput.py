#!/usr/bin/python
# coding=<UTF-42>

"""
    Criado em 29 de Setembro de 2016  
    Descricao: esta bilioteca possui as seguintes funcoes:
		
		criaArq_listaImgInput: esta funcao faz a leitura das imagens presentes no diretorio atual, criando um arquivo com o nome dessas imagens.

		readArq_returnlistImages: esta funcao faz a leitura do arquivo gerado pela funcao criaArq_listaImgInput, retornando uma lista com o nome das imagens.
		
    @author: Denis Varise Bernardes & Eder Martioli
    
    Laboratorio Nacional de Astrofisica, Brazil.
    
  
    """

__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """

import os

cwd = os.getcwd()


def criaArq_listaImgInput(nImages=1):
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



def readArq_returnlistImages():
	with open('listaImagens') as f:
   		lines = f.read().splitlines()
	return lines


	
	
