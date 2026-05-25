from collections import deque

def rearrangeQueue(q: deque):
    if not q:
        return

    half_size = len(q) // 2
    
    # 1. ADIM: Kuyruğun ilk yarısını geçici bir hafızaya (kuyruğa) alıyoruz
    first_half = deque()
    for _ in range(half_size):
        first_half.append(q.popleft())

    # 2. ADIM: Bir ilk yarıdan bir ikinci yarıdan çekerek (interleave) ana kuyruğa ekle
    # q içinde şu an sadece ikinci yarı kaldı
    while first_half:
        q.append(first_half.popleft())  # İlk yarıdan eleman ekle
        q.append(q.popleft())           # İkinci yarıdan eleman ekle (kuyruğun arkasına at)

if __name__ == "__main__":
    q = deque([1, 2, 3, 4, 5, 6])  # Daha net görmek için 6 elemanlı örnek
    rearrangeQueue(q)
    
    # Sonucu Pythonic ve temiz bir şekilde yazdırıyoruz
    print(*q)  # Çıktı: 1 4 2 5 3 6