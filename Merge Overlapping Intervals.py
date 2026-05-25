def mergeOverlap(arr):
    if not arr:
        return []

    # Aralıkları başlangıç zamanlarına göre sıralıyoruz
    arr.sort(key=lambda x: x[0])
    
    # İlk aralığı direkt sonuç listesine ekleyerek başlıyoruz
    res = [arr[0]]

    for current in arr[1:]:
        last_added = res[-1]
        
        # Eğer mevcut aralığın başlangıcı, son eklenen aralığın bitişinden küçük veya eşitse: ÇAKIŞMA VAR
        if current[0] <= last_added[1]:
            # Son eklenen aralığın bitişini güncelliyoruz
            last_added[1] = max(last_added[1], current[1])
        else:
            # Çakışma yoksa yeni aralığı listeye ekliyoruz
            res.append(current)
            
    return res

if __name__ == "__main__":
    arr = [[7, 8], [1, 5], [2, 4], [4, 6]]
    res = mergeOverlap(arr)

    for start, end in res:
        print(f"{start} {end}")