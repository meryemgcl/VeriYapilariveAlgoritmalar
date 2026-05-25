class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

# Varsayılan parametreler (default arguments) kullanarak tek fonksiyonda çözüyoruz.
# Böylece hantal 'Util' yardımcı fonksiyonlarına gerek kalmıyor.
def isBST(node: Node, min_val=float('-inf'), max_val=float('inf')) -> bool:
    # Base Case: Boş ağaç veya yaprak düğümün altı her zaman geçerli bir BST'dir
    if node is None:
        return True

    # Mevcut düğümün değeri belirlenen güvenli aralığın dışındaysa BST değildir
    if not (min_val < node.data < max_val):
        return False

    # Sol alt ağaç için üst sınırı, sağ alt ağaç için alt sınırı güncelleyerek ilerle.
    # Ondalıklı sayıları da desteklemesi için -1/+1 gibi tam sayı zorunluluklarını kaldırdık.
    return isBST(node.left, min_val, node.data) and isBST(node.right, node.data, max_val)

if __name__ == "__main__":
    # Test için örnek ikili ağaç oluşturma
    #       10
    #      /  \
    #     5    20
    #         /  \
    #        9    25
    root = Node(10)
    root.left = Node(5)
    root.right = Node(20)
    root.right.left = Node(9)   # Bu düğüm 10'dan büyük ama sağ kolda olduğu için 10'dan küçük olamaz! BST'yi bozar.
    root.right.right = Node(25)

    # Sonucu Pythonic ve temiz bir şekilde yazdırıyoruz
    print(str(isBST(root)).lower())  # Çıktı: false