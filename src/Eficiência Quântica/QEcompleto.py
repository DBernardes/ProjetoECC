#!/usr/bin/python
# coding=<UTF-42>

"""
    Criado em 29 de Setembro de 2016  
    Descricao: Este codigo reune todas as bibliotecas necessarias para a caracterizacao da Eficiencia Quantica. Nele constam a makeList_imagesInput, QE_GraphLib, QE_readImages_Arq, QE_calcFluxo, QE_calcBackground_Images. O codigo cria uma lista das imagens fornecidas e, combinando-as de n em n imagens (onde n e um parametro fornecido), cria um diretorio com com essas novas imagens combinadas pela mediana. Apos isso, gera uma mascara de um caixa cuja a area e igual a area do chip do detector de referencia calculando a mediana do background para a regiao externa a essa caixa. Sobre a regiao interna e calculado o fluxo do CCD, dividindo-o pelo valor do fluxo do detector (fornecido o arquivo de dados); o resultado e um vetor utilizado para plotar o grafico da eficiencia quantica. Para mais detalhes, consulte a descricao propria das bibliotecas. 
    @author: Denis Varise Bernardes & Eder Martioli
    
    Laboratorio Nacional de Astrofisica, Brazil.
    
  
    """

__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """

import os, sys
import astropy.io.fits as fits
import matplotlib.pyplot as plt
import numpy as np
import logfile as l
import datetime

from makeList_imagesInput import criaArq_listaImgInput
from optparse import OptionParser
from QE_GraphLib import plotGraph, parametrosGraph
from QE_readImages_Arq import mkDir_saveCombinedImages, readArqDetector, ImagemUnica_returnHeader, LeArqFluxoCamera
from QE_calcFluxo import  GeraVetorFluxoCamera, FluxoRelativo
from QE_calcBackground_Images import LeBackgroundImagens_saveArquivoMedianBackground

parser = OptionParser()
parser.add_option("-d", "--detect", dest="detect", help="detector values",type='string',default="")
parser.add_option("-s", "--spectro", dest="spect", help="spectro values",type='string',default="")
parser.add_option("-l", "--logfile", dest="log", help="make logfile",type='string',default="")
parser.add_option("-v", action="store_true", dest="verbose", help="verbose",default=False)
parser.add_option("-r",'--range',dest="Range",type = 'string', help='Intervalo do Espectro', default ='')
parser.add_option("-n", "--nImages", dest="nImages", help="number images",type='string',default="")
parser.add_option("-c", "--calibD", dest="calibD", help="nome arq calibracao Detector",type='string',default="")
parser.add_option("-g", "--ganho", dest="ganho", help="Ganho do CCD",type='int',default=1)
nowInitial = datetime.datetime.now()

try:
    options,args = parser.parse_args(sys.argv[1:])
except:
    print "Error: check usage with ./QEcompleto.py -h ";sys.exit(1);

if options.verbose:
    print 'Lista de imagens: ', options.list

#retorna os valores de espectro para um intervalo de EQ
def returnInterval(x,f):
	if options.Range:
		vetor = tuple(options.Range.split(','))
		vetor = [int(vetor[0]),int(vetor[1])]
		print 'Espectro (nm)\t'+'EQ (%)'
		for data in x:	
			if vetor[0] < f(data) < vetor[1]:
				print ' ',round(data,2),'\t', round(f(data),2)

#------------------------------------------------------------------------------------------
nImages = int(options.nImages) #numero de imagens para cada comprimento de onda
intervEspectro = options.spect
nomeArqDetector = options.detect
nomeArqCalibDetector = options.calibD
ganhoCCD = options.ganho

#cria um arquivo contendo o nome das imagens obtidas para a caracterizacao
#criaArq_listaImgInput(nImages)

#le o header de uma unica imagem para retirada de informacoes de tamanho e coords. centrais
header = ImagemUnica_returnHeader()


#cria um diretorio com as imagens combinadas pela mediana
#mkDir_saveCombinedImages(nImages)


#realiza a leitura do background das imagens, salvando um arquivo com os valores medianos e respectivos desvios padrao
#LeBackgroundImagens_saveArquivoMedianBackground(header)


#gera os vetores de fluxo da camera e respectivo desvio padrao
GeraVetorFluxoCamera(header, nImages, ganhoCCD)

#le os dados do fluxo do CCD
vetorFluxoCamera, vetorSigmaBackground_Signal = LeArqFluxoCamera()
#le os dados do fotometros
valoresFotometro = readArqDetector(nomeArqDetector)


#divide os valores do fluxo da camera pelo detector
vetorEQ, vetorSigmaTotal = FluxoRelativo(vetorFluxoCamera, valoresFotometro, vetorSigmaBackground_Signal, intervEspectro, nomeArqCalibDetector)


#retorna os valores do espectro, interpolacao, EQmax, lambdaMax e absPorcent(porcent. de conversao)
espectro, interpolation, parametrosList = parametrosGraph(intervEspectro, vetorEQ)


#plota o grafico e imprime os valores na tela
plotGraph(espectro, vetorEQ, vetorSigmaTotal, parametrosList)


#retorna no terminal os valores de EQ para um dado intervalo (opcional)
returnInterval(espectro, interpolation)


plt.savefig('Eficiencia Quantica', format='jpg')
passo = (espectro[-1]-espectro[0])/len(espectro)+1
dic = {'qtdImagens':len(espectro)*nImages,'minute':nowInitial.minute, 'second':nowInitial.second,'header':header,'espectro':(espectro[0],espectro[-1],passo)}

l.logfile(options.log, dic)

