from functools import lru_cache
import sys

# Python'da varsayılan özyineleme sınırı 1000'dir. 
# Çok büyük n değerleri için bu sınırı artırmak gerekebilir:
sys.setrecursionlimit(2000)

@lru_cache(maxsize=None)
def get_nck_recursive(n, k):
    """
    Özyinelemeli ve otomatik memoization (lru_cache) kullanan hesaplama.
    """
    # Temel durumlar
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    
    # Simetri kuralı: nCk = nC(n-k) 
    # Bu özellik hesaplama süresini yarı yarıya indirebilir.
    if k > n // 2:
        k = n - k

    # Pascal kuralı: C(n, k) = C(n-1, k-1) + C(n-1, k)
    return get_nck_recursive(n - 1, k - 1) + get_nck_recursive(n - 1, k)

def binomial_coeff_optimized(n, k):
    """
    Iteratif (Döngüsel) Yaklaşım - O(k) zaman, O(1) alan karmaşıklığı.
    Bu yöntem bellek ve hız açısından en gelişmiş halidir.
    """
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    
    # Simetriyi kullan (k'yı küçültmek için)
    if k > n // 2:
        k = n - k
    
    res = 1
    for i in range(k):
        # nCk = [n * (n-1) * ... * (n-k+1)] / [k * (k-1) * ... * 1]
        res = res * (n - i) // (i + 1)
        
    return res

if __name__ == "__main__":
    n, k = 5, 2
    
    # 1. Yöntem: Geliştirilmiş Özyinelemeli
    print(f"Recursive Sonuç ({n},{k}): {get_nck_recursive(n, k)}")
    
    # 2. Yöntem: En Optimize İteratif (Büyük sayılar için tavsiye edilen)
    print(f"Iteratif Sonuç ({n},{k}): {binomial_coeff_optimized(n, k)}")
    
    # Python 3.8+ için gömülü en hızlı yöntem:
    import math
    print(f"Python Math Modülü: {math.comb(n, k)}")