import math

def get_prime_factors(n):
    """
    n sayısının benzersiz asal çarpanlarını döndürür.
    Zaman Karmaşıklığı: O(sqrt(n))
    """
    factors = []
    
    # 1. Adım: 2'ye bölünebilme kontrolü (En küçük ve tek çift asal)
    if n % 2 == 0:
        factors.append(2)
        while n % 2 == 0:
            n //= 2  # Tam sayı bölmesi (integer division)
            
    # 2. Adım: 3'ten başlayarak tek sayılarla kontrol
    # n'in kareköküne kadar gitmek yeterlidir (Matematiksel kural)
    limit = int(math.sqrt(n))
    for i in range(3, limit + 1, i + 2):
        if n % i == 0:
            factors.append(i)
            while n % i == 0:
                n //= i
        # n küçüldüğü için karekök limitini dinamik olarak takip edebiliriz
        if n == 1: break

    # 3. Adım: Eğer n hala 1'den büyükse, kendisi bir asaldır
    if n > 1:
        factors.append(n)
        
    return factors

# BONUS: Çarpanların kaçar adet olduğunu da veren versiyon
def get_prime_factors_with_counts(n):
    counts = {}
    temp_n = n
    
    # 2 için kontrol
    d = 2
    while d * d <= temp_n:
        while temp_n % d == 0:
            counts[d] = counts.get(d, 0) + 1
            temp_n //= d
        d += 1 if d == 2 else 2
        
    if temp_n > 1:
        counts[temp_n] = counts.get(temp_n, 0) + 1
    return counts

if __name__ == "__main__":
    n = 100
    
    # Temel Liste Çıktısı
    result = get_prime_factors(n)
    print(f"{n} sayısının asal çarpanları: {' '.join(map(str, result))}")
    
    # Detaylı Sözlük Çıktısı (Örn: 100 = 2^2 * 5^2)
    detailed = get_prime_factors_with_counts(n)
    print(f"Detaylı analiz: {detailed}")