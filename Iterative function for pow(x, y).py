def power(x: float, y: int) -> float:
    # Üs sıfır ise sonuç her zaman 1'dir
    if y == 0:
        return 1.0

    # Negatif üs durumunu yönetmek için hazırlık
    is_negative = y < 0
    y = abs(y)
    
    res = 1.0
    while y > 0:
        # y tek sayı ise mevcut tabanı sonuca dahil et
        if y & 1:
            res *= x
        
        x *= x      # Tabanın karesini al
        y >>= 1     # y'yi 2'ye böl (bit kaydır)

    return 1.0 / res if is_negative else res


if __name__ == "__main__":
    print(power(3, 19))    # Pozitif üs testi
    print(power(2, -3))    # Negatif üs testi (Çıktı: 0.125)