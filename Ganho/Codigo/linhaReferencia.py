#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    Criado em 10 de Agosto de 2016  
    Descricao: este modulo tem como entrada dois vetores, sendo estes os eixos (x,y) de um grafico, retornando um novo grafico com uma linha no valor medio dos dados e duas outros linhas para o valor da media mais/menos o desvio padrao.
    @author: Denis Varise Bernardes & Eder Martioli
    
    Laboratorio Nacional de Astrofisica, Brazil.    
"""
__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """

import numpy as np
import matplotlib.pyplot as plt

#linha referencia
def linhaReferencia(x,y):
	lenY = len(y)
	mean = np.mean(y)
	std = np.std(y)
	linhaR = []
	lisStd = []
	i=0
	while i < lenY:
		linhaR.append(mean)		
		i+=1
	
	plt.plot(x,linhaR, '-', c='red', linewidth=1.5)
	plt.plot(x,linhaR - std, '--', c='red', linewidth=1.5)
	plt.plot(x,linhaR + std, '--', c='red', linewidth=1.5)
