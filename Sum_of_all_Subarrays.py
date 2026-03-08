def get_total_subarray_sum(data):
    """
    Tüm alt dizilerin toplamını O(n) zaman karmaşıklığı ile hesaplar.
    Matematiksel yaklaşım: Her eleman (i+1) * (n-i) kez toplama dahil olur.
    """
    n = len(data)
    total_sum = 0
    
    for i, value in enumerate(data):
        # i. indisteki eleman (i + 1) * (n - i) tane alt dizide bulunur.
        # Bu formül, elemanın toplam sonuca ne kadar 'katkı' sağladığını verir.
        count = (i + 1) * (n - i)
        total_sum += value * count
        
    return total_sum

if __name__ == "__main__":
    arr = [1, 4, 5, 3, 2]
    
    # Sonucu ekrana yazdır
    result = get_total_subarray_sum(arr)
    print(f"Alt dizilerin toplamı: {result}")