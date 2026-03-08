def find_first_repeating(arr):
    """
    Dizideki ilk tekrar eden elemanı ve indisini döndürür.
    Zaman Karmaşıklığı: O(n), Alan Karmaşıklığı: O(n)
    """
    if not arr:
        return -1, None

    seen = {} # Eleman: İlk görüldüğü indis
    first_repeat_idx = float('inf')
    
    # Elemanları ve indislerini bir kez tara
    for i, val in enumerate(arr):
        if val in seen:
            # Eğer eleman daha önce görüldüyse, 
            # bu elemanın İLK görülme indisini aday olarak belirle.
            first_repeat_idx = min(first_repeat_idx, seen[val])
        else:
            # Elemanı ilk kez gördüğümüzde indisiyle kaydet
            seen[val] = i

    if first_repeat_idx == float('inf'):
        return -1, None
    
    return first_repeat_idx, arr[first_repeat_idx]

# --- EKLENTİ: Tekrar Analizi ---
def get_repetition_stats(arr):
    """Ekstra özellik: Tüm tekrar edenlerin listesini ve sayılarını verir."""
    counts = {}
    for x in arr:
        counts[x] = counts.get(x, 0) + 1
    
    # Sadece birden fazla olanları filtrele
    duplicates = {k: v for k, v in counts.items() if v > 1}
    return duplicates

if __name__ == "__main__":
    data = [10, 5, 3, 4, 3, 5, 6]
    
    idx, value = find_first_repeating(data)
    
    if idx != -1:
        print(f"🚀 İlk tekrar eden eleman: {value} (İndis: {idx})")
        
        # Eklenti kullanımı
        stats = get_repetition_stats(data)
        print(f"📊 Tekrar istatistikleri: {stats}")
    else:
        print("❌ Tekrar eden eleman bulunamadı.")