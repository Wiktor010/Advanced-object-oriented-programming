# Wiktor Wiernasiewicz,405029
from typing import List,Tuple
import random
import copy





def quicksort( I:List[int]):
    def quicksort_inplace(I, start:int, stop:int):
        i = start
        j = stop
        pivot = (start + stop) // 2

        while i < j:
            while I[i] < I[pivot]:
                i += 1
            while I[j] > I[pivot]:
                j -= 1
            if i <= j:
                I[i], I[j] = I[j], I[i]
                i = i + 1
                j = j - 1
        if start < j:
            quicksort_inplace(I, start, j)

        if i < stop:
            quicksort_inplace(I, i, stop)

        return I


    kopia = I.copy()

    return quicksort_inplace(kopia, 0, len(I)-1)




def bubblesort(I:List[int])->Tuple[List[int],int]:


    n = len(I)
    kopia = I.copy()
    licznik = 0
    flaga = True
    while n > 1 and flaga:
        flaga = False
        for i in range(1,n):
            if kopia[i-1] > kopia[i]:
                kopia[i-1], kopia[i] = kopia[i], kopia[i-1]
                flaga = True
            licznik = licznik +1
        n = n-1
    return kopia, licznik









