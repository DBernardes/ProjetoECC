#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    Criado em 20 de Outubro de 2016.
    
    Descricão: este modulo possui como entrada uma string, o numero de linhas e colunas (n,m) do canvas, a posicao (posx,posy) em que a caixa irá ser posicionada, retornando um texto editado para as informacoes fornecidas. 
    
    @author: Denis Varise Bernardes & Eder Martioli
    
    Laboratorio Nacional de Astrofisica, Brazil.    

    """

__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """

import matplotlib.pyplot as plt

#caixa de texto com informacoes do grafico
def caixaTexto(Str, n, m, posx, posy,font, space=0.1,rspan=1, cspan=1):		
	i=0
	ax = plt.subplot2grid((n,m),(posx,posy), rowspan=rspan, colspan=cspan)
	plt.xticks(())
	plt.yticks(())
	while i < len(Str):
		plt.text(0.05, 0.90-space*i, Str[i], ha='left', va='center', size=font)
		i+=1

