class Node:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None

def noSibling(root: Node) -> list:
    # Boş ağaç veya tek düğümlü ağaç durumunda boş liste döndür
    if not root:
        return []

    ans = []

    # İç yardımcı fonksiyon (Closure) kullanarak parametre taşıma zahmetinden kurtuluyoruz
    def traverse(node):
        if not node:
            return

        # Sol çocuk var ama sağ yoksa -> Sol çocuk öksüzdür
        if node.left and not node.right:
            ans.append(node.left.data)
            
        # Sağ çocuk var ama sol yoksa -> Sağ çocuk öksüzdür
        elif node.right and not node.left:
            ans.append(node.right.data)

        # Ağacın derinliklerine inmeye devam et
        traverse(node.left)
        traverse(node.right)

    traverse(root)
    
    # Sonucu sıralı istiyorsak sorted() kullanmak daha Pythonic bir yaklaşımdır
    return sorted(ans) if ans else [-1]

if __name__ == "__main__":
    # Ağaç Oluşturma
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.left.left = Node(6)

    ans = noSibling(root)
    
    # Listeyi aralarında boşluk bırakarak yazdırmanın en temiz ve insansı yolu
    print(*ans)  # Çıktı: 4 5 6