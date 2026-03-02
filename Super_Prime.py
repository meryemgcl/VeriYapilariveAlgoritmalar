def get_super_primes(n):
    """
    n'e kadar olan Süper Asalları (indeksi asal olan asalları) döner.
    """
    if n < 3:
        return []

    # 1. Adım: Eratosthenes Eleği (Hızlı ve Pythonic)
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            # p*p'den başlayarak p'şer atlayarak False yap (En hızlı yöntem)
            is_prime[p*p : n+1 : p] = [False] * len(range(p*p, n+1, p))

    # 2. Adım: Asalları bir listeye topla
    primes = [i for i, prime in enumerate(is_prime) if prime]

    # 3. Adım: Süper Asalları bul
    # ÖNEMLİ DÜZELTME: k+1 ifadesi asalın "kaçıncı" asal olduğunu belirtir.
    # Eğer bu sıra numarası (k+1) is_prime tablosunda True ise, o sayı Süper Asaldır.
    super_primes = []
    for k in range(len(primes)):
        ordinal_position = k + 1  # 1. asal, 2. asal...
        if ordinal_position <= n and is_prime[ordinal_position]:
            super_primes.append(primes[k])

    return super_primes

if __name__ == "__main__":
    n = 241
    result = get_super_primes(n)
    
    print(f"{n} sayısına kadar olan Süper Asallar:")
    # Çıktıyı yan yana temiz bir şekilde yazdırır
    print(*(result), sep=" ")
    
    # Doğrulama için: 3 (2. asal), 5 (3. asal), 11 (5. asal)...