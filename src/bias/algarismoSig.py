#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    Criado em 15 de Novembro de 2016  
    Descricao: este modulo possui como entrada uma variavel float, retornando o numero da casa decimal do algarismo mais significativo. Deve aparecer em conjunto com a funcao do python round() para, assim, arredondar o numero com a casa decimal adequada. 
    
    @author: Denis Varise Bernardes & Eder Martioli
    
    Laboratorio Nacional de Astrofisica, Brazil.

    
	example: ./biasCompleto.py --list=list
   
    """

__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """


def algarismoSig(num):
	if 0< num < 1:
		dec = '%1.0e'%(num)
		dec = dec.split('-')
		dec = int(dec[1])
	
	if num > 1:
		dec = 1
    	
	return dec


