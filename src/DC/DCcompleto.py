#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    Criado em 19 de Setembro de 2016  
    Descricao: este script reune todos as rotinas responsaveis pela completa caracterizacao da corrente de escuro: DCderivada, DCvariacaoTemporal, geraArquivo,caixaPixels, makeList_cwd, readArq, logfile. Este codigo faz uso de listas de imagens obtidas para diferentes temperaturas para gerar um grafico da variacao temporal da mediana das contagens das  imagens fornecidas (em funcao do tempo de exposicao); para as imagens de menor temperatura, gera dois graficos da variacao da corrente de escuro ao longo dos eixos  x e y.
	Deve ser criado um diretorio contendo as imagens adquiridas para cada temperatura. Para cada diretorio, o código gera uma lista de imagens de bias e dark, utilizando-as no processo de leitura. As imagens bias sao lidas atraves da funcao readArq_returnListImages. Sobre essa lista cria uma nova imagem de bias chamada ImgReduce proveniente da combinacao pela mediana das imagens bias. Em seguida, faz a leitura do arquivo de imagens DC tambem atraves da funcao readArq_returnListImages; esta lista e passada para a funcao criaArq_DadosTemporais responsavel por gerar um arquivo chamado Arquivo_DadosTemporais para cada diretorio contendo o valor da mediana e desvio padrao da serie de imagens. Esse arquivo será lido pela funcao DCvariacaoTemporal, responsavel por gerar um grafico da variacao da mediana das imagens em funcao do tempo de exposicao.
A funcao chamada DCderivada ira receber a ultima lista de imagens de dark lidas no loop, utilizando-a no calculo da corrente de escuro da serie de imagens em funcao dos eixos x e y. Para maiores detalhes, consulte a descricao da propria biblioteca.


    @author: Denis Varise Bernardes & Eder Martioli
    
    Laboratorio Nacional de Astrofisica, Brazil.
    
  	example: ./DCcompleto.py -iDirectories -bBias -dDark -eExposure -lLogfile
 

    """

__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """

import os, sys
import astropy.io.fits as fits
import numpy as np
import matplotlib.pyplot as plt
import datetime

from DCderivada import DCderivada
from DCvariacaoTemporal import DCvariacaoTemporal
from geraArquivo import CombinaImgs_salvaArquivoFITS, criaImgBias_Reduction, criaArq_DadosTemporais
from caixaPixels import caixaPixels
from makeList_cwd import criaArq_listaImgInput, criaArq_listaDirectories, criaListas_Dark_Bias
from logfile import logfile
from readArq import readArq_returnListDirectories, readArq_returnListImages

from optparse import OptionParser

nowInitial = datetime.datetime.now()
minute = nowInitial.minute
second = nowInitial.second

parser = OptionParser()
parser.add_option("-i", "--directories", dest="directories", help="Keyword para diretorios",type='string',default="")
parser.add_option("-b", "--bias", dest="bias", help="Keyword para imagens bias",type='string',default="")
parser.add_option("-d", "--dark", dest="dark", help="Keyword para imagens dark",type='string',default="")
parser.add_option("-e", "--etimekey", dest="etimekey", help="Keyword para tempo de exposicao",type='string',default="EXPOSURE")
parser.add_option("-l", "--logfile", dest="logfile", help="Log file name",type='string',default="")
parser.add_option("-v", action="store_true", dest="verbose", help="verbose",default=False)
parser.add_option("-c", "--box", dest="box", help="caixa de pixels",type='string',default="")

try:
    options,args = parser.parse_args(sys.argv[1:])
except:
    print "Error: check usage with ./calcbias.py -h ";sys.exit(1);

if options.verbose:
    print 'Lista de imagens: ', options.img



cwd = os.getcwd()
Dict = {'header':0, 'qtdImagens':0, 'Boxparameter':[], 'vetorTemp':[]}



#criaArq_listaDirectories(options.directories)
directories = readArq_returnListDirectories()
#criaListas_Dark_Bias(cwd, directiories, options.bias, options.dark)


for Dir  in directories:
	chdir = cwd + '/' + Dir
	os.chdir(chdir)
	print chdir
	
	#cria imagem bias para reducao dos dados
	listaImgBias = readArq_returnListImages(options.bias)
	criaImgBias_Reduction(listaImgBias)

	listaImgDark = readArq_returnListImages(options.dark)
	header = fits.getheader(listaImgDark[-1])		
	Dict['vetorTemp'].append(header['temp'])
	Dict['qtdImagens']+= len(listaImgDark)	
	Dict['header'] = header
	if options.box:
		parametros = tuple(options.box.split(','))
		xcoord = int(parametros[0])
		ycoord = int(parametros[1])
		dimension = int(parametros[2])
	else:
		xcoord = header['naxis1']/2
		ycoord = header['naxis2']/2
		dimension = 100

	parametros = [xcoord,ycoord,dimension]
	Dict['Boxparameter'] = parametros	
	criaArq_DadosTemporais(listaImgDark,parametros)


fig = plt.figure(figsize=(15,17))
DCnominal = DCvariacaoTemporal(cwd, directories, Dict['vetorTemp'])
#recebe as imagens do ultimo diretorio da lista
DCderivada(listaImgDark, header)


os.chdir(cwd)
plt.savefig('Relatório DC', format='pdf')
plt.close() 



# Gera arquivo log
if options.logfile :
	if options.box:
		logfile(options.logfile, nowInitial, minute, second, Dict, DCnominal, box=True)
	else:
		logfile(options.logfile, nowInitial, minute, second, Dict, DCnominal)



