#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 14, 2014

@author: anroco

How to split a string on newlines in python?

¿Como dividir un string por saltos de linea en python?
'''

#create a str
s = 'red lorry,\nyellow lorry,\nred lorry,\nyellow lorry'
print(s)

#the splitlines() method return a list of the lines in the string, breaking at
#line boundaries.
l = s.splitlines()
print(l)

#if want included in the resulting list the newlines, True is passed
#as parameter
l = s.splitlines(True)
print(l)

#another way is to use the split method() passed as parameter the character
#newline.
l = s.split('\n')
print(l)
