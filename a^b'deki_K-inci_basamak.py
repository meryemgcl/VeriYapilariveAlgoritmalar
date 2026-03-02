def kth_digit(a, b, k):
    """
    a^b sayısının sağdan k. basamağını döndürür.
    Örnek: a=5, b=2, k=1 => 5^2 = 25, sağdan 1. basamak 5'tir.
    """
    # 1. Adım: Sadece ihtiyacımız olan basamakları korumak için mod alıyoruz.
    # Sağdan k. basamağa kadar olan kısım (a^b % 10^k) bize yeterlidir.
    mod = 10 ** k
    
    # 2. Adım: Hızlı Üs Alma (Modular Exponentiation)
    # Python'un gömülü pow(taban, üs, mod) fonksiyonu O(log b) hızında çalışır
    # ve devasa sayılarda bile bellek hatası vermez.
    target_part = pow(a, b, mod)
    
    # 3. Adım: Hedef basamağı çekip çıkarma
    # Örneğin sayı 1234 ve k=3 ise, önce 10^(3-1) yani 100'e böleriz -> 12
    # Sonra 10'a göre mod alırız -> 2.
    result = (target_part // (10 ** (k - 1))) % 10
    
    return result

if __name__ == "__main__":
    # Örnek 1: 5^2 = 25 -> Sağdan 1. basamak: 5
    print(f"Örnek 1: {kth_digit(5, 2, 1)}") 
    
    # Örnek 2: 3^10 = 59049 -> Sağdan 4. basamak: 9
    print(f"Örnek 2: {kth_digit(3, 10, 4)}")
    
    # Örnek 3: Devasa bir sayı denemesi
    # 12^500 sayısının sağdan 5. basamağı
    print(f"Örnek 3: {kth_digit(12, 500, 5)}")