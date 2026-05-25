def maxOccured(l: list, r: list) -> int:
    # Aralıklar boşsa veya uzunluklar uyuşmuyorsa koruma filtresi
    if not l or not r or len(l) != len(r):
        return -1

    # Verilerdeki maksimum sınırı buluyoruz (Örn: 8)
    max_val = max(r)
    
    # Fark dizisi için (max_val + 2) boyutunda bir liste oluşturuyoruz
    # +2 yapmamızın sebebi r[i]+1 indeksine de erişecek olmamızdır
    diff = [0] * (max_val + 2)

    # 1. Adım: Sadece aralık sınırlarını işaretle -> O(n)
    for start, end in zip(l, r):
        diff[start] += 1
        diff[end + 1] -= 1

    # 2. Adım: Kümülatif toplam (Prefix Sum) alarak en sık geçen sayıyı bul -> O(max_val)
    max_freq = 0
    result = -1
    current_freq = 0

    for i in range(1, max_val + 1):
        current_freq += diff[i]
        
        # Eğer mevcut frekans şu ana kadarkilerden büyükse güncelle
        # En küçük sayıyı istediğimiz için strictly greater (>) kullanıyoruz
        if current_freq > max_freq:
            max_freq = current_freq
            result = i

    return result

if __name__ == "__main__":
    l = [1, 2, 4, 3]
    r = [6, 4, 8, 5]
    print(maxOccured(l, r))  # Çıktı: 4 (Hem 3 hem 4 sayısı 3 kez tekrar eder, en küçüğü 4'tür)