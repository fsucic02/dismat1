import math
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.pyplot import show

INT_MAX = 1e6 

def dfs(graf: list, src: int, path = []) -> list:    
    if src not in path:
        path.append(src)

        for i in range(len(graf[src])):
            if graf[src][i] != INT_MAX:
                dfs(graf, i, path)

    return path
    
def kreiraj_matricu(n: int, abc: list) -> list:
    graph: list = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if (i < j):
                value = math.floor((abs(abc[0] * (i+1) - abc[1] * (j + 1))) / abc[2])
                graph[i][j] = graph[j][i] = value

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0:
                graph[i][j] = graph[j][i] = INT_MAX

    return graph

def prim(graph: list) -> list:
    n: int = len(graph)
    mst: list = [[0] * n for _ in range(n)]
    selected: list = [False] * n
    no_edge: int = 0
    selected[0] = True

    while (no_edge < n - 1):
        min: int = INT_MAX
        x = y = 0
        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and graph[i][j] != INT_MAX:
                        if min > graph[i][j]:
                            min = graph[i][j]
                            x, y = i, j

        selected[y] = True
        no_edge += 1
        mst[x][y] = mst[y][x] = min
    
    return mst

def prufer(graph: list) -> None:
    n: int = len(graph)
    # code: list = []
    '''for _ in range(n):
        if len(code) == n - 2:
            break
        for i in range(n):
            if sum(graph[i]) == 1:
                for j in range(n):
                    if graph[i][j] == 1:
                        code.append(j+1)
                        graph[i][j] = graph[j][i] = 0
                break

    print(code)'''
    
    n: int = len(graph)
    G = nx.Graph()
    prufer = nx.Graph()

    if n >= 2:
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 1:
                    G.add_edge(i+1, j+1)
                    prufer.add_edge(i, j)
                    graph[j][i] = 0
        
        kod = nx.to_prufer_sequence(prufer)
        kod = [i+1 for i in kod]
        if n <= 35:
            nx.draw(G, with_labels = 1, pos = nx.spring_layout(G))
            plt.show(block = False)
        nx.from_prufer_sequence

        print(f"Prüferov kod minimalnog razapinjuceg stabla: ({', '.join(map(str, kod))})")
        show()
    else:
        print("Unesite n ≥ 2")
        main()

def main() -> None:
    n: int = int(input("Unesite prirodan broj n: "))
    abc = [int(input(f"Unesite vrijednost prirodnog broja {_}: ")) for _ in ["a", "b", "c"]]

    graph: list = kreiraj_matricu(n, abc)
    path = dfs(graph, 0)
    if len(path) == n:
        print("Graf G je povezan graf")
        mst: list = prim(graph)

        for i in range(n):
            for j in range(n):
                if mst[i][j] != 0:
                    mst[i][j] = mst[j][i] = 1

        prufer(mst)
    else:
        print("Graf G nije povezan graf")

if __name__ == "__main__":
    main()