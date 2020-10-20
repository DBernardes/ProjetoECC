#!/usr/bin/python
# coding=<UTF-42>

"""
    Criado em 29 de Setembro de 2016  
    Descricao: esta biblioteca possui as seguintes funcoes:
		criaArq_listaImgInput: dado o numero de imagens para cada intensidade de luz obtidas e parte do nome das imagens,
		que serve de referencia para o codigo identificar quais sao as imagens de bias e quais sao as de flat, a funcao criara
		um arquivo contendo uma lista com as imagens do ensaio.

		LeArquivoReturnLista: esta funcao faz a leitura do arquivo gerado pela funcao criaArq_listaImgInput, retornando um vetor
		contendo o nome das imagens. 

    @author: Denis Varise Bernardes & Eder Martioli
    
    Laboratorio Nacional de Astrofisica, Brazil.
    
  
    """

__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """

import os

cwd = os.getcwd()


def criaArq_listaImgInput(nImages, name, images_path):
	s,i='',0	
	listaImagens = os.listdir(images_path)
	listaImagensFiltrada = []
	for img in listaImagens:
		if '.fits' in img and name in img:
			listaImagensFiltrada.append(img)
	listaImagensFiltrada.sort()

	for img in listaImagensFiltrada:
		if i%nImages == nImages-1:  
			s += str(img)+'\n'
		else: 
			s += str(img)+','
		i+=1
	
	nameArq = images_path+ '\\'+ name+'list.txt'
	try:
		logf = open(nameArq, 'w') 
	except:
		name.remove()
		logf = open(nameArq, 'w')
	logf.write(s)
	logf.close()





def LeArquivoReturnLista(arquivo, images_path):	
	with open(images_path + '\\' + arquivo) as arq:
		lista = []
		linhas = arq.read().splitlines()
		for lin in linhas:			
			for img in lin.split(','):
				lista.append(img)
		arq.close()
	return lista
	
	
