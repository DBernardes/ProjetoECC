#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    Criado em 08 de Novembro de 2016  
    
    @author: Denis Varise Bernardes & Eder Martioli
	descricao: este modulo possui como entrada o nome do arquivo log, um dicionario mais algumas informacoes que serao escritas em um arquivo texto. 
    
    Laboratorio Nacional de Astrofisica, Brazil.
   
    """

__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """
import getpass
import socket
import datetime
import os, sys

from CCDinfo import CCDinfo
from astropy.io import fits
from readArq import readArq_returnListDirectories, readArq_returnListImages


cwd = os.getcwd()

def logfile(Dic, DCnominal):

	minute = Dic['minute']
	second = Dic['second']
	header = Dic['header']
	tagBias = Dic['tagBias']
	tagDark = Dic['tagDark']
	parametrosBox = Dic['parametrosBox']	
	qtdImagesBias = Dic['qtdImagesBias']
	qtdImagesDark = Dic['qtdImagesDark']
	coordxBox = parametrosBox[0]
	coordyBox = parametrosBox[1]	
	dimensao = parametrosBox[2]
		
	now = datetime.datetime.now()
	commandline = sys.argv		

	Logdata = 'Caracterizacao da Corrente de escuro, ' + now.strftime("%Y-%m-%d %H:%M")
	user = 'Usuario: %s' %(getpass.getuser())
	IP = 'IP local: %s' %(socket.gethostbyname(socket.gethostname()))
	Strcommandline = 'Linha de comando: '
	for arg in commandline:
		Strcommandline += arg + ' ' 	
	WorkDirectory = 'Diretorio atual: ' + os.getcwd()	

	nowInitial = datetime.datetime.now()
	TimeElapsed = (nowInitial.minute - minute)*60 + (nowInitial.second - second) #hora final menos hora inicial 	
	Tempoprocess = 'Tempo de processamento: %i min %i s' %(TimeElapsed/60,TimeElapsed%60)

	Strbox = 'Opcao caixa de pixels: (x,y) = (%i,%i), dimensao = %i.' %(coordxBox,coordyBox,dimensao) + '\n\n'
	
	CCDstr = CCDinfo(header, qtdImagesBias,qtdImagesDark)
	DCnominal = 'Corrente de escuro: %s +/- %s e-/pix/s' %(DCnominal[0], DCnominal[1])


	StrNomeImagens =  '\t\tArquivo\t\t\t CDDTemp (ºC)\t Texp (s)\n'
	StrNomeImagens += '--------------------------------------------------------\n'
	directories = readArq_returnListDirectories()
	for Dir  in directories:
		chdir = cwd + '/' + Dir
		os.chdir(chdir)
		listaImgBias = readArq_returnListImages(tagBias)
		listaImgDark = readArq_returnListImages(tagDark)
		for img in listaImgBias:
			header = fits.getheader(img)
			StrNomeImagens += img + '\t\t' + str(header['temp']) + '\t\t\t' + str(header['exposure']) +'\n' 
	for Dir  in directories:
		chdir = cwd + '/' + Dir
		os.chdir(chdir)
		listaImgBias = readArq_returnListImages(tagBias)
		listaImgDark = readArq_returnListImages(tagDark)
		for img in listaImgDark:
			header = fits.getheader(img)
			StrNomeImagens += img + '\t\t' + str(header['temp']) + '\t\t\t' + str(header['exposure']) +'\n' 
	os.chdir(cwd)
	

	dados = Logdata + '\n\n'+ user + '\n'+ IP + '\n' + Strcommandline+'\n'+ WorkDirectory +'\n'+ Tempoprocess+'\n\n'+ Strbox + CCDstr+ '\n\n'+ DCnominal + '\n\n\n\n' + StrNomeImagens

	BackDir = os.path.normpath(os.getcwd() + os.sep + os.pardir)
	os.chdir(BackDir)
	try:
		logf = open('DCLog', 'w') 
	except:
		name.remove()
		logf = open('DCLog', 'w') 	
	logf.write(dados)
	logf.close()	
