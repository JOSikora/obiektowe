#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 19:47:57 2020

@author: Justyna Ossibach-Sikora
"""
'''
Zadanie 2 (3 pkt)
Napisz dekorator o nazwie „trial”. 
Funkcję udekorowaną tym dekoratorem można wywołać 
jedynie dziesięć razy. Przy jedenastym i kolejnym wywołaniu
zamiast właściwego wyniku działania funkcji ma zwracać 
None i wypisywać komunikat „kup pelna wersje”.
'''

    
def trial(fun):
    def helper():
        helper.calls += 1
        if helper.calls > 10:
            print('Kup pełną wersję')
            return None
        return fun()
    helper.calls = 0
    return helper


@trial
def x():
    print('hello')




    