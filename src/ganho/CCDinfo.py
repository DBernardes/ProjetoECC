#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    Criado em 18 de Outubro de 2016  
    Descricao: este modulo tem como entrada o cabecalho de uma imagen fits e a quantidade de imagens da serie obtidam retornado uma string com as principais informacoes do CCD.
    
    @author: Denis Varise Bernardes & Eder Martioli
    
    Laboratorio Nacional de Astrofisica, Brazil.    
	
    """

__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """
import matplotlib.pyplot as plt


def CCDinfo(header, nImagesFlat, nImagesBias):	
	date = header['date'].split('T')
	plt.xticks(())
	plt.yticks(())
	text =  'Camera: ' + header['head'] +'\n'																+			'Data do experimento: %s %s '  %(date[0], date[1]) +'\n'													+			'Quantidade de imagens: %i imagens de Flat e %i imagens de bias' %(nImagesFlat, nImagesBias) + '\n' 	+			'Modo de Leitura: %s' %(header['ACQMODE']) + '\n'												 	+			'Taxa  de  leitura: %.2f  MHz'%(1/(header['readtime']*1000000)) + '\n' 							+			'Pre-amplificacao: %i' %(header['preamp']) + '\n' 															+			'VShift Speed: %.3f e-6' %(header['vshift']*1000000)
	
	return text
	


