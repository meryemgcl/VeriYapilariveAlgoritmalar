def intersect(a: list, b: list) -> list:
    # b listesini set'e çevirerek arama hızını O(1) yapıyoruz
    set_b = set(b)
    
    # Elemanların tekrarlanmaması için set comprehension kullanıp liste olarak döndürüyoruz
    return list({item for item in a if item in set_b})

if __name__ == "__main__":
    a = [1, 2, 3, 2, 1]
    b = [3, 2, 2, 3, 3, 2]

    res = intersect(a, b)
    print(*res)