#!/usr/bin/python
# coding=UTF-8

"""
    Criado em 20 de Outubro de 2016.
    
    Descricão: este modulo possui como entrada um número e retorna a posicao da casa so algarismo mais significativo.
    
    @author: Denis Varise Bernardes & Eder Martioli
    
    Laboratorio Nacional de Astrofisica, Brazil.    
 
    """

def algarismoSig(num):
	if 0< num < 1:
		dec = '%1.0e'%(num)
		dec = dec.split('-')
		dec = int(dec[1])
	
	if num > 1:
		dec = 1
    	
	return dec


