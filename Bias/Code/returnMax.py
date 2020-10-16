#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    Criado em 10 de Agosto de 2016  
    Descricao: este modulo tem como entrada uma serie de dados, retornando o valor maximo dessa serie.
    
    Laboratorio Nacional de Astrofisica, Brazil.    
"""
__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """


def returnMax(dados):
	i=0
	fvetor = dados
	while i < len(fvetor)-1:
		if fvetor[i] > fvetor[i+1]:
			vartemp = fvetor[i+1]
			fvetor[i+1] = fvetor[i]
			fvetor[i] = vartemp
		else:
			index = i+1
		i+=1
	return fvetor[-1], index
