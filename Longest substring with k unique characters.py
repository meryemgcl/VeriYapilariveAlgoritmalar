def longestKSubstr(s: str, k: int) -> int:
    # Metindeki toplam benzersiz karakter sayısı k'dan azsa çözüm imkansızdır
    if len(set(s)) < k:
        return -1

    char_freq = {}
    left = 0
    max_len = -1

    # Sağ işaretçiyle pencereyi sürekli genişletiyoruz
    for right, char in enumerate(s):
        # Karakteri frekans sözlüğüne ekle veya sayısını artır
        char_freq[char] = char_freq.get(char, 0) + 1

        # Eğer benzersiz karakter sayısı k'yı aşarsa, sol tarafı daralt
        while len(char_freq) > k:
            left_char = s[left]
            char_freq[left_char] -= 1
            if char_freq[left_char] == 0:
                del char_freq[left_char]
            left += 1

        # Benzersiz karakter sayısı tam olarak k olduğunda uzunluğu güncelle
        if len(char_freq) == k:
            max_len = max(max_len, right - left + 1)

    return max_len

if __name__ == "__main__":
    s = "aabacbebebe"
    k = 3
    print(longestKSubstr(s, k))  # Çıktı: 7 ("cbebebe")