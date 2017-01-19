#!/usr/bin/python
# coding=UTF-8

"""
    Criado em 20 de Setembro de 2016.
    
    Descricão: esta biblioteca possui as seguintes funcoes:

		CombinaImgs_salvaArquivoFITS: esta funcao tem como input uma serie imagens obtidas pelo CCD, retornando uma imagem combinada dessa serie. Sobre os dados e realizada uma mediana para cada pixel em funcao do tempo, salvando a imagem resultante com o nome ImgReduce.

		criaImgBias_Reduction: esta funcao faz a leitura de uma lista de imagens bias fornecida, retornando essa serie para a funcao CombinaImgs_salvaArquivoFITS.

		criaArq_DadosTemporais: esta funcao recebe uma lista de imagens de dark; sobre essas imagens faz a reducao do bias utilizando da imagem combinada, retira uma caixa de pixels e, sobre ela, calcula sua mediana e desvio padrao, realizando para cada uma a leitura do valor do tempo de exposicao. Sobre o tempo de exposicao e a mediana das imagens, calcula uma funcao linear; gera um arquivo chamado Arquivo_DadosTemporais  expressando um cabecalho contendo o coeficiente angular e linear da curva e desvio padrao do ajuste; e tambem escrito o valor da mediana e desvio padrao das imagens em forma de colunas. A funcao gera ainda um segundo arquivo contendo uma lista do tempo de exposicao das imagens.

    @author: Denis Varise Bernardes & Eder Martioli
    
    Laboratorio Nacional de Astrofisica, Brazil.    
 
    """

__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """

import numpy as np
import astropy.io.fits as fits

from ccdproc import Combiner, CCDData
from caixaPixels import caixaPixels
from scipy import stats


def CombinaImgs_salvaArquivoFITS(inputlist, Reduce=False, num=50):
	#vetor com os dados
	scidata = []
	if Reduce == True:
		Imin = len(inputlist)
		scidata = inputlist

	else:
		Imin=-num
		for img in inputlist[Imin:]:
			scidata.append(img)
	
	#gera um outro vetor na classe CCDData
	x = []
	i = 0	
	while i < np.abs(Imin):
		x.append(CCDData(scidata[i], unit = 'adu'))
		i+=1
	
	combinedImage = Combiner(x)
	combinedImageMedian = combinedImage.average_combine() #average_median
	NPcombinedImage = np.asarray(combinedImageMedian)

	try: fits.writeto('ImgReduce.fits',NPcombinedImage, clobber=True)	
	except: print 'Erro ao salvar o arquivo.' 




def criaImgBias_Reduction(listaImgBias):
	imgReduce = 0
	bias = []	
	for img in listaImgBias:
		bias.append(fits.getdata(img))		
	CombinaImgs_salvaArquivoFITS(bias, Reduce=True)





def criaArq_DadosTemporais(listaImgDark,parametros):
	Imgmedian,ImgStd, VetorEtime = [], [],[]
	for img in listaImgDark:		
		scidata,hdr = fits.getdata(img,header=True)
		imgReduce = fits.getdata('ImgReduce.fits')
		scidata = scidata.astype(float) - imgReduce
		scidata = scidata[0]
		scidata = caixaPixels(scidata, parametros) #retira apenas uma caixa de pixels da imagem total
		Imgmedian.append(np.median(scidata))
		ImgStd.append(np.std(scidata))
		VetorEtime.append(hdr['exposure'])
	#ajuste da curva
	coefAjust, intercept, r, p, stdLinAjust = stats.linregress(VetorEtime,Imgmedian) 
	
	name = 'Arquivo_DadosTemporais'	
	try: arq = open(name,'w')
	except: 
		name.remove()
		arq = open(name,'w')	
	arq.write('coefAjust = %.7f\nintercept = %.7f\nstdLinAjust = %.1e\n'%(coefAjust,intercept,stdLinAjust))
	arq.write('Mediana (adu)        Std (adu)\n')
	i=0
	for dado in Imgmedian:
		s = '   %.7f \t\t %.7f\n' %(dado, ImgStd[i])
		arq.write(s)
		i+=1
	arq.close()


	#arquivo separado Etime
	name = 'Arquivo_Etime'	
	try: arq = open(name,'w')
	except: 
		name.remove()
		arq = open(name,'w')	
	arq.write('Etime (s)\n')
	i=0
	for dado in VetorEtime:
		s = '  %.2f\n'%(dado)
		arq.write(s)
		i+=1
	arq.close()





	
