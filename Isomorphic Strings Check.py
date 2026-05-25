def areIsomorphic(s1: str, s2: str) -> bool:
    # Uzunluklar eşit değilse zaten izomorfik olamazlar
    if len(s1) != len(s2):
        return False

    # s1 -> s2 ve s2 -> s1 yönündeki eşleşmeleri tutacak sözlükler
    map_s1_to_s2 = {}
    map_s2_to_s1 = {}

    for c1, c2 in zip(s1, s2):
        # s1'deki karakter daha önce eşleştiyse, yeni karakterle tutarlı mı kontrol et
        if c1 in map_s1_to_s2 and map_s1_to_s2[c1] != c2:
            return False
            
        # s2'deki karakter daha önce eşleştiyse, yeni karakterle tutarlı mı kontrol et
        if c2 in map_s2_to_s1 and map_s2_to_s1[c2] != c1:
            return False

        # Karakterleri karşılıklı olarak haritalandır
        map_s1_to_s2[c1] = c2
        map_s2_to_s1[c2] = c1

    return True

if __name__ == "__main__":
    s1 = "aab"
    s2 = "xxy"

    # Pythonic ve temiz bir şekilde sonucu yazdırıyoruz
    print(str(areIsomorphic(s1, s2)).lower())