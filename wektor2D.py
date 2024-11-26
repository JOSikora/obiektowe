#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 13:13:20 2020
@author: justyna
"""
class wektor2D():
    def __init__(self, x, y):
        self.__x = int(x)
        self.__y = int(y)
        
    def __get_x(self):
        return self.__x
    
    def __set_x(self, x):
        self.__x = int(x)
    
    x = property(__get_x, __set_x)
    
    def __get_y(self):
        return self.__y
    
    def __set_y(self, x):
        self.__y = int(y)
    
    y = property(__get_y, __set_y)
    
#    @property
#    def x(self):
#        return self.__x
        
    def __str__(self):
        return 'wektor 2D: '+ str(self.__x)+', '+ str(self.__y)
    
    def __repr__(self):
        return self.__str__()
    
    def __dlugosc(self):
        return ((self.__x)**2 + (self.__y)**2)**(0.5)
    
    def __abs__(self):
        return self.__dlugosc()
    
    def kwadratowa(self, x):
        return self.__x*x
    
    def mnozenie(self, mnoznik):
        self.__x = int(mnoznik) * self.__x
        self.__y = int(mnoznik) * self.__y
    
a = wektor2D(3,4)
print(a)













