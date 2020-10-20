#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    Criado em 08 de Novembro de 2016  
    Descricao: este codigo reune todas as bibliotecas responsaveis para a caracterizacao do ganho do CCD, sao elas:
    plotGraph, logfile, makeList_imagesInput e Gain_processesImages. O codigo ira criar duas listas de imagens: flat e bias,
    realizando o calculo da instensidade do sinal em funcao da variancia. Esses dados serao usado na plotagem de um grafico linear
    e, por meio do coeficiente angular de um ajuste linear calculado,  obtem-se o ganho; um segundo grafico e plotado onde
    aparece o resultado da subtracao dos dados obtidos pelos valores de um ajuste linear calculado.
    @author: Denis Varise Bernardes & Eder Martioli
    
    Laboratorio Nacional de Astrofisica, Brazil.

    
	example: ./ganhoCompleto.py -f'Flat','nImages' -b'Bias' 

	Esta lista fornecida ao programa deve conter as imagens de bias e as imagens flat associdas em conjunto na forma
biasA,biasB,flatA,flatB.
   
    """

__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """



import os, sys
import matplotlib.pyplot as plt
import datetime


from optparse import OptionParser
from plotGraph import Graph_sinal_variance, Graph_residuos
from logfile import logfile
from makeList_imagesInput import criaArq_listaImgInput, LeArquivoReturnLista
from Gain_processesImages import calcXY_YerrorBar_XerrorBar, parametrosCaixaPixels
from criaArq_resultadoCaract import arquivoCaract

from astropy.io import fits


numeroImagens = 5
Flat_name = 'Flat'
Bias_name = 'Bias'
images_path = r'C:\Users\observer\Desktop\Imagens_ECC\Gain'
criaArq_listaImgInput(numeroImagens, Flat_name, images_path)
criaArq_listaImgInput(1, Bias_name, images_path)
listaBias = LeArquivoReturnLista(Bias_name+'list.txt', images_path)
listaFlat = LeArquivoReturnLista(Flat_name+'list.txt', images_path)

#----------------------------------------------------------------------------------------------------------------------
caixa_pixels = '512,512,100'
parametersBox = parametrosCaixaPixels(caixa_pixels, listaFlat[0])		
X,Y,SigmaTotal, XsigmaBar, sigmaBias = calcXY_YerrorBar_XerrorBar(listaFlat, listaBias, numeroImagens, parametersBox, images_path)

plt.figure(figsize=(17,8))
ganho = Graph_sinal_variance(X,Y,SigmaTotal, XsigmaBar, sigmaBias)
Graph_residuos(X,Y, SigmaTotal, images_path)


