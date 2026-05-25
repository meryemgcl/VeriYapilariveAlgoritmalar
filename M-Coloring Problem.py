def is_safe(node: int, color_list: list, adj: list, current_color: int) -> bool:
    # Boyamak istediğimiz rengin, komşularda olup olmadığını anlık kontrol ediyoruz
    for neighbor in adj[node]:
        if color_list[neighbor] == current_color:
            return False
    return True

def solve_coloring(node: int, color_list: list, m: int, adj: list) -> bool:
    # Base Case: Tüm düğümler başarıyla boyandıysa çözüm bulunmuştur
    if node == len(color_list):
        return True

    # Mevcut düğüm için m adet rengi tek tek dene
    for current_color in range(m):
        # Güvenliyse (komşularla çakışmıyorsa) boya
        if is_safe(node, color_list, adj, current_color):
            color_list[node] = current_color

            # Bir sonraki düğümü boyamaya geç
            if solve_coloring(node + 1, color_list, m, adj):
                return True

            # Geri İzleme (Backtrack): Eğer sonraki adımlarda tıkanırsa rengi sıfırla
            color_list[node] = -1

    return False

def graphColoring(v: int, edges: list, m: int) -> bool:
    # Komşuluk listesini (Adjacency List) oluşturuyoruz
    adj = [[] for _ in range(v)]
    for u, w in edges:
        adj[u].append(w)
        adj[w].append(u)

    # Renk listesini -1 (boyanmamış) ile ilklendir
    color_list = [-1] * v
    
    # 0. düğümden başlayarak renklendirmeyi dene
    return solve_coloring(0, color_list, m, adj)

if __name__ == "__main__":
    V = 4
    edges = [[0, 1], [0, 2], [0, 3], [1, 3], [2, 3]]
    m = 3

    # Sonucu Pythonic ve temiz bir şekilde yazdırıyoruz
    print(str(graphColoring(V, edges, m)).lower())