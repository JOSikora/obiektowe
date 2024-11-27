#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 20:26:31 2020

@author: Justyna Ossibach-Sikora
"""
'''
Zadanie 3 (3 pkt)
Napisz klasę ZegarHM. Obiekty tej klasy powinny:
•	przechowywać 2 zmienne: godziny i minuty (podawane jako parametry)
•	posiadać atrybuty H i M odpowiadające godzinom i minutom, utworzone 
za pomocą dekoratora property (tylko getter)
•	posiadać reprezentację tekstową  
•	operator dodawania ma być zdefiniowany tak, aby obiekt (klasy ‘ZegarHM’) 
powstały w wyniku dodawania dwóch obiektów 'ZegarHM' reprezentował sumę czasów 
(przesunięcie pierwszej godziny o tyle godzin i minut ile przechowuje drugi obiekt).
'''

class ZegarHM():
    def __init__(self, h, m):
        if h >= 0 and m >= 0 and h < 25 and m < 60:
            self.__h = int(h)
            self.__m = int(m)
        else: 
            print('Bledna godzina lub/i minuta')
    
    @property        
    def H(self):
        return self.__h
    
    @property
    def M(self):
        return self.__m
        
    def __str__(self):
        if self.__m < 10:
            return 'Zegar wskazuje godzinę: ' + str(self.__h) + ':0' + str(self.__m)
        return 'Zegar wskazuje godzinę: ' + str(self.__h) + ':' + str(self.__m)
    
    def __repr__(self):
        return self.__str__()
    
    def __add__(self, other):
        x = self.__h + other.__h
        y = self.__m + other.__m
        if x > 23:
            x = x - 24
        if y > 59:
            y = y - 60
            x = x + 1
        
        return ZegarHM(x,y)


'''
Zadanie 4 (5 pkt)
Napisz klasę ZegarHMS, dziedziczącą po klasie Zegar HM. Obiekty tej klasy powinny:
•	przechowywać 3 zmienne: godziny, minuty, sekundy (podawane jako parametry), 
z czego dwie pierwsze powinny być przekazane do konstruktora klasy rodzica
•	posiadać atrybuty H, M, S odpowiadające godzinom, minutom i sekundom utworzone 
za pomocą dekoratora property (tylko getter, 2 pierwsze będą już odziedziczone)
•	posiadać reprezentację tekstową korzystającą z reprezentacji tekstowej klasy rodzica
•	operator dodawania ma być zdefiniowany tak, aby obiekt (klasy ‘ZegarHMS’) 
powstały w wyniku dodawania dwóch obiektów 'ZegarHMS' lub dodawania obiektu ‘ZegarHM’ 
do obiektu ‘ZegarHMS’, reprezentował sumę czasów (przesunięcie pierwszej godziny o tyle godzin, 
minut i ewentualnie sekund ile przechowuje drugi obiekt). WSKAZÓWKA: można skorzystać z try-except
'''

class ZegarHMS(ZegarHM):
    def __init__(self, h, m, s):
        super().__init__(h, m)
        if s >= 0 and s < 60:
            self.__s = int(s)
        else: 
            print('Bledna sekunda')
        
    @property        
    def S(self):
        return self.__s
    
    def __str__(self):
        if self.__s < 10:
            return super().__str__() + ':0' + str(self.__s)
        return super().__str__() + ':' + str(self.__s)
        
    def __add__(self, other):
        x = self.H + other.H
        y = self.M + other.M
        z = self.S + other.S
        if z > 59:
            z = z - 60
            y = y + 1
        if y > 59:
            y = y - 60
            x = x + 1
        if x > 23:
            x = x - 24
            
        return ZegarHMS(x,y,z)
        
























