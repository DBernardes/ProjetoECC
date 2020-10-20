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
from sys import exit

def caixaPixels(imagem, parametros):
    #retira apenas uma caixa de pixels, dada as coordenadas (x,y) e seu tamanho    
    xcoord = parametros[0]
    ycoord = parametros[1]
    dimension = int(parametros[2]/2)
    d = dimension   
    newimage = imagem[xcoord-d:xcoord+d, ycoord-d:ycoord+d] 
    return newimage



