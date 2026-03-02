import time

def solve_hanoi(n, from_rod, to_rod, aux_rod):
    """
    Hanoi Kuleleri çözümünü yazdıran ve toplam hamle sayısını dönen fonksiyon.
    """
    moves = 0

    def hanoi_recursive(n, source, target, spare):
        nonlocal moves
        if n > 0:
            # 1. n-1 diski yardımcı çubuğa taşı
            hanoi_recursive(n - 1, source, spare, target)
            
            # 2. En büyük diski hedefe taşı
            moves += 1
            print(f"Hamle {moves:2}: Disk {n} | {source} -> {target}")
            
            # 3. n-1 diski yardımcı çubuktan hedefe taşı
            hanoi_recursive(n - 1, spare, target, source)

    # Başlangıç zamanını tut
    start_time = time.perf_counter()
    
    hanoi_recursive(n, from_rod, to_rod, aux_rod)
    
    end_time = time.perf_counter()
    
    print("-" * 30)
    print(f"Toplam Hamle Sayısı: {moves} (2^{n}-1)")
    print(f"İşlem Süresi: {end_time - start_time:.6f} saniye")

if __name__ == "__main__":
    # n = Disk sayısı
    n_disks = 3
    solve_hanoi(n_disks, 'A', 'C', 'B')