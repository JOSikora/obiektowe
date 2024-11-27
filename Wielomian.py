#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 13:20:53 2020

@author: justyna
"""
import numpy as np

#Wielomian(a,b) = a+b*x
#Wielomian(a,b,c) = a + b*x + c*x^2

class Wielomian():
    def __init__(self, *args):
        self.__a = args
        self.__n = len(args)
        
    def __str__(self):
        if self.__n > 0:
            wynik = str(self.__a[0])
            for i in range(1, self.__n):
                wynik += ' + ' + str(self.__a[i]) + '*x^' + str(i)
            return wynik
        return '0'
    
    def __repr__(self):
        return self.__str__()
    
    def __call__(self, x):
        if self.__n > 0:
            wynik = self.__a[0]
            for i in range(1, self.__n):
                wynik += self.__a[i] * x**i
            return wynik
            #return sum([self.__a[i] * x**i for i in range(self.__n)])
        return 0
        
    def __add__(self, other):
        wynik = np.zeros(max(self.__n, other.__n))
        
        for i in range(self.__n):
            wynik[i] += self.__a[i]
            
        for i in range(other.__n):
            wynik[i] += other.__a[i]
            
        return Wielomian(*tuple(wynik))
    
    def __mul__(self, other):
        a = np.outer(self.__a, other.__a)[:,::-1]
        return Wielomian(*[a.trace(i) for i in range(other.__n - 1, -self.__n, -1)])
        
#        n = max(self.__n, other.__n)
#        wynik = np.zeros(n)
#        
#        for i in range(n):
#            for j in range(n):
#                wynik[i,j] = self.__a[i]*other.__a[i]
#        
#        for 
#        
#        return Wielomian()
      
        
    def pochodna(self):
        return Wielomian(*[i*self.__a[i] for i in range(1, self.__n)])
    
    def calka(self):
        return Wielomian(0, *[self.__a[i]/(i+1) for i in range(self.__n)])
    
    
w = Wielomian(1,2,3,4)

# 1 + 2*x^1 + 3*x^2 + 4*x^3  -> (1,2,3,4)
#                               (0,1,2,3)
#pochodna to: 
# 2*1 + 3*2*x^1 + 4*3*x^2  -> (2,6,12)
#
#całka to:
#

w1 = Wielomian(3,4)
w2 = Wielomian(2,1)
print(w1)
print(w2)

#     (3  ,  4)
# (2)  6     8
# (1)  3     4

#    6 + (3+8) * x^1 + 4 * x^2




