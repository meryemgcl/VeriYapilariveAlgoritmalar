def maxEqualSubarrayLength(arr: list, k: int) -> int:
    if not arr:
        return 0

    left = 0
    max_length = 0
    current_window_sum = 0
    max_elem = 0

    # Sağ işaretçi ile pencereyi sürekli genişletiyoruz
    for right in range(len(arr)):
        current_window_sum += arr[right]
        max_elem = max(max_elem, arr[right])
        
        # Mevcut pencerenin genişliği
        window_len = right - left + 1
        
        # Tüm elemanları max_elem yapmak için gereken operasyon sayısı
        # Eğer bu sayı k'dan büyükse, sol taraftan pencereyi daraltıyoruz
        while (window_len * max_elem) - current_window_sum > k:
            current_window_sum -= arr[left]
            left += 1
            window_len = right - left + 1
            # Sol eleman çıktıktan sonra yeni max_elem'i güncelliyoruz
            max_elem = max(arr[left:right + 1]) if left <= right else 0

        # Geçerli güvenli pencerenin uzunluğunu güncelle
        max_length = max(max_length, window_len)

    return max_length

if __name__ == "__main__":
    arr = [2, 4, 8, 5, 9, 6]
    k = 6

    print(maxEqualSubarrayLength(arr, k))  # Çıktı: 3  ([8, 5, 9] alt dizisi için k=5 harcanarak hepsi 9 yapılır)