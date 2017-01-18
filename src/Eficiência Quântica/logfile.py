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


# Gera arquivo log
def logfile(name, dic):	
	
	lenDados  = dic['qtdImagens']
	minute 	  = dic['minute']	
	second 	  = dic['second']
	header 	  = dic['header']
	espectro  = dic['espectro']
	

	try:
		logf = open(name, 'w') 
	except:
		name.remove()
		logf = open(name, 'w')

	now = datetime.datetime.now()	
	commandline = sys.argv	
	
	Strcommandline = 'Linha de comando: '
	for arg in commandline:
		Strcommandline += arg + ' ' 	
	nowInitial = datetime.datetime.now()	
	TimeElapsed = (nowInitial.minute - minute)*60 + nowInitial.second - second #hora final menos hora inicial 	
	StrCCD = CCDinfo(header, lenDados)	

	StrEspectro = 'Espectro do experimento: %i nm a %i nm com passo %i nm'%(espectro[0], espectro[1], espectro[2])
	Logdata = 'Caracterizacao da Eficiencia Quantica, ' + now.strftime("%Y-%m-%d %H:%M")
	user = 'Usuario: %s' %(getpass.getuser())
	IP = 'IP local: %s' %(socket.gethostbyname(socket.gethostname()))
	WorkDirectory = 'Diretorio atual: ' + os.getcwd()	
	Tempoprocess = 'Tempo de processamento: %i min %i s' %(TimeElapsed/60,TimeElapsed%60)


	dados = Logdata + '\n\n'+ user + '\n'+ IP + '\n' + Strcommandline+'\n'+ WorkDirectory +'\n'+ Tempoprocess+ '\n\n'+ StrEspectro + '\n\n' + StrCCD+ '\n\n'
	logf.write(dados)
	logf.close()	
