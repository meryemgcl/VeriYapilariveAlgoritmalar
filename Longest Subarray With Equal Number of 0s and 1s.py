def maxLen(arr: list) -> int:
    # Kümülatif toplamların ilk görüldüğü indeksleri tutan sözlük
    # En başta toplam 0'dır ve indeks -1 olarak kabul edilir
    prefix_sums = {0: -1}
    
    current_sum = 0
    max_length = 0

    for index, val in enumerate(arr):
        # 0'ı -1, 1'i +1 olarak kabul edip kümülatif toplamı güncelliyoruz
        current_sum += -1 if val == 0 else 1

        # Eğer bu kümülatif toplamı daha önce gördüysek, 
        # aradaki alt dizinin toplamı 0'dır (0 ve 1 sayıları eşittir)
        if current_sum in prefix_sums:
            prev_index = prefix_sums[current_sum]
            max_length = max(max_length, index - prev_index)
        else:
            # İlk defa karşılaşılan toplamı indeksiyle kaydet
            prefix_sums[current_sum] = index

    return max_length

if __name__ == "__main__":
    array = [1, 0, 0, 1, 0, 1, 1]
    print(maxLen(array))  # Çıktı: 6  ([0, 0, 1, 0, 1, 1] veya [1, 0, 0, 1, 0, 1])