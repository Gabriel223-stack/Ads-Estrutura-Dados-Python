#montagem da lista de adjacência

grafo = {
    1: [2,3],
    2: [1,4,5],
    3: [1,4],
    4: [2,5,3,6],
    5: [2,4],
    6: [4,7,8],
    7: [6,8],
    8: [6,7]
}

for vertice, adjacentes in grafo.items():
    print(f"{vertice} -> {adjacentes}")