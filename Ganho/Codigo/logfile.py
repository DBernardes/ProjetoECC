#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    Criado em 08 de Novembro de 2016  
    
    @author: Denis Varise Bernardes & Eder Martioli
	descricao: este modulo possui como entrada o nome do arquivo log e um dicionario com algumas informacoes que serao escritas nesse arquivo. 
    
    Laboratorio Nacional de Astrofisica, Brazil.
   
    """

__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """

import os, sys
import datetime
import getpass
import socket

from CCDinfo import CCDinfo
from astropy.io import fits


# Gera arquivo log
def logfile(dic, listaFlat, listaBias):	
	nImagesFlat   = dic['nImagesFlat']
	nImagesBias   = dic['nImagesBias']
	parametrosBox = dic['box']
	minute = dic['minute']	
	second = dic['second']
	ganho  = dic['ganho']
	header 	  = fits.getheader(listaFlat[0])

	now = datetime.datetime.now()	
	commandline = sys.argv	

	Logdata = 'Caracterizacao do ganho, ' + now.strftime("%Y-%m-%d %H:%M")
	user = 'Usuario: %s' %(getpass.getuser())
	IP = 'IP local: %s' %(socket.gethostbyname(socket.gethostname()))
	Strcommandline = 'Linha de comando: '
	for arg in commandline:
		Strcommandline += arg + ' ' 	
	WorkDirectory = 'Diretorio atual: ' + os.getcwd()	
	nowInitial = datetime.datetime.now()
	TimeElapsed = (nowInitial.minute - minute)*60 + nowInitial.second - second #hora final menos hora inicial 	
	Tempoprocess = 'Tempo de processamento: %i min %i s' %(TimeElapsed/60,TimeElapsed%60)
	
	Strbox = 'Parametros da caixa de pixels: coordenadas (%i,%i) e dimensao %i'%(parametrosBox[0],parametrosBox[1],parametrosBox[2]*2)
	StrCCD = CCDinfo(header, nImagesFlat, nImagesBias)
	Strganho = 'Ganho: %.2f +/- %.2f e-/ADU'%(ganho[0], ganho[1])

	StrNomeImagens =  '\t\tArquivo\t\t\t CDDTemp (ºC)\t Texp (s)\n'
	StrNomeImagens += '--------------------------------------------------------\n'
	for Nomeimg in listaFlat:
		header = fits.getheader(Nomeimg)
		StrNomeImagens += Nomeimg + '\t\t' + str(header['temp']) + '\t\t\t' + str(header['exposure']) +'\n' 
	for Nomeimg in listaBias:
		header = fits.getheader(Nomeimg)
		StrNomeImagens += Nomeimg + '\t\t' + str(header['temp']) + '\t\t\t' + str(header['exposure']) +'\n' 

	dados = Logdata + '\n\n'+ user + '\n'+ IP + '\n' + Strcommandline+'\n'+ WorkDirectory +'\n'+ Tempoprocess+'\n\n'+ Strbox + '\n\n' + StrCCD+ '\n\n'+ Strganho + '\n\n\n\n' + StrNomeImagens

	BackDir = os.path.normpath(os.getcwd() + os.sep + os.pardir)
	os.chdir(BackDir)
	try: logf = open('GanhoLog', 'w') 
	except:
		name.remove()
		logf = open('GanhoLog', 'w')
	logf.write(dados)
	logf.close()	
