def josephus_optimized(n, k):
    """
    Josephus probleminin O(n) zaman ve O(1) alan karmaşıklığı ile çözümü.
    n: Toplam kişi sayısı
    k: Her k. kişi elenir
    """
    survivor = 0  # 0 tabanlı indeksleme ile başla
    
    # 1'den n'e kadar olan her adımda hayatta kalanın yeni konumunu hesapla
    for i in range(2, n + 1):
        survivor = (survivor + k) % i
        
    # İnsanlar genelde 1'den başladığı için sonucu 1-tabanlı döndür
    return survivor + 1

if __name__ == "__main__":
    n = 7
    k = 3
    print(f"n={n}, k={k} için hayatta kalan kişi: {josephus_optimized(n, k)}")