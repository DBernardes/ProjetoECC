#!/usr/bin/python
# -*- coding: UTF-8 -*-
#@author: Denis Varise Bernardes & Eder Martioli
#Laboratorio Nacional de Astrofisica, Brazil.
#19/10/2020

#Este código foi criado para executar a biblioteca de caracterização
#da corrente de escuro dos CCDs.

import DCCharact as DC

dir_path = r'C:\Users\denis\Desktop\ProjetoECC\Dark_Current'
DCobjeto = DC.DarkCurrent(ccd_gain = 3.36, dir_path = dir_path)
DCobjeto.caractTemporal()
DCobjeto.DiretorioMenorTemperatura()

listaImgDark = DCReadArq.returnListImages(options.dark)
fig = plt.figure(figsize=(15,17))
DCobjeto.CaractTemporal()
DCobjeto.CaractEspacial()
DCobjeto.LogFile()
plt.savefig('Relatório DC', format='png')

arqCaract = arquivoCaract()
arqCaract.criaArq(arqCaract)
