#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Criado em 10 de Agosto 2016
Descricao: tendo como entrada um arquivo texto, retorna uma lista separando cada uma das linhas do texto fornecido.
@autor: Denis Bernardes & Eder Martioli
Laboratorio Nacional de Astrofisica, Brazil
"""

import os

def readlist(inputlist) :
	with open(inputlist) as f:
   		lines = f.read().splitlines()
	return lines


