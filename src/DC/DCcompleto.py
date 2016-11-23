#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    Criado em 19 de Setembro de 2016  
    Descricao: este script reune todos as rotinas resposaveis pela completa caracterizacao da corrente de escuro: gifImagens, DKderivada, DKvariacaoTemporal, geraArquivo,caixaPixels, readlist, logfile. Ele criara um grafico da variacao temporal das imagens fornecidas, assim como dois graficos da variacao da corrente de escuro ao longo dos eixos  x e y das imagens.

    @author: Denis Varise Bernardes & Eder Martioli
    
    Laboratorio Nacional de Astrofisica, Brazil.
    
  	example: ./DCcompleto.py -bBias -dDark -eExposure
 

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
from gifImagens import plotGif
from DCvariacaoTemporal import DCvariacaoTemporal, geraDados
from geraArquivo import geraArquivo
from caixaPixels import caixaPixels
from ecc_utils import readlist
from logfile import logfile

from optparse import OptionParser
from scipy import misc

nowInitial = datetime.datetime.now()
minute = nowInitial.minute
second = nowInitial.second

parser = OptionParser()
parser.add_option("-b", "--biaslist", dest="blist", help="imagens FITS de BIAS",type='string',default="")
parser.add_option("-d", "--darklist", dest="dlist", help="imagens FITS de DARK",type='string',default="")
parser.add_option("-e", "--etimekey", dest="etimekey", help="Keyword para tempo de exposicao",type='string',default="")
parser.add_option("-l", "--logfile", dest="logfile", help="Log file name",type='string',default="")
parser.add_option("-v", action="store_true", dest="verbose", help="verbose",default=False)
parser.add_option("-i", "--directory", dest="dirlist", help="Directorys with images",type='string',default="")
parser.add_option("-c", "--box", dest="box", help="caixa de pixels",type='string',default="")

try:
    options,args = parser.parse_args(sys.argv[1:])
except:
    print "Error: check usage with ./calcbias.py -h ";sys.exit(1);

if options.verbose:
    print 'Lista de imagens: ', options.img


directorys = readlist(options.dirlist)
cwd = os.getcwd()
Dict = {'vetoresMediana':[],'vetoresStd':[], 'vetoresAjust':[], 'vetoresCoef':[], 'vetoresEtime':[], 'vetorTemp':[], 'vetorTemp':[], 'cuboImagensTemporal':[], 'cuboImagensDerivada':[], 'etime':[], 'header':0, 'qtdImagens':0, 'Boxparameter':[]}

for Dir  in directorys:
	chdir = cwd + '/' + Dir
	os.chdir(chdir)
	print chdir

	#cria imagem para reducao dos dados
	imgReduce = 0
	bias = []
	if options.blist:
		imagefiles = readlist(options.blist)
		for img in imagefiles:
			bias.append(fits.getdata(img))		
		imgReduce = geraArquivo(bias, Reduce=True)

	#gera um cubo de imagens
	cuboImagensTemporal = []
	cuboImagensDerivada = []
	etime = []		
	if options.dlist:
		imagefiles = readlist(options.dlist)	
		data, Dict['header'] = fits.getdata(imagefiles[-1],header=True)		
		Dict['vetorTemp'].append(Dict['header']['temp'])
		Dict['qtdImagens']+= len(imagefiles)
		for img in imagefiles:
			scidata,hdr = fits.getdata(img,header=True)
			scidata = scidata.astype(float) - imgReduce
			scidata = scidata[0]
			cuboImagensDerivada.append(scidata)

			if options.box:
				scidata, xcoord, ycoord, dimenison = caixaPixels(scidata,options.box) #retira apenas uma caixa de pixels da imagem total
				Dict['Boxparameter'] = [xcoord, ycoord, dimenison]		
			
			cuboImagensTemporal.append(scidata)
			etime.append(hdr[options.etimekey])	

		#retorna os dados processados para funcao variacaoTemporal
		median, std, ajust, coefAjust = geraDados(cuboImagensTemporal, etime)
		Dict['vetoresMediana'].append(median)
		Dict['vetoresStd'].append(std)
		Dict['vetoresAjust'].append(ajust)
		Dict['vetoresCoef'].append(coefAjust[0])
		Dict['vetoresEtime'].append(etime)
		Dict['cuboImagens'] = cuboImagensTemporal
		Dict['cuboImagensDerivada'] = cuboImagensDerivada
		Dict['etime'] = etime

#plotGif(dados)
fig = plt.figure(figsize=(15,17))	
preamp = Dict['header']['preamp']
DCnominal = DCvariacaoTemporal(Dict)	
#recebe as imagens do ultimo diretorio da lista
DCderivada(Dict['cuboImagensDerivada'], Dict['etime'], preamp, Dict['vetorTemp'][-1])	


os.chdir(cwd)
plt.savefig('Relatório DC', format='pdf')
#plt.show()
plt.close() 



# Gera arquivo log
if options.logfile :
	if options.box:
		logfile(options.logfile, nowInitial, minute, second, Dict, DCnominal, box=True)
	else:
		logfile(options.logfile, nowInitial, minute, second, Dict, DCnominal)


	

