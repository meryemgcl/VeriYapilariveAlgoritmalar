def commonElements(a: list, b: list, c: list) -> list:
    # Set kesişimi ile 3 listede de ortak olan elemanları anında buluyoruz.
    # Sıralı gelme zorunluluğu yoktur, karmaşık döngüleri tamamen yok eder.
    common = set(a) & set(b) & set(c)
    
    # Sonucu sıralı bir liste olarak döndürüyoruz
    return sorted(list(common))

if __name__ == "__main__":
    a = [1, 5, 10, 20, 30]
    b = [5, 13, 15, 20]
    c = [5, 20]

    common = commonElements(a, b, c)
    
    # Boş liste kontrolünü Pythonic bir yöntemle (if not) yapıyoruz
    if not common:
        print("[]")
    else:
        print(*common)