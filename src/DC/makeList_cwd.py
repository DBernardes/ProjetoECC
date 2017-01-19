#!/usr/bin/python
# coding=<UTF-42>

"""
    Criado em 29 de Setembro de 2016  
    Descricao: esta biblioteca possui as seguintes funcoes:

		criaArq_listaImgInput: esta funcao recebe uma keyword (parte do nome) das imagens como forma de identifica-las e, sobre a lista de arquivos do diretorios atual, gera um arquivo contendo uma lista dos nomes das imagens. 

		criaArq_listaDirectories: esta funcao recebe um keywork (parte do nome) dos diretorios que contem as imagens, gerando um arquivo contendo uma lista destes nomes.

		criaListas_Dark_Bias: a chamada desta funcao cria uma lista das imagens de bias e dark para cada um dos diretorios.

    @author: Denis Varise Bernardes & Eder Martioli
    
    Laboratorio Nacional de Astrofisica, Brazil.
    
  
    """

__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """

import os




def criaArq_listaImgInput(keyword, nImages=1):
	cwd = os.getcwd()
	s,i='',0	
	listaImagens = os.listdir(cwd)
	listaImagensFiltrada = []
	for img in listaImagens:
		if keyword in img and '.fits' in img:
			listaImagensFiltrada.append(img)
	listaImagensFiltrada.sort()

	for img in listaImagensFiltrada:
		if i%nImages == nImages-1:  
			s += str(img)+'\n'
		else: 
			s += str(img)+','
		i+=1
	name = keyword+'list'
	try:
		logf = open(name, 'w') 
	except:
		name.remove()
		logf = open(name, 'w')
	logf.write(s)
	logf.close()
	
	

def criaArq_listaDirectories(directories):
	cwd = os.getcwd()
	s,i='',0	
	listaArquivos = os.listdir(cwd)
	listaArquivos.sort()

	for arq in listaArquivos:
		if directories in arq:
			s += str(arq)+'\n'
		
	try:
		logf = open('Directories', 'w') 
	except:
		name.remove()
		logf = open('Directories', 'w')
	logf.write(s)
	logf.close()



def criaListas_Dark_Bias(cwd, directiories, KW_bias, KW_dark):
	for Dir in directories:
		chdir = cwd + '/' + Dir
		os.chdir(chdir)
		criaArq_listaImgInput(KW_bias)
		criaArq_listaImgInput(KW_dark)

	
