#!/usr/bin/python
# coding=UTF-8

"""
    Criado em 20 de Outubro de 2016.
    
    Descricão: este modulo possui como entrada uma imagem e uma string no formato (x,y,L = posx,posy,dimensao), retornando uma lista de arrays dos pixels das imagens retirados de dentro das dimensoes e coordendas da caixa fornecidas pela string.
    @author: Denis Varise Bernardes & Eder Martioli
    
    Laboratorio Nacional de Astrofisica, Brazil.    
 
    """

__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """
import numpy as np

def caixaPixels(imagem, string):
	#retira apenas uma caixa de pixels, dada as coordenadas (x,y) e seu tamanho			
	parametros = tuple(string.split(','))
	xcoord = int(parametros[0])
	ycoord = int(parametros[1])
	dimension = int(parametros[2])/2
	working_mask = np.ones(imagem.shape,bool)
	ym, xm = np.indices(imagem.shape, dtype='float16') 
	mask = (ycoord-dimension<ym)*(ym<ycoord+dimension)*(xcoord-dimension<xm)*(xm<xcoord+dimension)*working_mask 
	pixels = imagem[np.where(mask)]	
	return pixels, xcoord, ycoord, dimension
