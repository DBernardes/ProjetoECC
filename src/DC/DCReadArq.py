#!/usr/bin/python
# coding=UTF-8

"""
    Criado em 16 de Janeiro de 2017
    
	Descricao: esta biblioteca possui as seguintes funcoes:
		readArq_DadosTemporais: esta funcao faz a leitura do arquivo Arquivo_DadosTemporais gerado pela funcao criaArq_DadosTemporais, retornando os parametros e tabelas nela contidos.

		readArq_Etime: esta funcao realiza a leitura do arquivo Arquivo_Etime gerado pela funcao criaArq_DadosTemporais, retornando um vetor contendo seus valores.
  
    
    @author: Denis Varise Bernardes & Eder Martioli
    
    Laboratorio Nacional de Astrofisica, Brazil.    
 
    """

__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """



def infoCaractTemporal():
	VetorImgMedian, VetorStdImg = [], []
	with open('infoCaractTemporal') as arq:
		Linhas = arq.read().splitlines()
		arq.close()	
	coefAjust = float(Linhas[0].split('=')[1])
	intercept = float(Linhas[1].split('=')[1])
	stdLinAjust = float(Linhas[2].split('=')[1])
	for linha in Linhas [4:]:
		dados = linha.split('\t\t')
		VetorImgMedian.append(float(dados[0]))
		VetorStdImg.append(float(dados[1]))		
	return VetorImgMedian, VetorStdImg, coefAjust, intercept, stdLinAjust



def Etime():
	VetorEtime=[]
	with open('Arquivo_Etime') as arq:
		Linhas = arq.read().splitlines()
		arq.close()
	for linha in Linhas[1:]:
		VetorEtime.append(float(linha))
	return VetorEtime



def returnListDirectories() :
	with open('Directories') as f:
   		lines = f.read().splitlines()	
	return lines



def returnListImages(keyword):
	with open(keyword+'list') as f:
   		lines = f.read().splitlines()
	return lines
