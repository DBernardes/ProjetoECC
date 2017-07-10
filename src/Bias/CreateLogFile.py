#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    Criado em 08 de Novembro de 2016  
    
    @author: Denis Varise Bernardes & Eder Martioli
	descricao: este modulo possui como entrada o nome do arquivo log e um dicionario com as informacoes que serao escritas neste arquivo. 
    
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

cwd = os.getcwd()
BackDir = os.path.normpath(os.getcwd() + os.sep + os.pardir)
# Gera arquivo log
def logfile(dic, listaImagens):		
	header      = dic['header'] 
	minute 	    = dic['minute']	
	second 	    = dic['second']	
	ruidoNominal = dic['ruidoNominal']
	TempoExp    =	header['KCT']*len(listaImagens) # tempo total do experimento
	nImages = len(listaImagens)
	
	nowInitial = datetime.datetime.now()
	commandline = sys.argv	
	Logdata = 'Caracterizacao do ruido de leitura, ' + nowInitial.strftime("%Y-%m-%d %H:%M")
	user = 'Usuario: %s' %(getpass.getuser())
	IP = 'IP local: %s' %(socket.gethostbyname(socket.gethostname()))
	Strcommandline = 'Linha de comando: '
	for arg in commandline:
		Strcommandline += arg + ' ' 	
	WorkDirectory = 'Diretorio atual: ' + os.getcwd()	

			
	TimeElapsed = (nowInitial.minute*60+nowInitial.second) - (minute*60+second) #hora final menos hora inicial 
	Tempoprocess = 'Tempo de processamento: %i min %i s' %(TimeElapsed/60,TimeElapsed%60)
	Ehoras, Eminutos, Esegundos = TempoExp/3600, (TempoExp%3600)/60, (TempoExp%3600)%60	
	TempoExperimento = 'Tempo do experimento: %i h %i m %i s' %(Ehoras, Eminutos, Esegundos)	
	StrCCD = CCDinfo(header, nImages)
	biasNominal = 'Ruido de Leitura: %s adu' %(ruidoNominal)

	StrNomeImagens =  '\t\tArquivo\t\t\t CDDTemp (ºC)\t Texp (s)\n'
	StrNomeImagens += '--------------------------------------------------------\n'
	for Nomeimg in listaImagens:
		header = fits.getheader(Nomeimg)
		StrNomeImagens += Nomeimg + '\t\t' + str(header['TEMP']) + '\t\t\t' + str(header['exposure']) +'\n' 



	dados = Logdata + '\n\n'+ user + '\n'+ IP + '\n' + Strcommandline+'\n'+ WorkDirectory +'\n\n'+ Tempoprocess+ '\n'+ TempoExperimento+ '\n\n' + StrCCD+ '\n\n'+ biasNominal + '\n\n\n\n' + StrNomeImagens
	
	os.chdir(BackDir)
	try:
		name = 'BiasLog'
		logf = open(name, 'w') 
	except:
		name.remove()
		logf = open(name, 'w')
	logf.write(dados)
	logf.close()		
