#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    Criado em 29 de Agosto de 2016  
    Descricao: este modulo visa reunir as bibliotecas responsaveis para a caracterizacao do ruido de leitura: variacaoTemporal, geraArquivo, gradiente, biashistogram, CCDinfo, caixaTexto, logfile, makeList_imagesInput. O codigo ira criar um arquivo contendo a lista de nomes das imagens; dessa lista ira retirar uma amostra de 10 imagens e retorna-la para as funcoes gradiente e histograma. A funcao gradiente ira expressar em um grafico em cores a variacao das contagens dos pixels ao longo desta imagem mediana, junto de dois outros graficos da variacao da media das constagens ao longo de suas linhas e colunas; a funcao histograma ira calcular uma distribuicao de frequencia das contagens para um intervalo da media dos pixels +/- 7sigmas. A funcao variacaoTemporal ira receber a lista de imagens completa, retornando um grafico com a mediana das contagens de cada imagem em funcao do tempo do experimento. Sobre esses dados e realizada uma FFT; e gerada uma segunda lista de dados normais em relacao a media e desvio padrao dos dados originais, de modo que a FFT desta serie e plotada junto a primeira, permitindo comparar os picos com intensidade acima de media+3sigmas.
		
    
    @author: Denis Varise Bernardes & Eder Martioli
    
    Laboratorio Nacional de Astrofisica, Brazil.

    
	example: ./biasCompleto.py --list=list
   
    """

__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """

import os, sys
import astropy.io.fits as fits
import matplotlib.pyplot as plt
import datetime
import getpass
import socket

from variacaoTemporal import variacaoTemporal
from geraArquivo import geraArquivo
from gradiente import gradiente
from biashistogram import histograma
from CCDinfo import CCDinfo
from caixaTexto import caixaTexto as caixa
from logfile import logfile
from makeList_imagesInput import criaArq_listaImgInput, readArq_returnlistImages
from criaArq_resultadoCaract import arquivoCaract

from optparse import OptionParser

nowInitial = datetime.datetime.now()
minute = nowInitial.minute
second = nowInitial.second
cwd = os.getcwd()
BackDir = os.path.normpath(os.getcwd() + os.sep + os.pardir)

parser = OptionParser()
parser.add_option("-v", action="store_true", dest="verbose", help="verbose",default=False)
parser.add_option("-l","--logfile", action="store_true", dest="logfile", help="Log file",default=False)

try:
    options,args = parser.parse_args(sys.argv[1:])
except:
    print "Error: check usage with ./calcbias.py -h ";sys.exit(1);

if options.verbose:
    print 'Lista de imagens: ', options.img


criaArq_listaImgInput()
listaImagens = readArq_returnlistImages()
header = fits.getheader(listaImagens[0]) #aquisicao do header
Strtemperatura = [r'$\mathtt{Temperatura: %i^oC}$' %(header['temp'])]
tempoExperimento =	header['KCT']*len(listaImagens) # tempo total do experimento

plt.figure(figsize=(22,28))
CombinedImage = geraArquivo(listaImagens)
textGradiente = gradiente(CombinedImage)
textHistograma, BiasNominal = histograma(CombinedImage)
variacaoTemporal(listaImagens, tempoExperimento)

textstr =  Strtemperatura+ textGradiente + textHistograma
caixa(textstr, 4, 3, 0, 2, font=24, space=0.05, rspan=2)	

os.chdir(BackDir)
plt.savefig('Relatório Bias', format='pdf')
os.chdir(cwd)
dic = {'minute':minute, 'second':second,'biasNominal':BiasNominal, 'header':header}
if options.logfile :
	print 'Criando arquivo log', '\n'
	logfile(dic, listaImagens)	

os.chdir(BackDir)
arqCaract = arquivoCaract()
arqCaract.criaArq(arqCaract)


