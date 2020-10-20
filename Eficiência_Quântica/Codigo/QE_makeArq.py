#!/usr/bin/python
# coding=<UTF-42>

"""
    Criado em 29 de Setembro de 2016  
    Descricao: Esta biblioteca possui as seguintes funcoes:

    criaArq_listaImgInput: para as imagens situadas no diretorio atual, esta funcao cria uma lista com os nomes dos conjuntos
    de imagens que possuam a incidencia de luz de mesmo comprimento de onda.

    criaArq_infoEnsaio: esta funcao cria um arquivo para ser preechido contendo as informacoes necessarias do ensaio.
    @author: Denis Varise Bernardes & Eder Martioli
    
    Laboratorio Nacional de Astrofisica, Brazil.
    
  
    """

__version__ = "1.0"

__copyright__ = """
    Copyright (c) ...  All rights reserved.
    """

import os
from sys import exit




def criaArq_listaImgInput(cwd):
    s,i='',0    
    listaImagens = os.listdir(cwd)
    listaImagensFiltrada = []
    for img in listaImagens:
        if '.fits' in img:
            listaImagensFiltrada.append(img)
    listaImagensFiltrada.sort()

    for img in listaImagensFiltrada:
        s += str(img)+'\n'

    arq = cwd + '\\' + listaImagens
    try:
        logf = open('listaImagens', 'w') 
    except:
        name.remove()
        logf = open('listaImagens', 'w')
    logf.write(s)
    logf.close()



def criaArq_listaImgMedidas(tag, cwd):
    s, i='',0
    listaImagens = os.listdir(cwd)
    listaImagensFiltrada = []
    for img in listaImagens:
        if '.fits' in img and tag in img:
            listaImagensFiltrada.append(img)
    listaImagensFiltrada.sort()
    
    
    for img in listaImagensFiltrada:
        s += str(img)+'\n'
        
    name = cwd + '\\' + tag+'List.txt'
    try:
        logf = open(name, 'w') 
    except:
        name.remove()
        logf = open(name, 'w')
    logf.write(s)       
    logf.close()



    

def criaArq_infoEnsaio(images_path):

    Str = ['Arquivo com as informacoes necessarias para caracterizacao da eficiencia quantica do CCD.\n', '->', 'Espectro (nm) (Einicial, Efinal, passo) =','nome arquivo calibracao filtro densidade =', 'nome arquivo QE do fabricante =', 'nome arquivo detector =', 'nome arquivo Log =','tag do nome das imagens (PAR2,PAR1) =','ganho eletronico =','Tamanho do pixel (um)=13.5', 'Dimensao do fotometro (mm) = 11.0','<-']

    nota = ['\nNota: neste arquivo estao as principais informacoes referentes ao ensaio de caracterizacao da eficiencia quantica. Nele devem constar as seguintes informacoes:\n', '- Espectro (nm): espectro utilizado no ensaio (em nanometros); nele devem constar o comprimento de onda inicial, comprimento de onda final e o passo utilizado, respectivamente;', '- Nome do arquivo contendo a curva de calibracao do filtro de densidade (opcional); nele devem constar os valores da curva de transmissao do filtro de densidade utilizado no ensaio. Caso esta opcao nao seja fornecida, o programa ira plotar a curva de EQ sem levar em consideracao a correcao do filtro;' , '- Nome do arquivo contendo a curva de Eficiencia Quantica do fabricante (opcional);nele devem constar o par coordenado do comprimento de onda (em nm) pela eficiencia quantica do fabricante; Caso esse opcao nao seja fornecida, o codigo ira plotar apenas a curva de EQ obtida pelo ensaio de caracterizacao;','- Nome do arquivo contendo os dados detector;este arquivo precisa conter apenas o valores medidos pelo detector (sem o comprimento de onda utilizado);', '- Nome arquivo Log (opcional);','- uma tag (nome ou parte do nome) das imagens, separados por virgulas, obtidas como dados e das imagens obtidas como referencia para que o programa possa separar cada serie de imagens em uma lista diferente;', '- Ganho do CCD;','- Tamanho do pixel (em micrometros); o padrao e de 13.5, mas dependendo do CCD este valor pode mudar;','- Dimensao do fotometro (em milimetros); este valor refere-se a dimensao do lado do quadrado do chip do fotometro; o valor medido para este caso foi de 11 mm;','\nApos o preenchimento das informacoes pedidas, execute novamente o comando para obter a caracterizacao da curva de EQ do CCD.\n','As opcoes marcadas com \'(opcional)\' nao necessitam ser preenchidas, no momento dos calculos o codigo apenas levara em consideracao caso seja fornecido o nome de um arquivo.\n','O codigo apenas levara em consideracao os parametros situados dentro das tags \'->\' e \'<-\'; respeitando essa opcao, a organizacao dos dados pode ser feita da forma mais conveniente, permitindo comentarios e espacamento de linhas.\n','Os arquivos contendo dados a serem lidos devem conter o mesmo numero de comprimentos de onda do ensaio.\n', 'obs: nao deve haver espaco entre o nome de cada arquivo e o sinal de igualdade, caso contrario, o programa retornara um erro.'] 

    name = images_path + '\\' + 'InformacoesEnsaio.txt'
    try: open(name)
    except:     
        print('\n---Preencha o arquivo InformacoesEnsaio---\n')
        arq = open(name, 'w')       
        for Strdado in Str:
            arq.write(Strdado+'\n')
        
        for StrNota in nota:
            arq.write(StrNota+'\n')

        arq.close()
        exit()

    with open(name) as arq:     
        linhas = arq.read().splitlines()

        for linha in linhas:            
            if '->' == linha: tag1 = linha
            if '<-' == linha: 
                tag2 = linha
                break
        if tag1 != '->' : 
            print('\n Tag \'->\' nao encontrada.\n')
            exit()
        if tag2 != '<-' : 
            print('\n Tag \'<-\' nao encontrada.\n')
            exit()


        for linha in linhas:
            if '->' in tag1:
                dado = linha.split('=')             
                if 'Espectro (nm) (Einicial, Efinal, passo)' in dado[0]: intervEspectro = dado[1]
        
                if 'nome arquivo calibracao filtro densidade' in dado[0]: nomeArqCalibDetector = dado[1]

                if 'nome arquivo QE do fabricante' in dado[0]: nomeArqFabricante = dado[1]

                if 'nome arquivo detector' in dado[0]: nomeArqDetector = dado[1]

                if 'nome arquivo Log' in dado[0]: nomeArqlog = dado[1]

                if 'tag do nome das imagens (PAR2,PAR1)' in dado[0]: tagPAR2, tagPAR1 = dado[1].split(',')

                if 'ganho eletronico' in dado[0]:
                    try: ganhoCCD = float(dado[1])
                    except: 
                        print('\nErro na leitura do ganho do CCD.\n')
                        exit()  
                if 'Tamanho do pixel (um)' in dado[0]: lenPixel = float(dado[1])

                if 'Dimensao do fotometro' in dado[0]: Dfotometro = float(dado[1])

            if '<-' in linha: break     
        
        return intervEspectro,  nomeArqCalibDetector, nomeArqFabricante, nomeArqDetector, nomeArqlog, tagPAR2, tagPAR1, ganhoCCD, lenPixel, Dfotometro
    

