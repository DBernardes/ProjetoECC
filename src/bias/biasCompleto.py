#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    Criado em 29 de Agosto de 2016  
    Descricao: este modulo visa reunir os scripts geraArquivo.py, variacaoTemporal.py, gradiente.py e biashistogram.py em um unico arquivo, compilando-os e retornando um arquivo pdf com as informacoes do diagnostico obtido.
    
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
import ecc_utils as ecc
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

from optparse import OptionParser

nowInitial = datetime.datetime.now()
minute = nowInitial.minute
second = nowInitial.second

parser = OptionParser()
parser.add_option("-i", "--list", dest="list", help="imagens FITS",type='string',default="")
parser.add_option("-v", action="store_true", dest="verbose", help="verbose",default=False)
parser.add_option("-l", "--logfile", dest="logfile", help="Log file name",type='string',default="")

try:
    options,args = parser.parse_args(sys.argv[1:])
except:
    print "Error: check usage with ./calcbias.py -h ";sys.exit(1);

if options.verbose:
    print 'Lista de imagens: ', options.img

imagefiles = ecc.readlist(options.list) #lista de imagens
plt.figure(figsize=(22,28))
data, header = fits.getdata(imagefiles[0], header=True) #aquisicao do header
tempoExp = header['KCT']*len(imagefiles) # tempo total do experimento

variacaoTemporal(imagefiles, tempoExp)
CombinedImage = geraArquivo(imagefiles)
textGradiente = gradiente(CombinedImage)
textHistograma, BiasNominal = histograma(CombinedImage)
textstr = textGradiente + textHistograma
caixa(textstr, 4, 3, 0, 2, font=24, space=0.05, rspan=2)
	
plt.savefig('Relatório Bias', format='pdf')
plt.close()
lenDados = len(imagefiles)
dic = {'minute':minute, 'second':second, 'lenDados':lenDados, 'header':header, 'biasNominal':BiasNominal}
if options.logfile :
	logfile(options.logfile,dic)	


