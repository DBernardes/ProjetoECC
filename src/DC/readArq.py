#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Criado em 10 de Agosto 2016
Descricao: esta bilbioteca possui as seguintes funcoes:
		readArq_returnListDirectories: esta funcao faz a leitura do arquivo Directories, returnando uma lista com o nome dos diretorios que contem as imagens de dark.

		readArq_returnListImages: esta funcao faz a leitura dos arquivos que contem os nomes das imagens de dark e bias, retornando um vetor dessas listas.
		
@autor: Denis Bernardes & Eder Martioli
Laboratorio Nacional de Astrofisica, Brazil
"""


def readArq_returnListDirectories() :
	with open('Directories') as f:
   		lines = f.read().splitlines()	
	return lines


def readArq_returnListImages(keyword):
	with open(keyword+'list') as f:
   		lines = f.read().splitlines()
	return lines
