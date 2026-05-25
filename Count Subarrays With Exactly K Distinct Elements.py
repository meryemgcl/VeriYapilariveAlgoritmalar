from collections import Counter

def exactlyK(arr: list, k: int) -> int:
    
    # Yardımcı fonksiyon: En fazla 'max_distinct' kadar benzersiz eleman içeren alt dizileri sayar
    def atMostK(max_distinct: int) -> int:
        if max_distinct <= 0:
            return 0
            
        freq = Counter()
        left = 0
        count = 0
        
        for right in range(len(arr)):
            # Genişleyen pencereye yeni elemanı ekle
            freq[arr[right]] += 1
            
            # Eğer benzersiz eleman sayısı sınırı aşarsa, sol tarafı daralt
            while len(freq) > max_distinct:
                freq[arr[left]] -= 1
                if freq[arr[left]] == 0:
                    del freq[arr[left]]
                left += 1
                
            # Geçerli pencere boyutunu (alt dizi sayısını) toplam sonuca ekle
            count += right - left + 1
            
        return count

    # Matematiksel mantık: Tam olarak K = (En fazla K) - (En fazla K-1)
    return atMostK(k) - atMostK(k - 1)

if __name__ == "__main__":
    arr = [1, 2, 2, 3]
    k = 2
    print(exactlyK(arr, k))  # Çıktı: 4