#!/usr/bin/python
# -*- coding: utf-8 -*-
from sort import quicksort, bubblesort


from timeit import timeit
import random


slownik = {"lista_posortowana":list(range(1000)),"lista_posortowana_odwrotnie":list(range(1000,0,-1)),
           "lista_rowne_wartosci":[5]*1020,"lista_losowe_wartosci":random.sample(range(0,1001),1)}

for value,key in slownik.items():
    t1_bubble = timeit("bubblesort(key)",number=100,globals=globals())
    t1_quick =  timeit( "quicksort(key)", number =100 ,globals = globals())

    if t1_bubble < t1_quick:
        print(" szybszy jest bubblesort ")
    if t1_bubble > t1_quick:
        print('szybszy jest quicksort')



    print(t1_bubble)
    print(t1_quick)


print("Bubblesort jest szybszy dla listy posortowanej oraz dla listy\n"
       "o równych wartościach natomiast quicksort dla listy posortowanej odwrotnie i listy o losowych wartościach\n"
      "testy wykonywane są przy pomocy pętli for, która przy pomocy klucza przechodzi po słowniku, natomiast w słowniku zainicjalizowane są listy  ")