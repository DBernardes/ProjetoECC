#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    Criado em 20 de Setembro de 2016  
    Descricao: este modulo possui com entrada a serie de imagens obtida pela camera, tendo como retorno uma imagem .gif onde e possivel ver a variacao pixel a pixel ao redor da media em funcao do tempo.
    @author: Denis Varise Bernardes & Eder Martioli
    
    Laboratorio Nacional de Astrofisica, Brazil.
    
   
    """

__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """


import os, sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def plotGif(dados):
	meanDados = np.mean(dados[0])
	lenDados = len(dados)	
	fig = plt.figure()
	ims = []
	i=0
	while i < (lenDados):		
		im = plt.imshow(dados[i] - meanDados,cmap='seismic',vmin=-6, vmax=45,origin='lower', animated= True)
		plt.title(r'$\mathtt{Imagens \;\; em \;\; fun}$'+u'ç'+r'$\mathtt{\~ao \;\; do \;\; tempo }$')
		plt.xlabel(r'$\mathtt{Eixo \;\; x}$')
		plt.ylabel(r'$\mathtt{Eixo \;\; y}$')		
		ims.append([im])
		i+=1
	plt.colorbar()	
	
	ani = animation.ArtistAnimation(fig, ims, interval=150, blit=True, repeat_delay=2000)	
	ani.save('animation.gif', writer='imagemagick', fps=10)
#	plt.show()
	plt.close()


