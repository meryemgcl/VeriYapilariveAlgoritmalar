class Node:
    def __init__(self, x: int):
        self.data = x
        self.next = None
        self.random = None

def cloneLinkedList(head: Node) -> Node:
    if not head:
        return None

    # 1. ADIM: Her orijinal düğümün ardına kendi klonunu ekle (Örn: 1 -> 1' -> 2 -> 2')
    curr = head
    while curr:
        cloned = Node(curr.data)
        cloned.next = curr.next
        curr.next = cloned
        curr = cloned.next

    # 2. ADIM: Klon düğümlerin 'random' işaretçilerini bağla
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next

    # 3. ADIM: Orijinal liste ile klon listeyi birbirinden ayır (Dokumayı sök)
    curr = head
    cloned_head = head.next
    
    while curr:
        cloned_node = curr.next
        curr.next = cloned_node.next  # Orijinal bağları eski haline getir
        
        if cloned_node.next:
            cloned_node.next = cloned_node.next.next  # Klon bağlarını birleştir
            
        curr = curr.next

    return cloned_head

def printList(head: Node):
    curr = head
    output = []
    while curr:
        random_val = curr.random.data if curr.random else 'null'
        output.append(f"{curr.data}({random_val})")
        curr = curr.next
    print(" -> ".join(output))

if __name__ == "__main__":
    # Test verisini oluşturma
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    
    head.random = head.next.next
    head.next.random = head
    head.next.next.random = head.next.next.next.next
    head.next.next.next.random = head.next.next
    head.next.next.next.next.random = head.next
    
    print("Original linked list:")
    printList(head)
    
    clonedList = cloneLinkedList(head)
    
    print("Cloned linked list:")
    printList(clonedList)