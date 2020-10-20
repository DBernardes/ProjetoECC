#!/usr/bin/python
# -*- coding: UTF-8 -*-
#@author: Denis Varise Bernardes & Eder Martioli
#Laboratorio Nacional de Astrofisica, Brazil.
#19/10/2020

#Este código foi criado para executar a biblioteca de caracterização
#da corrente de escuro dos CCDs.

import DCCharact as DC
import DCReadArq
import matplotlib.pyplot as plt
import os

dir_path = r'C:\Users\observer\Desktop\Imagens_ECC\DC'
DCobjeto = DC.DarkCurrent(ccd_gain = 3.36, dir_path = dir_path)
DCobjeto.caractTemporal()
DCobjeto.DiretorioMenorTemperatura()

listaImgDark = DCReadArq.returnListImages(keyword = 'DC')
fig = plt.figure(figsize=(15,17))
DCobjeto.CaractTemporal()
DCobjeto.CaractEspacial()
plt.savefig('Relatório DC.pdf', format='pdf')
