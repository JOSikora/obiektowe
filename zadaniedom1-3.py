#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 22:21:54 2020

@author: justyna
"""
'''
MYŚLĘ, ŻE WARTO NA NASTĘPNYCH ZAJĘCIACH POWTÓRZYĆ JESZCZE PROPERTY
DZIĘKUJĘ
'''



'''
Zadanie 1. Utwórz klasę Punkt1, która będzie służyła do reprezentowania punktu
na płaszczyźnie. Klasa powinna mieć dwa prywatne pola (współrzędne punktu), 
konstruktor (chodzi o metodę __init__) oraz metody: get_x, get_y, set_x, set_y, 
odlegloscOdZera (liczy odległość od zera), nachylenie (współczynnik kierunkowy 
prostej przechodzącej przez zero i ten punkt), __str__ (opis punktu postaci (x; y)).
'''

class Punkt1():
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    def set_x(self, x):
        self.__x = float(x)
    
    def set_y(self, y):
        self.__y = float(y)
    
    def odlegloscOdZera(self):
        return ((self.__x)**2 + (self.__y)**2)**0.5
    
    def nachylenie(self):
        return self.__y / self.__x
    
    def __str__(self):
        return '(' + str(self.__x) + '; ' + str(self.__y) + ')'
    
    def __repr__(self):
        return self.__str__()

P = Punkt1(3,4)


'''
Zadanie 2. Utwórz klasę Punkt2, która jest kopią klasy Punkt1, ale zamiast 
metod get_x, get_y, set_x, set_y posiada atrybuty x i y utworzone za pomocą property.
'''
class Punkt2():
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    def __get_x(self):
        return self.__x
    
    def __get_y(self):
        return self.__y
    
    def __set_x(self, x):
        self.__x = float(x)
    
    def __set_y(self, y):
        self.__y = float(y)
    
    x = property(__get_x, __set_x)
    y = property(__get_y, __set_y)
    
    
    def odlegloscOdZera(self):
        return ((self.__x)**2 + (self.__y)**2)**0.5
    
    def nachylenie(self):
        return self.__y / self.__x
    
    def __str__(self):
        return '(' + str(self.__x) + '; ' + str(self.__y) + ')'
    
    def __repr__(self):
        return self.__str__()

R = Punkt2(3,4)

'''
Zadanie 3. Utwórz klasę Kwadrat. Obiekty tej klasy powinny: 
przechowywać długość boku kwadratu w postaci zmiennej prywatne 
( ale zapewnić do niej dostęp beż możliwości zmiany wartości - dekorator property), 
posiadać reprezentację tekstową, posiadać metody zwracające pole i obwód kwadratu.
'''

class Kwadrat():
    def __init__(self, bok):
        self.__a = bok
        
    @property
    def bok(self):
        return self.__a
    
    def __str__(self):
        return 'kwadrat o boku: ' + str(self.bok)
    
    def __repr__(self):
        return self.__str__()
    
    def pole(self):
        return self.__a**2

    def obwod(self):
        return self.__a*4

K = Kwadrat(2)



class Punkt3():
    def __init__(self, x, y):
        self.__wsp = [float(x), float(y)]
    
    @property
    def wsp(self):
        return self.__wsp[:]












