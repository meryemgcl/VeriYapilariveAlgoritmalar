def check_nearby_duplicates(data_list, k):
    """
    Dizi içerisinde k mesafesinde tekrar eden eleman olup olmadığını kontrol eder.
    """
    # k sıfır veya negatifse mesafe içinde tekrar mümkün değildir
    if k <= 0:
        return False

    # Pencere içindeki elemanları tutmak için küme (hash set)
    # Listede arama yapmak yerine set kullanmak O(1) hız sağlar
    window = set()

    for i, current_val in enumerate(data_list):
        # 1. Eleman pencerede zaten varsa, k mesafesinde bir duplicate bulduk
        if current_val in window:
            return True

        # 2. Elemanı pencereye ekle
        window.add(current_val)

        # 3. Pencere boyutu k'yı aşarsa, en eski elemanı (i - k) çıkar
        # Böylece set içerisinde her zaman son k eleman kalır
        if len(window) > k:
            old_val = data_list[i - k]
            window.remove(old_val)

    return False

# Test senaryosu
if __name__ == "__main__":
    sample_arr = [10, 5, 3, 4, 3, 5, 6]
    distance_k = 3

    if check_nearby_duplicates(sample_arr, distance_k):
        print("Sonuç: Evet (k mesafesinde tekrar var)")
    else:
        print("Sonuç: Hayır (tekrar yok)")