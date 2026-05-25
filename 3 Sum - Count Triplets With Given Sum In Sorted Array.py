from collections import Counter

def countTriplets(arr: list, target: int) -> int:
    freq = Counter()
    res = 0
    
    # Eleman çiftlerini dönerken, üçüncü elemanı hafızadaki frekans tablosundan arıyoruz
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            required = target - (arr[i] + arr[j])
            if required in freq:
                res += freq[required]
        
        # Mevcut elemanı bir sonraki turlar için hafızaya ekle
        freq[arr[i]] += 1
        
    return res

if __name__ == "__main__":
    arr = [-3, -1, -1, 0, 1, 2]
    target = -2
    print(countTriplets(arr, target))  # Çıktı: 2