#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    Criado em 19 de Setembro de 2016  
    Descricao: este script reune todos as rotinas responsaveis pela completa caracterizacao da corrente de escuro:
    DCderivada, DCvariacaoTemporal, geraArquivo,caixaPixels, makeList_cwd, readArq, logfile. Este codigo faz uso de
    listas de imagens obtidas para diferentes temperaturas para gerar um grafico da variacao temporal da mediana das
    contagens das  imagens fornecidas (em funcao do tempo de exposicao); para as imagens de menor temperatura, gera
    dois graficos da variacao da corrente de escuro ao longo dos eixos  x e y.
	Deve ser criado um diretorio contendo as imagens adquiridas para cada temperatura. Para cada diretorio, o
	código gera uma lista de imagens de bias e dark, utilizando-as no processo de leitura. As imagens bias sao
	lidas atraves da funcao readArq_returnListImages. Sobre essa lista cria uma nova imagem de bias chamada
	ImgReduce proveniente da combinacao pela mediana das imagens bias. Em seguida, faz a leitura do arquivo de
	imagens DC tambem atraves da funcao readArq_returnListImages; esta lista e passada para a funcao
	criaArq_DadosTemporais responsavel por gerar um arquivo chamado Arquivo_DadosTemporais para cada diretorio
	contendo o valor da mediana e desvio padrao da serie de imagens. Esse arquivo será lido pela funcao
	DCvariacaoTemporal, responsavel por gerar um grafico da variacao da mediana das imagens em funcao do tempo de exposicao.
        A funcao chamada DCderivada ira receber a ultima lista de imagens de dark lidas no loop, utilizando-a no calculo
        da corrente de escuro da serie de imagens em funcao dos eixos x e y. Para maiores detalhes, consulte a descricao
        da propria biblioteca.


    @author: Denis Varise Bernardes & Eder Martioli
    
    Laboratorio Nacional de Astrofisica, Brazil. 

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


import DCvariacaoTemporal
import DCespacial
import DCReadArq
import DCgeraArquivo
from optparse import OptionParser
from criaArq_resultadoCaract import arquivoCaract
from logfile import CriaLogfile
from sys import exit


##parser = OptionParser()
##parser.add_option("-i", "--directories", dest="directories", help="Keyword para diretorios",type='string',default="")
##parser.add_option("-b", "--bias", dest="bias", help="Keyword para imagens bias",type='string',default="")
##parser.add_option("-d", "--dark", dest="dark", help="Keyword para imagens dark",type='string',default="")
##parser.add_option("-e", "--etimekey", dest="etimekey", help="Keyword para tempo de exposicao",type='string',default="EXPOSURE")
##parser.add_option("-l", "--logfile", action='store_true', dest="logfile", help="Log file name", default=False)
##parser.add_option("-c", "--box", dest="box", help="caixa de pixels",type='string',default="")
##parser.add_option("-g", "--gain", dest="gain", help="ganho do CCD",type='string',default='')
##try:
##    options,args = parser.parse_args(sys.argv[1:])
##except:
##    print "Error: check usage with ./DCCharact.py -h ";sys.exit(1);
##

class DarkCurrent:
	
	def __init__(self, ccd_gain, dir_path, pixels_box = False, bias_tag = 'Bias', dc_tag = 'DC', texp_tag='exposure', directories_tag = 'DC'):
		nowInitial = datetime.datetime.now()
		self.minute = nowInitial.minute
		self.second = nowInitial.second
		self.dir_path = dir_path
		self.Keywords = [bias_tag, dc_tag]	
		self.KeyWordDirectories = directories_tag
		self.ganho = ccd_gain
		self.pixels_box = pixels_box
		self.Dic = {'qtdImagesBias':0, 'qtdImagesDark':0, 'minute':self.minute, 'second':self.second, 'tagBias':bias_tag, 'tagDark':dc_tag}

		def criaArq_listaDirectories():
			s=''	
			listaArquivos = os.listdir(self.dir_path)
			listaArquivos.sort()
			for arq in listaArquivos:
				if self.KeyWordDirectories in arq:
					s += str(arq)+'\n'
			try:
				logf = open('Directories', 'w') 
			except:
				name.remove()
				logf = open('Directories', 'w')
			logf.write(s)
			logf.close()
			
	
	
		def returnListDirectories():
			with open('Directories') as f:
   				self.Directories = f.read().splitlines()	

		
		def criaListas_Dark_Bias(nImages=1):
			for Dir in self.Directories:
				chdir = self.dir_path + '\\' + Dir		
				os.chdir(chdir)			
				listaImagens = os.listdir(chdir)				
				for keyword in self.Keywords:
	
					listaImagensFiltrada = []
					for img in listaImagens:
						if keyword in img and '.fits' in img:
							listaImagensFiltrada.append(img)
					listaImagensFiltrada.sort()
	
					s,i='',0
					for img in listaImagensFiltrada:
						if i%nImages == nImages-1:  
							s += str(img)+'\n'
						else: 
							s += str(img)+','
						i+=1
					name = keyword+'list'
					try:
						logf = open(name, 'w') 
					except:
						name.remove()
						logf = open(name, 'w')
					logf.write(s)
					logf.close()
	
	
			
		def readArq_returnListaImgsBias_Dark():
			with open(self.Keywords[0]+'list') as arq:
				listaImagensBias = arq.read().splitlines()
				arq.close()
			with open(self.Keywords[1]+'list') as arq:
				listaImagensDC = arq.read().splitlines()
				arq.close()		

		criaArq_listaDirectories()
		returnListDirectories()	
		criaListas_Dark_Bias()
		os.chdir(self.dir_path)	
		


	def caractTemporal(self):
                for Dir in self.Directories:
                    chdir = self.dir_path + '/' + Dir
                    os.chdir(chdir)
                    print(chdir)
                    
                    #cria imagem bias para reducao dos dados
                    listaImgBias = DCReadArq.returnListImages(self.Keywords[0])	
                    CombinedImgBias = DCgeraArquivo.criaImgBias_Reduction(listaImgBias)
                    self.Dic['qtdImagesBias'] += len(listaImgBias)
            
                    listaImgDark = DCReadArq.returnListImages(self.Keywords[1])	
                    header = fits.getheader(listaImgDark[0])
                    self.Dic['header'] = header
                    self.Dic['qtdImagesDark'] += len(listaImgDark)

                    xcoord = int(header['naxis1']/2)
                    ycoord = int(header['naxis2']/2)
                    dimension = 100
                    
                    if self.pixels_box:
                            parametros = tuple(self.pixels_box.split(','))
                            xcoord = int(parametros[0])
                            ycoord = int(parametros[1])
                            dimension = int(parametros[2])                  
                    parametrosBox = [xcoord,ycoord,dimension]                    
                    self.Dic['parametrosBox'] = parametrosBox
                    DCgeraArquivo.infoCaractTemporal(listaImgDark,parametrosBox)
            

	def DiretorioMenorTemperatura(self):
		#verifica qual o diretorio com a menor temperatura e retorna seu nome
		self.vetorTemp=[]
		TempMin= 0
		for Dir  in self.Directories:
			chdir = self.dir_path + '/' + Dir
			os.chdir(chdir)
			self.listaImgDark = DCReadArq.returnListImages(options.dark)
			header=fits.getheader(self.listaImgDark[0])
			self.vetorTemp.append(header['temp'])
			if header['temp'] < TempMin:
				TempMin = header['temp']
				DiretorioTempMin = Dir		
		os.chdir(self.dir_path + '/' + DiretorioTempMin)					
	

	def CaractTemporal(self):
		self.DCnominal = DCvariacaoTemporal.caractTemporal(self.dir_path, self.Directories, self.vetorTemp, self.ganho)	

	def CaractEspacial(self):
		DCespacial.CaractDCEspacial(self.listaImgDark, self.ganho)
		os.chdir(self.dir_path)

	def LogFile(self):
		if options.logfile:
			CriaLogfile(self.Dic, self.DCnominal)




