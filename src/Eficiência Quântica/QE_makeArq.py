#!/usr/bin/python
# coding=<UTF-42>

"""
    Criado em 29 de Setembro de 2016  
    Descricao: Esta biblioteca possui as seguintes funcoes:

	criaArq_listaImgInput: para as imagens situadas no diretorio atual, esta funcao cria uma lista com os nomes dos conjuntos de imagens que possuam a incidencia de luz de mesmo comprimento de onda.

	criaArq_infoEnsaio: esta funcao cria um arquivo para ser preechido contendo as informacoes necessarias do ensaio.
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
	

def criaArq_infoEnsaio():
	Str = ['Arquivo com as informacoes necessarias para caracterizacao da eficiencia quantica do CCD.\n', 'Espectro (nm) (Einicial, Efinal, passo) = ', 'Numero de imagens para cada comprimento de onda = ', 'Tempo exposicao do detector = ', 'nome arquivo calibracao detector = ', 'nome arquivo QE do fabricante = ', 'nome arquivo detector = ', 'nome arquivo Log = ', 'ganho = ']
	try: open('InformacoesEnsaio')
	except:
		name = 'InformacoesEnsaio'
		print '\n---Preencha o arquivo InformacoesEnsaio---\n'
		arq = open(name, 'w')		
		for dado in Str:
			arq.write(dado+'\n')
		arq.close()
		exit()

	with open('InformacoesEnsaio') as arq:
		nImages, Texp_Detector, ganhoCCD = 0, 0, 0
		nomeArqCalibDetector, noemArqFabricante, nomeArqDetector, nomeArqlog, intervEspectro = '', '', '', '', ''
		linhas = arq.read().splitlines()[2:]
		for linha in linhas:
			dado = linha.split('=')
			if 'Espectro' in dado[0]:
				intervEspectro = dado[1]

			if 'Numero de imagens para cada comprimento de onda' in dado[0]:
				try: nImages = int(dado[1])					
				except: 
					print '\nErro na leitura do numero de imagens para cada comprimento de onda.\n'
					exit()

			if 'Tempo exposicao do detector' in dado[0]:
				try: Texp_Detector = float(dado[1])
				except: 
					print '\nErro na leitura do Tempo exposicao do detector.\n'
					exit()

			if 'nome arquivo calibracao detector' in dado[0]:
				nomeArqCalibDetector = dado[1]

			if 'nome arquivo QE do fabricante' in dado[0]:
				noemArqFabricante = dado[1]

			if 'nome arquivo detector' in dado[0]:
				nomeArqDetector = dado[1]

			if 'nome arquivo Log' in dado[0]:
				nomeArqlog = dado[1]

			if 'ganho' in dado[0]:
				try: ganhoCCD = float(dado[1])
				except: 
					print '\nErro na leitura do ganho do CCD.\n'
					exit()
		arq.close()

		return nImages, Texp_Detector, ganhoCCD, nomeArqCalibDetector, noemArqFabricante, nomeArqDetector, nomeArqlog, intervEspectro
	

