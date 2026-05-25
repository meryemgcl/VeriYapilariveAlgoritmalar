class Node:
    def __init__(self, x: int):
        self.data = x
        self.left = None
        self.right = None

def inorder_generator(root: Node):
    """Ağacı inorder sırayla dönen bir Python üreteci (Generator).
    Bellekte liste tutmaz, elemanları ihtiyaç duyuldukça (lazy evaluation) üretir."""
    if root:
        yield from inorder_generator(root.left)
        yield root.data
        yield from inorder_generator(root.right)

def merge(root1: Node, root2: Node) -> list:
    # İki ağaç için de üreteçleri (generator) başlatıyoruz
    gen1 = inorder_generator(root1)
    gen2 = inorder_generator(root2)
    
    result = []
    
    # Üreteçlerden ilk elemanları çekiyoruz
    val1 = next(gen1, None)
    val2 = next(gen2, None)
    
    # İki üreteçte de eleman olduğu sürece küçük olanı seçerek ilerle (O(N + M))
    while val1 is not None and val2 is not None:
        if val1 <= val2:
            result.append(val1)
            val1 = next(gen1, None)
        else:
            result.append(val2)
            val2 = next(gen2, None)
            
    # Kalan elemanları doğrudan listeye ekle
    while val1 is not None:
        result.append(val1)
        val1 = next(gen1, None)
        
    while val2 is not None:
        result.append(val2)
        val2 = next(gen2, None)
        
    return result

if __name__ == "__main__":
    # Ağaç 1 Oluşturma
    root1 = Node(3)
    root1.left = Node(1)
    root1.right = Node(5)
    
    # Ağaç 2 Oluşturma
    root2 = Node(4)
    root2.left = Node(2)
    root2.right = Node(6)
    
    res = merge(root1, root2)
    print(*res)  # Çıktı: 1 2 3 4 5 6