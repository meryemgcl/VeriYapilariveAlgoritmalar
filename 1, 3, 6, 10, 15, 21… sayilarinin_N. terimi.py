def get_nth_term_optimized(n):
    """
    1'den n'e kadar olan sayıların toplamını (Triangular Number) hesaplar.
    Matematiksel Formül: n * (n + 1) / 2
    Zaman Karmaşıklığı: O(1) - Sabit zaman
    """
    if n < 0:
        return 0
    # Tam sayı bölmesi (//) kullanarak sonucu integer olarak döndürüyoruz
    return (n * (n + 1)) // 2

def get_nth_term_pythonic(n):
    """
    Python'un gömülü sum() fonksiyonunu kullanarak hesaplama.
    Zaman Karmaşıklığı: O(n) - Döngü mantığı
    """
    return sum(range(1, n + 1))

if __name__ == "__main__":
    n = 4
    
    # 1. Yöntem: Matematiksel (En Hızlısı)
    print(f"n={n} için Terim (Matematiksel): {get_nth_term_optimized(n)}")
    
    # 2. Yöntem: Pythonic (Kısa Kod)
    print(f"n={n} için Terim (Pythonic): {get_nth_term_pythonic(n)}")
    
    # Büyük sayı testi:
    big_n = 1_000_000
    print(f"n={big_n} için sonuç hesaplandı (O(1) sayesinde anında).")