#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    Criado em 10 de Agosto de 2016  
    Descricao: este modulo tem como entrada uma serie de dados, retornando a quantidade de pontos para um intervalo entre a media mais/menos o desvio padrao.
    
    Laboratorio Nacional de Astrofisica, Brazil.    
"""
__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """


import numpy as np

#retorna porcentagem de pixels dentro de um intervalo
def porcentPixel(dados):
	mean = np.mean(dados)
	std = np.std(dados)
	contador = 0

	for d in dados:
		if mean - std < d < mean + std:
			contador+=1
	contador = contador/float(len(dados))*100
	return contador


