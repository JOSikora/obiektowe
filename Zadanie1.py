#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 19:34:09 2020

@author: Justyna Ossibach-Sikora
"""
'''
Zadanie 1 (3 pkt)
Napisz klasę „do10” dziedziczącą po klasie „int” (liczbach całkowitych). 
Zmiana polega na tym, że przy dodawaniu dwóch obiektów klasy „do10” otrzymujemy 
obiekt klasy „do10” odpowiadający reszcie z dzielenia przez 10 liczb sumy 
liczb im odpowiadających. Analogicznie dla mnożenia.
'''

class Int():
    def __init__(self, x):
        self.__x = int(x)
        
    def __str__(self):
        return str(self.__x)
    
    def __repr__(self):
        return self.__str__()
        
    def __add__(self, other):
        return self.__x + other.__x
    
    def __mul__(self, other):
        return self.__x * other.__x

class do10(Int):
    def __init__(self, x):
        super().__init__(x)
        
    def __add__(self, other):
        return do10(super().__add__(other)%10)
    
    def __mul__(self, other):
        return do10(super().__mul__(other)%10)
        
    