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



def criaArq_listaImgMedidas(nImages, tag):
	s, i='',0
	listaImagens = os.listdir(cwd)
	listaImagensFiltrada = []
	for img in listaImagens:
		if '.fits' in img and tag in img:
			listaImagensFiltrada.append(img)
	listaImagensFiltrada.sort()
	
	
	for img in listaImagensFiltrada:
		s += str(img)+'\n'
		
	name = tag+'List.txt'
	try:
		logf = open(name, 'w') 
	except:
		name.remove()
		logf = open(name, 'w')
	logf.write(s)		
	logf.close()



	

def criaArq_infoEnsaio():

	Str = ['Arquivo com as informacoes necessarias para caracterizacao da eficiencia quantica do CCD.\n', '->', 'Espectro (nm) (Einicial, Efinal, passo) =', 'Numero de imagens para cada comprimento de onda =','nome arquivo calibracao filtro densidade =', 'nome arquivo QE do fabricante =', 'nome arquivo detector =', 'nome arquivo Log =','tag do nome das imagens (dado,referencia) =','ganho =', '<-']

	nota = ['\nNota: neste arquivo estao as principais informacoes referentes ao ensaio de caracterizacao da eficiencia quantica. Nele devem constar as seguintes informacoes:\n', '- Espectro (nm): espectro utilizado no ensaio (em nanometros); nele devem constar o comprimento de onda inicial, comprimento de onda final e o passo utilizado, respectivamente;', '- Numero de imagens adquiridas para cada comprimento de onda;', '- nome do arquivo contendo a curva de calibracao do filtro de densidade (opcional); nele devem constar os valores da curva de transmissao do filtro de densidade utilizado no ensaio. Caso esta opcao nao seja fornecida, o programa ira plotar a curva de EQ sem levar em consideracao a correcao do filtro;' , '- nome do arquivo contendo a curva de Eficiencia Quantica do fabricante (opcional);nele devem constar o par coordenado do comprimento de onda (em nm) pela eficiencia quantica do fabricante; Caso esse opcao nao seja fornecida, o codigo ira plotar apenas a curva de EQ obtida pelo ensaio de caracterizacao;','- nome do arquivo contendo os dados detector;este arquivo precisa conter apenas o valores medidos pelo detector (sem o comprimento de onda utilizado);', '- nome arquivo Log (opcional);','- uma tag (nome ou parte do nome) das imagens, separados por virgulas, obtidas como dados e das imagens obtidas como referencia para que o programa possa separar cada serie de imagens em uma lista diferente;', '- ganho do CCD;','\nApos o preenchimento das informacoes pedidas, execute novamente o comando para obter a caracterizacao da curva de EQ do CCD.\n','As opcoes marcadas com \'(opcional)\' nao necessitam ser preenchidas, no momento dos calculos o codigo apenas levara em consideracao caso seja fornecido o nome de um arquivo.\n','O codigo apenas levara em consideracao os parametros situados dentro das tags \'->\' e \'<-\'; respeitando essa opcao, a organizacao dos dados pode ser feita da forma mais conveniente, permitindo comentarios e espacamento de linhas.\n','Os arquivos contendo dados a serem lidos devem conter o mesmo numero de dados em relacao ao numero de comprimentos de onda do ensaio.\n', 'obs: nao deve haver espaco entre o nome de cada arquivo e o sinal de igualdade, caso contrario, o programa retornara um erro.'] 

	try: open('InformacoesEnsaio')
	except:
		name = 'InformacoesEnsaio'
		print '\n---Preencha o arquivo InformacoesEnsaio---\n'
		arq = open(name, 'w')		
		for Strdado in Str:
			arq.write(Strdado+'\n')
		
		for StrNota in nota:
			arq.write(StrNota+'\n')

		arq.close()
		exit()

	with open('InformacoesEnsaio') as arq:		
		linhas = arq.read().splitlines()

		for linha in linhas:			
			if '->' == linha: tag1 = linha
			if '<-' == linha: 
				tag2 = linha
				break
		if tag1 != '->' : 
			print '\n Tag \'->\' nao encontrada.\n'
			exit()
		if tag2 != '<-' : 
			print '\n Tag \'<-\' nao encontrada.\n'
			exit()


		for linha in linhas:
			if '->' in tag1:
				dado = linha.split('=')				
				if 'Espectro (nm) (Einicial, Efinal, passo)' in dado[0]: intervEspectro = dado[1]

				if 'Numero de imagens para cada comprimento de onda' in dado[0]:
					try: nImages = int(dado[1])					
					except: 
						print '\nErro na leitura do numero de imagens para cada comprimento de onda.\n'
						exit()
		
				if 'nome arquivo calibracao filtro densidade' in dado[0]: nomeArqCalibDetector = dado[1]

				if 'nome arquivo QE do fabricante' in dado[0]: nomeArqFabricante = dado[1]

				if 'nome arquivo detector' in dado[0]: nomeArqDetector = dado[1]

				if 'nome arquivo Log' in dado[0]: nomeArqlog = dado[1]

				if 'tag do nome das imagens (dado,referencia)' in dado[0]: tagDado, tagRef = dado[1].split(',')

				if 'ganho' in dado[0]:
					try: ganhoCCD = float(dado[1])
					except: 
						print '\nErro na leitura do ganho do CCD.\n'
						exit()		
			if '<-' in linha: break
		

		return nImages, ganhoCCD, nomeArqCalibDetector, nomeArqFabricante, nomeArqDetector, nomeArqlog, intervEspectro, tagDado, tagRef
	

