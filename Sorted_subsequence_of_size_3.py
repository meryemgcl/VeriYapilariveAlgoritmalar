def find_increasing_triplet(arr):
    """
    Dizi içinde a < b < c kuralına uyan ilk üçlüyü bulur.
    Zaman Karmaşıklığı: O(n), Alan Karmaşıklığı: O(n)
    """
    n = len(arr)
    if n < 3:
        print("Dizi çok kısa.")
        return

    # Sol taraftaki en küçük elemanların indislerini tutar
    smaller = [-1] * n
    min_idx = 0
    for i in range(1, n):
        if arr[i] <= arr[min_idx]:
            min_idx = i
            smaller[i] = -1
        else:
            smaller[i] = min_idx

    # Sağ taraftaki en büyük elemanların indislerini tutar
    greater = [-1] * n
    max_idx = n - 1
    for i in range(n - 2, -1, -1):
        if arr[i] >= arr[max_idx]:
            max_idx = i
            greater[i] = -1
        else:
            greater[i] = max_idx

    # Hem solunda küçük hem sağında büyük eleman olan sayıyı bul
    for i in range(n):
        if smaller[i] != -1 and greater[i] != -1:
            print(f"Bulunan üçlü: {arr[smaller[i]]}, {arr[i]}, {arr[greater[i]]}")
            return

    print("Uygun bir üçlü bulunamadı.")

# Test
if __name__ == "__main__":
    data = [12, 11, 10, 5, 6, 2, 30]
    find_increasing_triplet(data)