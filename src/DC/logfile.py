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

def logfile(name, nowInitial, minute, second, Dict, DKnominal, box=False):
	try:
		logf = open(name, 'w') 
	except:
		name.remove()
		logf = open(name, 'w') 	
	
	now = datetime.datetime.now()
	lenDados = len(Dict['cuboImagens'])
	commandline = sys.argv		

	Logdata = 'Caracterizacao da Corrente de escuro, ' + now.strftime("%Y-%m-%d %H:%M")
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

	if box:
		Strbox = 'Opcao caixa de pixels: (x,y) = (%i,%i), dimensao = %i.' %(Dict['Boxparameter'][0],Dict['Boxparameter'][1],Dict['Boxparameter'][2]*2) + '\n\n'
	else:
		Strbox = ''

	CCDstr = CCDinfo(Dict['header'], Dict['qtdImagens'], Dict['vetorTemp'] )
	DKnominal = 'Corrente de escuro nominal: %s e-/pix/s' %(DKnominal)

	dados = Logdata + '\n\n'+ user + '\n'+ IP + '\n' + Strcommandline+'\n'+ WorkDirectory +'\n'+ Tempoprocess+'\n\n'+ Strbox + CCDstr+ '\n\n'+ DKnominal

	logf.write(dados)
	logf.close()	
