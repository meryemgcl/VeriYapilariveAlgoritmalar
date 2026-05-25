class Node:
    def __init__(self, value: int):
        self.data = value
        self.left = None
        self.right = None

def lca(root: Node, n1: Node, n2: Node) -> Node:
    # Base Case: Ağaç boşsa veya aranan düğümlerden birine ulaştıysak mevcut düğümü döndür
    if root is None or root == n1 or root == n2:
        return root

    # Sol ve sağ alt ağaçlarda düğümleri ara (Tek geçişli DFS)
    left_res = lca(root.left, n1, n2)
    right_res = lca(root.right, n1, n2)

    # Eğer hem sol koldan hem sağ koldan bir düğüm döndüyse; 
    # n1 ve n2 farklı kollardadır, yani mevcut düğüm en yakın ortak atadır (LCA).
    if left_res and right_res:
        return root

    # Sadece bir koldan sonuç döndüyse, o sonucu yukarıya fırlat (Taşı)
    return left_res if left_res else right_res

if __name__ == "__main__":
    # İkili Ağaç Oluşturma
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.left = Node(8)

    # Test Senaryosu: Düğüm 7 ve Düğüm 8
    n1 = root.right.right       # Node 7
    n2 = root.right.left.left   # Node 8

    ans = lca(root, n1, n2)
    
    if ans:
        print(ans.data)  # Çıktı: 3