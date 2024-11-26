#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 11:24:05 2020
@author: justyna
"""

'''
klasa - pracownik UW #abstrakcjny format danych
    atrybuty: imie, nazwisko, wydział

obiekt - TG jest obiektem klasy człowiek
    imie = 'Tomasz'
    nazwisko = 'Gubiec'
    wydział = 'Fizyki'
'''

class pracownikUW():
    def __init__(self, imie, nazwisko, wydzial): #inicjacja nowego obiektu, ustawianie wart zmiennych
        self.Imie = imie
        self.Nazwisko = nazwisko
        self.Wydzial = wydzial
        
    #uproszczona reprezentacja tekstowa
    def __str__(self):
        return 'pracownik UW: '+ str(self.Imie) + ' ' + str(self.Nazwisko)
    
    #pełna reprezentacja tekstowa    
    def __repr__(self):
        return self.__str__() +' z Wydziału ' + str(self.Wydzial)
    
#TG = pracownikUW #nowa nazwa 'TG' dla klasy pracownikUW
TG = pracownikUW('Tomasz', 'Gubiec', 'Fizyki') # tworzy obiekt klasy pracownikUW o nazwie 'TG'
JK = pracownikUW('Jan', 'Kowalski', 'Chemii')

print(TG)
print(JK)
