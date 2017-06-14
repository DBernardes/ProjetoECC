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

from optparse import OptionParser

from QE_makeArq import criaArq_listaImgMedidas, criaArq_infoEnsaio
from QE_GraphLib import plotGraph, parametrosGraph
from QE_reduceImgs_readArq import mkDir_saveCombinedImages, mkDir_ImgPair, readArqDetector, ImagemUnica_returnHeader, LeArqFluxoCamera
from QE_calcFluxo import  GeraVetorFluxoCamera, FluxoRelativo
from criaArq_resultadoCaract import arquivoCaract

parser = OptionParser()
parser.add_option("-v", action="store_true", dest="verbose", help="verbose",default=False)
parser.add_option("-r",'--range',dest="Range",type = 'string', help='Intervalo do Espectro', default ='')

nowInitial = datetime.datetime.now()

try:
    options,args = parser.parse_args(sys.argv[1:])
except:
    print "Error: check usage with ./QEcompleto.py -h ";sys.exit(1);

if options.verbose:
    print 'Lista de imagens: ', options.list

minute = nowInitial.minute
second = nowInitial.second


#------------------------------------------------------------------------------------------
intervEspectro, nomeArqCalibDetector, noemArqFabricante, nomeArqDetector, nomeArqlog,  tagPAR2, tagPAR1, ganhoCCD, lenPixel, Dfotometro = criaArq_infoEnsaio()


#cria um arquivo contendo o nome das imagens obtidas para a caracterizacao
criaArq_listaImgMedidas(tagPAR2)
criaArq_listaImgMedidas(tagPAR1)


#le o header de uma unica imagem para retirada de informacoes de tamanho e coords. centrais
header = ImagemUnica_returnHeader(tagPAR2)


#cria um diretorio com as imagens combinadas pela mediana
mkDir_ImgPair(tagPAR2, tagPAR1, ganhoCCD)


#gera os vetores de fluxo da camera e respectivo desvio padrao
GeraVetorFluxoCamera(header, ganhoCCD, tagPAR2, tagPAR1, lenPixel, Dfotometro)

#le os dados do fluxo do CCD
vetorFluxoCamera, vetorSigmaBackground_Signal = LeArqFluxoCamera()
#le os dados do fotometros
valoresFotometro = readArqDetector(nomeArqDetector)


#divide os valores do fluxo da camera pelo detector
vetorEQ, vetorSigmaTotal = FluxoRelativo(vetorFluxoCamera, valoresFotometro, vetorSigmaBackground_Signal, intervEspectro, nomeArqCalibDetector)


#retorna os valores do espectro, interpolacao, EQmax, lambdaMax e absPorcent(porcent. de conversao)
espectro, interpolation, parametrosList = parametrosGraph(intervEspectro, vetorEQ)


#plota o grafico e imprime os valores na tela

plotGraph(espectro, vetorEQ, vetorSigmaTotal, parametrosList, noemArqFabricante)

passo = (espectro[-1]-espectro[0])/(len(espectro)-1)
dic = {'qtdImagens':len(espectro),'minute':minute,'second':second,'header':header,'espectro':(espectro[0],espectro[-1],passo), 'tagPAR2':tagPAR2, 'tagPAR1':tagPAR1, 'ValoresEspectro':espectro, 'ValoresEQ':vetorEQ}

if nomeArqlog != '': l.logfile(dic)
arqCaract = arquivoCaract()
arqCaract.criaArq(arqCaract)


