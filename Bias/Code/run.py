#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
    Criado em 16/10/2020
    @author: Denis Varise Bernardes & Eder Martioli
    
    Laboratorio Nacional de Astrofisica, Brazil.   
	
   
"""

__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """

import ReadNoiseCharact as RNC
import matplotlib.pyplot as plt

dir_path = r'C:\Users\denis\Desktop\ProjetoECC\Bias\Images'
RNobject = RNC.ReadNoiseCharact(dir_path)
plt.figure(figsize=(22,28))
RNobject.combinaImagensBias()
RNobject.CaractGradiente()
RNobject.CaractHistograma()
RNobject.CaractVariacaoTemporal()
RNobject.InfoCaixaTexto()
RNobject.salvaArquivosResultados()


