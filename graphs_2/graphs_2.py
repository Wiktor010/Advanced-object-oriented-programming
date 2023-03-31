#Wiernasiewicz_Wiktor_405029
#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List, NamedTuple, Set, Dict, Tuple
import networkx as nx
from enum import Enum, auto


# Pomocnicza definicja podpowiedzi typu reprezentującego etykietę
# wierzchołka (liczba 1..n).
VertexID = int
EdgeID = int
Distance = int

# Pomocnicza definicja podpowiedzi typu reprezentującego listę sąsiedztwa.
AdjList = Dict[VertexID, List[VertexID]]


class Colour(Enum):
    BIAŁY = auto()
    SZARY = auto()
    CZARNY = auto()

def neighbors(adjlist: AdjList, start_vertex_id: VertexID,
              max_distance: Distance) -> Set[VertexID]:

    neighbors: List[VertexID] = []
    colours: Dict[VertexID, str] = {}
    for i in adjlist:
        colours[i] = Colour.BIAŁY
        for j in adjlist[i]:
            colours[j] = Colour.BIAŁY
    colours[start_vertex_id] = Colour.SZARY
    queue: List[Tuple[VertexID, Distance]] = [(start_vertex_id, 0)]

    while len(queue) != 0:
        u = queue.pop(0) # pobieram element z kolejki
        u_id, dist = u
        if u_id in adjlist:
            u_neighbours: List[VertexID] = adjlist[u_id] # lista sądziadów u
            for i in u_neighbours:
                if colours[i] == Colour.BIAŁY:
                    colours[i] = Colour.CZARNY
                    queue.append((i, dist + 1))
            colours[u_id] = Colour.SZARY
        if 0 < dist <= max_distance:
            neighbors.append(u_id)
        elif dist > max_distance:
            return set(neighbors)

    return set(neighbors)


# Nazwana krotka reprezentująca segment ścieżki.
class TrailSegmentEntry(NamedTuple):
    v_start:VertexID
    v_end:VertexID
    edge:EdgeID
    edge_rate:float


Trail = List[TrailSegmentEntry]



def load_multigraph_from_file(filepath: str) -> nx.MultiDiGraph:
    """Stwórz multigraf na podstawie danych o krawędziach wczytanych z pliku.

    :param filepath: względna ścieżka do pliku (wraz z rozszerzeniem)
    :return: multigraf
    """
    edges: List[Tuple[int, int, float]] = []

    with open(filepath) as f:
        for line in f:
            if line.strip():
                tokens = line.split(' ')
                edges.append((int(tokens[0]), int(tokens[1]), float(tokens[2])))

    g = nx.MultiDiGraph()
    g.add_weighted_edges_from(edges)
    return g

def find_min_trail(g: nx.MultiDiGraph, v_start: VertexID, v_end: VertexID) -> Trail:
    path = nx.dijkstra_path(g, v_start, v_end)
    min_trail: Trail = []
    for i in range(1, len(path)):
        edge = g[path[i - 1]][path[i]]
        if len(edge) != 1:  # len(edge) - ilość dróg pomiędzy dwoma wierzchołkami
            x = []
            for j in range(len(edge)):
                x.append(edge[j]["weight"])
            min_x_ind = x.index(min(x))  # indeks najkrótrzej drogi
        else:
            min_x_ind = 0
        min_trail.append(
            TrailSegmentEntry(v_start=path[i - 1], v_end=path[i], edge=min_x_ind, edge_rate=edge[min_x_ind]["weight"]))
    return min_trail








def trail_to_str(trail: Trail) -> str:

        trail_str: str = ""
        total: float = 0
        for i in trail:
            trail_str += str(i.v_start) + " -[" + str(i.edge) + ": " + str(i.edge_rate) + "]-> "
            total += i.edge_rate
            if i == trail[-1]:
                trail_str += str(i.v_end)
        trail_str += "  (total = " + str(total) + ")"
        return trail_str



