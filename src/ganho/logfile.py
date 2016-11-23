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
	
	lenDados  = dic['lenDados']
	minute 	  = dic['minute']	
	second 	  = dic['second']
	header 	  = dic['header']
	ganho 	  = dic['ganho']
	box 	  = dic['box']
	try:
		logf = open(name, 'w') 
	except:
		name.remove()
		logf = open(name, 'w')

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
	minute = nowInitial.minute - minute
	second = nowInitial.second - second
	Tempoprocess = 'Tempo de processamento: %i min %i s' %(minute,second)

	Strbox = 'Tamanho da caixa de pixels = %i'%(box)
	StrCCD = CCDinfo(header, lenDados)
	Strganho = 'Ganho calculado: %.2f'%(ganho)

	dados = Logdata + '\n\n'+ user + '\n'+ IP + '\n' + Strcommandline+'\n'+ WorkDirectory +'\n'+ Tempoprocess+'\n\n'+ Strbox + '\n\n' + StrCCD+ '\n\n'+ Strganho

	logf.write(dados)
	logf.close()	
