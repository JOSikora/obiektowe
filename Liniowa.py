#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 10:51:50 2020

@author: justyna
"""

class Liniowa():
    def __init__(self, a, b):
        self.__a = float(a)
        self.__b = float(b)
     
    @property
    def a(self):
        return self.__a
    
    @property
    def b(self):
        return self.__b 
        
    def __str__(self):
        return 'Funkcja liniowa '+str(self.__a)+'*x+'+str(self.__b)
    
    def __repr__(self):
        return self.__str__()
    
    def __call__(self, x): #wartość funkcji
        return self.__a*x + self.__b
    
    def __add__(self, other):
        return Liniowa(self.__a + other.__a, self.__b + other.__b)
    
    def __mul__(self, other):
        return Liniowa(self.__a*other.__b + self.__b*other.__a, self.__b*other.__b)
    
f1 = Liniowa(1,1)
f2 = Liniowa(2,2)
print(f1)
print(f2)










