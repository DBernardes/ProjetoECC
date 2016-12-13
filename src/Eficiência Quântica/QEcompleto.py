#!/usr/bin/python
# coding=<UTF-42>

"""
    Criado em 29 de Setembro de 2016  
    Descricao: 
    @author: Denis Varise Bernardes & Eder Martioli
    
    Laboratorio Nacional de Astrofisica, Brazil.
    
  
    """

__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """

import os, sys
import astropy.io.fits as fits
import matplotlib.pyplot as plt
import numpy as np

from optparse import OptionParser

from dados import dados
from scipy.interpolate import interp1d, splrep, splev
from scipy.integrate import quad


parser = OptionParser()
parser.add_option("-i", "--list", dest="list", help="imagens FITS",type='string',default="")
parser.add_option("-v", action="store_true", dest="verbose", help="verbose",default=False)
parser.add_option("-r",'--range',dest="Range",type = 'string', help='Intervalo do Espectro', default ='')

try:
    options,args = parser.parse_args(sys.argv[1:])
except:
    print "Error: check usage with ./QEcompleto.py -h ";sys.exit(1);

if options.verbose:
    print 'Lista de imagens: ', options.list
	

#retorna valor maximo da curva de EQ
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


#retorna os valores de espectro para um intervalo de EQ
def returnInterval(x,f):
	if options.Range:
		vetor = tuple(options.Range.split(','))
		vetor = [int(vetor[0]),int(vetor[1])]
		print 'Espectro (nm)\t'+'EQ (%)'
		for data in x:	
			if vetor[0] < f(data) < vetor[1]:
				print ' ',round(data,2),'\t', round(f(data),2)



#------------------------------------------------------------------------------------------
dados, espectro = dados()
f = interp1d(espectro, dados, kind='cubic')
x = np.linspace(espectro[0], espectro[-1], 100)

fmax, i= returnMax(f(x))
integral = quad(f, x[0],x[-1])
absPorcent = integral[0]/(x[-1] - x[0])
returnInterval(x,f)
fmax = round(fmax,1)


font = 15
plt.plot(espectro, dados, c='blue')
plt.plot(espectro, dados, 'o', c='blue')
plt.xlabel(r'$\mathtt{Comprimento \quad de \quad onda \; (nm)}$', size=font)
plt.ylabel(r'$\mathtt{EQ \quad (}$' + '%' + r'$\mathtt{)}$', size=font)
plt.title(r'$\mathtt{Curva \quad de \quad Efici\^encia \quad Qu\^antica}$', size=font)

plt.annotate(r'$\mathtt{EQ_{max} \; = \; %.1f}$' %(fmax) + ' %', xy=(0.6,0.90), xycoords='axes fraction',  ha='left', va='center', size=font)
plt.annotate(r'$\mathtt{Comp. \; onda \; = \; %.2f \; (nm)}$' %(x[i]), xy=(0.6,0.85), xycoords='axes fraction',  ha='left', va='center', size=font)
plt.annotate(r'$\mathtt{Convers\~ao \; = \; %.2f}$' %(absPorcent) + ' %', xy=(0.6, 0.80), xycoords='axes fraction',  ha='left', va='center', size=font)

plt.savefig('Eficiencia Quantica', format='jpg')

