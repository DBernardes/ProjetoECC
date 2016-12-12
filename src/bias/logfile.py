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


# Gera arquivo log
def logfile(name, dic):	
	
	lenDados  = dic['lenDados']
	minute 	  = dic['minute']	
	second 	  = dic['second']
	header 	  = dic['header']
	biasNominal = dic['biasNominal']
	TE     = dic['tempoExperimento']	
	
	nowInitial = datetime.datetime.now()
	commandline = sys.argv	
	Logdata = 'Caracterizacao do bias, ' + nowInitial.strftime("%Y-%m-%d %H:%M")
	user = 'Usuario: %s' %(getpass.getuser())
	IP = 'IP local: %s' %(socket.gethostbyname(socket.gethostname()))
	Strcommandline = 'Linha de comando: '
	for arg in commandline:
		Strcommandline += arg + ' ' 	
	WorkDirectory = 'Diretorio atual: ' + os.getcwd()	

			
	TimeElapsed = (nowInitial.minute*60+nowInitial.second) - minute*60+second #hora final menos hora inicial 
	Tempoprocess = 'Tempo de processamento: %i min %i s' %(TimeElapsed/60,TimeElapsed%60)
	Ehoras, Eminutos, Esegundos = TE/3600, (TE%3600)/60, (TE%3600)%60	
	TempoExperimento = 'Tempo do experimento: %i h %i m %i s' %(Ehoras, Eminutos, Esegundos)	
	StrCCD = CCDinfo(header, lenDados)
	biasNominal = 'Ruido de Leitura nominal: %.2f adu' %(biasNominal)


	dados = Logdata + '\n\n'+ user + '\n'+ IP + '\n' + Strcommandline+'\n'+ WorkDirectory +'\n\n'+ Tempoprocess+ '\n'+ TempoExperimento+ '\n\n' + StrCCD+ '\n\n'+ biasNominal

	try:
		logf = open(name, 'w') 
	except:
		name.remove()
		logf = open(name, 'w')
	logf.write(dados)
	logf.close()	
