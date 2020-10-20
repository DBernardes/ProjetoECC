#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    Criado em 22 de Março de 2017  
    Descricao: 
    
    @author: Denis Varise Bernardes & Eder Martioli
    
    Laboratorio Nacional de Astrofisica, Brazil.

    
	example: ./biasCompleto.py --list=list
   
    """

__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """

import os, sys
import datetime

date = 'Data: ' + str(datetime.datetime.now()).split('.')[0].split(' ')[0]

class arquivoCaract:
	def __init__(self):
		self.dic = {'StrEspectroEQ':[], 'TemperaturaDC':'', 'nomeCamera':'', 'DCCalculado':'', 'ganhoCalculado':'', 'RNCalculado':''}

		
	def testArqExists(self):
		self.ListaArquivos = ['BiasLog', 'DCLog', 'GanhoLog', 'EQLog']
		for arq in self.ListaArquivos:
			if os.path.isfile(os.getcwd()+'/'+arq) is not True:
				exit()


	def getValues(self, Object):
		intervEQ=False	
		StrEspectroEQ = []
		Object.testArqExists()	

		RNCalculado, DCCalculado, TemperaturaDC, ganhoCalculado, taxaLeitura, preAmp, Vshift, StrEspectroEQ, Data = '','','','','','','',[],''
		for arq in self.ListaArquivos:
			with open(arq) as arq:
				linhas = arq.read().splitlines()
				ArqDC = False
				for linha in linhas:								
					if 'Ruido de Leitura:' in linha: 
						RNCalculado = linha.split(':')[1]
					if 'Corrente de escuro:' in linha: 
						DCCalculado = linha.split(':')[1]
						ArqDC = True				
					if  ArqDC == True:
						try:						
							if float(linha.split('\t\t')[1]) < TemperaturaDC:
								TemperaturaDC = linha.split('\t\t')[1]
						except: 1											
					if 'Ganho:' in linha: 						
						ganhoCalculado = linha.split(':')[1]
					if ' Lambda (nm) 	 EQ (%)' in linha: intervEQ=True
					if linha == '': intervEQ = False
					if intervEQ == True:
						StrEspectroEQ.append(linha)
					if 'Camera:' in linha:
						nomeCamera = linha.split(':')[1]
					if 'Taxa  de  leitura:' in linha:
						taxaLeitura = linha.split(':')[1]
					if 'VShift Speed:' in linha:
						Vshift = linha.split(':')[1]
					if 'Pre-amplificacao:' in linha:
						preAmp = linha.split(':')[1]
					if 'Data do experimento:' in linha:
						Data = linha.split(':')[1]
					if 'Tabela para pagina wiki' in linha:
						break
 

				
				arq.close()
		listValues = [RNCalculado, DCCalculado,TemperaturaDC, ganhoCalculado, StrEspectroEQ, nomeCamera, taxaLeitura, preAmp, Vshift, Data]					
		return listValues
			
		


	def criaArq(self, Object):	
			
		Object.getValuesArqCaract()
		listValues = Object.getValues(Object)	
		Object.atualizaVariavel(listValues)		
		listaEQ = self.dic['StrEspectroEQ'][2:]
		StrEQ = ''
		for linha in listaEQ:
			StrEQ += '|' + linha.split('\t\t')[0][1:] + '||' + linha.split('\t\t')[1] + '\n' + '|-' + '\n'

		StrNomeCamera = 'Camera:%s' %(self.dic['nomeCamera']) 
		StrTaxaLeitura = 'Taxa  de  leitura:%s' %(self.dic['taxaLeitura'])
		StrPreAmp = 'Pre-amplificacao:%s' %(self.dic['preAmp'])
		StrVShift = 'VShift Speed:%s' %(self.dic['Vshift'])
		StrTemp = 'Temperatura minima:%s ºC' %(self.dic['TemperaturaDC'])
		StrBias = 'Ruido de Leitura:%s' %(self.dic['RNCalculado'])
		StrDC = 'Corrente de escuro:%s' %(self.dic['DCCalculado'])
		StrGanho = 'Ganho:%s' %(self.dic['ganhoCalculado'])
		StrTabelaWiki = ['\n\n\n', 'Tabela para pagina wiki', '------------------------','\n',
'{| class="wikitable floatleft" style="text-align: center;"',  
'! style="background: #808080;"| Câmera: || style="background: #808080;" | %s'%(self.dic['nomeCamera']),
'|-', 
'| Taxa de Leitura: || %s'%(self.dic['taxaLeitura']),
'|-', 	
'| Pré-amplificação: || %s'%(self.dic['preAmp']),
'|-',
'| VShift Speed: || %s'%(self.dic['Vshift']),
'|-',
'| Data: || %s'%(self.dic['Data']), 
'|-',
'| Temperatura minima: || %s ºC'%(self.dic['TemperaturaDC']),
'|-',
'| Ruido de Leitura: || %s'%(self.dic['RNCalculado']),
'|-',
'| Corrente de escuro: || %s'%(self.dic['DCCalculado']),
'|-',
'| Ganho: || %s'%(self.dic['ganhoCalculado']),
'|-',
'!  style="background: #808080;"| Lambda (nm) ||  style="background: #808080;"| EQ (%)',
'|-',
StrEQ+'|}']





		StrArqTexto = [StrNomeCamera, StrTaxaLeitura, StrPreAmp, StrVShift, date, StrTemp, StrBias, StrDC, StrGanho] + [''] + self.dic['StrEspectroEQ']
		arqCaract = open('arquivoCaracterizacao', 'w')
		for Str in StrArqTexto:
			arqCaract.write(Str+'\n')
		for Str in StrTabelaWiki:
			arqCaract.write(Str+'\n')
		arqCaract.close()
		
		
	def getValuesArqCaract(self):
		intervEQ=False
		try:
			with open('arquivoCaracterizacao') as arq:
				linhas = arq.read().splitlines()
				arq.close()		
			for linha in linhas:					
				if 'Ruido de Leitura' in linha: 					
					self.dic['RNCalculado'] = linha.split(':')[1]
				if 'Corrente de escuro' in linha: 
					self.dic['DCCalculado'] = linha.split(':')[1]
				if 'Ganho' in linha: 
					self.dic['ganhoCalculado'] = linha.split(':')[1]
				if ' Lambda (nm) 	 EQ (%)' in linha: intervEQ=True				
				if intervEQ == True:
					self.dic['StrEspectroEQ'].append(linha)
				if 'Temperatura minima' in linha:
					self.dic['TemperaturaDC'] = linha.split(':')[1].split(' ')[0]
				if 'Camera' in linha:
					self.dic['nomeCamera'] = linha.split(':')[1]
				if 'Tabela para pagina wiki' in linha:
					break
		except: 1
		

	def atualizaVariavel(self, lista):		
		i=0
		listaVariaveis = ['RNCalculado', 'DCCalculado', 'TemperaturaDC', 'ganhoCalculado', 'StrEspectroEQ', 'nomeCamera', 'taxaLeitura', 'preAmp', 'Vshift', 'Data']
		for dado in lista:
			if dado != '':
				self.dic[listaVariaveis[i]] = dado		
			i+=1
		
		
			
