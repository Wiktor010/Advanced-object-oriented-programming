#!/usr/bin/python
# -*- coding: utf-8 -*-
#Wiktor_Wiernasiewicz_405029

from typing import List
from typing import Dict

def adjmat_to_adjlist(adjmat: List[List[int]]) -> Dict[int, List[int]]:
    x : int
    y : int
    slownik = {}
    for x,row in enumerate(adjmat,start=1):
        slownik[x] = []
        for y,col in enumerate(row,start=1):
            slownik[x] = slownik[x] + col * [y]
        if not slownik[x]:
            del slownik[x]

    return slownik


def dfs_recursive(G: Dict[int, List[int]], s: int) -> List[int]:
    visited : list =[]

    return dfs_2_recursive(G,s,visited)

def dfs_2_recursive(G:Dict[int,List[int]],s:int,visited=[])->List[int]:

    if s not in visited:
        visited.append(s)

    if s in G.keys():
        for v in G[s]:
            if v not in visited:
                visited =dfs_2_recursive(G,v,visited)
    return visited

def dfs_iterative(G: Dict[int, List[int]], s: int) -> List[int]:
    visited=[]
    stos = [s]
    while stos:
        v1 = stos.pop(0)
        if v1 not in visited:
            visited += [v1]
            if v1 in G.keys():
                stos = [i for i in G[v1] if i not in visited] + stos
    return visited


def is_acyclic(G: Dict[int, List[int]]) -> bool:
    visited = []

    def is_1acyclic(G,row,visited):
        if row not in visited:
            visited.append(row)
        for v1 in G[row]:
            if v1 in G.keys():
                if v1 in visited or is_1acyclic(G,v1,visited[:]):
                    return True
        return False
    for row in G.keys():
        if is_1acyclic(G,row,visited):
            return False
    return True






