# -*- coding: utf-8 -*-
"""
Created on Aug 10, 2016
@author: Denis Bernardes & Eder Martioli
Laboratorio Nacional de Astrofisica, Brazil
"""

import os

def readlist(inputlist) :
	with open(inputlist) as f:
   		lines = f.read().splitlines()
	return lines


