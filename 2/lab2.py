import time

def kreiraj_matricu(n: int, k_ovi: list) -> list:
    graf: list = [[0] * n for _ in range(n)]
    for j in range(n):
        for i in range(n):
            if abs(i - j) in k_ovi:
                graf[i][j] = 1

    return graf

def dfs(graf: list, src: int, put = []) -> list:    
    if src not in put:
        put.append(src)

        for i in range(len(graf[src])):
            if graf[src][i] == 1:
                dfs(graf, i, put)

    return put

def ciklus(v: int, graf: list, visited: list, n: int) -> bool:
    if len(hamil) == n + 1 and hamil[0] == v:
        global flag
        flag = True
        #print(hamil)
        return

    if flag == True:
        return

    for i in range(n-1, -1, -1):
        if graf[v][i] == 1 and visited[i] == 0:
            visited[i] = 1
            hamil.append(i)
            graf[i][v] = 0

            ciklus(i, graf, visited, n)
            
            graf[i][v] = 1
            visited[i] = 0
            hamil.pop()

if __name__ == "__main__":
    n: int = int(input("Unesite prirodan broj n: "))
    k_ovi: list = [int(input(f"Unesite vrijednost prirodnog broja k_{i + 1}: ")) for i in range(4)]
    
    graf = kreiraj_matricu(n, k_ovi)
    
    put: list = dfs(graf, 0)
    if len(put) != n:
        print("Graf G nije povezan\nGraf G nije hamiltonovski")
    else:
        print("Graf G je povezan")
        
        hamil: list = []
        hamil.append(0)
        flag: bool = False
        visited: list = [0] * n
        
        start = time.time()
        
        ciklus(0, graf, visited, n)
        
        if flag == True:
            print("Graf G je hamiltonovski")
        else:
            print("Graf G nije hamiltonovski")
        
        end = time.time()
        print(end - start)