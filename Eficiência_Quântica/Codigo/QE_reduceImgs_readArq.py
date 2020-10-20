#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    Criado em 19 de Novembro de 2016  
    
    @author: Denis Varise Bernardes & Eder Martioli
    Descricao: esta biblioteca possui as seguintes funcoes:

        mkDir_saveCombinedImages: pela chamada da funcao LeArquivoReturnLista retorna a lista de todas as imagens adquiridas no ensaio;
        realiza a subtração entre cada par de imagens, salvando o resultado em um novo diretório 'Imagens_reduzidas' . Feito isso, a
        funcao cria uma lista com o nomes das novas imagens atraves da chamada da funcao criaArquivo_listaImagensCombinadas.

        readArqDetector: esta funcao recebe o nome do arquivo contendo os PAR2s do detector, retornando um vetor com os valores medidos.

        ImagemUnica_returnHeader: esta funcao recebe uma unica imagem da lista, retornando o header para a retirada de informacoes.

        LeArquivoReturnLista: esta funcao faz a leitura do arquivo listaImagens gerado pela funcao criaArq_listaImgInput, retornando
        uma lista com o nome das imagens.

        criaArquivo_listaImagensCombinadas: esta funcao cria um arquivo chamado listaImagensCombinadas contendo o nome das imagens
        combinadas geradas na funcao mkDir_saveCombinedImages.

        LeArqFluxoCamera: esta funcao faz a leitura do arquivo Fluxo camera.dat gerado pela funcao criaArqFluxoCamera, retornado dois
        vetores com os valores do fluxo e dos desvio padrao.

        LeArq_curvaCalibDetector: PAR2 o nome do arquivo da curva de calibracao do detector e o numero do conjunto de imagens, esta
        funcao retornara um vetor contendo os valores da curva caso a opcao seja fornecida; caso contrario, a funcao retorna um vetor
        contendo o valor 1. 


    Laboratorio Nacional de Astrofisica, Brazil.

    
    
   
    """

__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """

import astropy.io.fits as fits
import numpy as np
import os

from sys import exit
from math import sqrt
from geraArquivo import geraArquivo


def mkDir_saveCombinedImages(nImages, images_dir):
    print('Criando diretorio: Mediana das Imagens')
    #recebe uma lista de imagens de retorna um diretorio com as imagens combinadas
    lista = LeArquivoReturnLista('listaImagens', images_dir)    
    n, i = 0, 0 
    VetorImagens = []
    for i in range(len(lista)):
        if i%nImages == nImages-1: 
            imagem = fits.getdata(images_dir + '\\' + lista[i])
            VetorImagens.append(imagem)          
            os.chdir(chdir)
            geraArquivo(VetorImagens, n)
            os.chdir(cwd)
            VetorImagens = []           
            n+=1            
        else:
            imagem = fits.getdata(images_dir + '\\' + lista[i])
            VetorImagens.append(imagem)
    criaArquivo_listaImagensReduzidas()     
    return 



def mkDir_ImgPair(tagPAR2, tagPAR1, ganho, images_dir):
    print('Criando diretorio: Imagens reduzidas')
    if not os.path.exists(images_dir + '\\' + 'Imagens_reduzidas'): os.makedirs(images_dir + '\\' + 'Imagens_reduzidas')
    chdir = images_dir + '\\' + 'Imagens_reduzidas'    
    #recebe uma lista de imagens de retorna um diretorio com as imagens reduzidas de raios cosmicos e erro do shutter
    listaPAR2 = LeArquivoReturnLista(tagPAR2+'List.txt', images_dir)    
    listaPAR1 = LeArquivoReturnLista(tagPAR1+'List.txt', images_dir)

    VetorImagens = [[],[]]
    i,n, string, VetorStdSignal = 0, 0, '', []
    for i in range(len(listaPAR2)):     
        imagemPAR2 = fits.getdata(images_dir + '\\' + listaPAR2[i])[0].astype(float)
        imagemPAR1 = fits.getdata(images_dir + '\\' + listaPAR1[i])[0].astype(float)        
                    
        imgReducePAR = imagemPAR2 - imagemPAR1
        VetorStdSignal.append(sqrt(sum(sum(imagemPAR2 + imagemPAR1))*ganho))
        
        os.chdir(chdir)
        if n < 10: string = '00%i'%(n)
        if 10 <= n < 100: string = '0%i'%(n)
        if n >= 100: string = '%i'%(n) 
        print('ImagemReduzida%s.fits'%(string))
        fits.writeto('ImagemReduzida_%s.fits'%(string),imgReducePAR, overwrite=True)
        os.chdir(images_dir)
        VetorImagens = [[],[]]
        n+=1        
    criaArquivo_StdDiffImagens(VetorStdSignal, images_dir)
    criaArquivo_listaImagensReduzidas(images_dir)     
    return 


def readArqDetector(name, images_dir):
    valores=[]
    with open(images_dir + '\\' + name) as arq:
        Strvalores = arq.read().splitlines()
        for valor in Strvalores[1:]:
            valores.append(float(valor))
        arq.close()
        return valores



def ImagemUnica_returnHeader(tagPAR2, images_path):
    with open(images_path + '\\' + tagPAR2+'List.txt') as arq:
        imagem = arq.read().splitlines()[0].split(',')[0]
        arq.close()
    header = fits.getheader(images_path + '\\' + imagem)
    return header



def LeArquivoReturnLista(arquivo, images_path):    
    with open(images_path + '\\' + arquivo) as arq:
        lista = []
        linhas = arq.read().splitlines()
        for lin in linhas:
            for img in lin.split(','):
                lista.append(img)
        arq.close()
    return lista



def criaArquivo_listaImagensReduzidas(images_path):    
    nome = images_path + '\Imagens_reduzidas\listaImagensReduzidas'
    try: File = open(nome,'w')
    except: 
        nome.remove()
        File = open(nome,'w')   
    listaImagemCombinada = os.listdir(images_path + '\Imagens_reduzidas')
    listaImagemCombinada.sort()
    for img in listaImagemCombinada:
        if '.fits' in img:
            File.write(img+'\n')    
    File.close()    


def criaArquivo_StdDiffImagens(vetorStd, images_path):
    nome = images_path + '\\' + 'StdDiffImages'
    try: arq = open(nome,'w')
    except: 
        nome.remove()
        arq = open(nome,'w')
    arq.write('-Desvio padrao das imagens reduzidas:\n')
    for std in vetorStd:
        arq.write(' \t\t ' + str(std) + '\n')
    arq.close()




def LeArqFluxoCamera(images_path):
    vetorFluxoCamera, vetorSigmaBackground_Signal = [],[]
    with open(images_path + '\\' + 'Fluxo camera.dat') as arq:
        listaValores = arq.read().splitlines()
    for linha in listaValores[1:]:
        Fluxo_e_Sigma = linha.split('\t\t\t')
        vetorFluxoCamera.append(float(Fluxo_e_Sigma[0]))
        vetorSigmaBackground_Signal.append(float(Fluxo_e_Sigma[1]))

    return vetorFluxoCamera, vetorSigmaBackground_Signal




def LeArq_curvaCalibFiltroDensidade(nome, numeroImagens, images_path):
    VetorPAR2s=[]
    if nome != '':
        with open(images_path + '\\' + nome) as arq:
            linhas = arq.read().splitlines()
        arq.close()
        for PAR2 in linhas[1:]:
            if PAR2 == '':continue
            VetorPAR2s.append(float(PAR2))
    else:
        for i in range(numeroImagens):
            VetorPAR2s.append(1)    
    return VetorPAR2s


def LeArq_curvaEQFabricante(name, images_path):
    espectro, vetorEQ = [], []
    with open(images_path + '\\' + name) as arq:
        linhas = arq.read().splitlines()
        arq.close()    
    for linha in linhas:
        if linha == '':continue
        valores = linha.split('\t')
        espectro.append(float(valores[0]))
        vetorEQ.append(float(valores[1]))
    return vetorEQ, espectro

        
