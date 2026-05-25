from typing import List

def minSoldiers(arr: List[int], k: int) -> int:
    if not arr or k <= 0:
        return 0
        
    costs = []
    
    # Her birliğin k'nın katı olması için gereken asker sayısını hesapla
    for num in arr:
        remainder = num % k
        if remainder == 0:
            costs.append(0)
        else:
            costs.append(k - remainder)
            
    # En az kaç birliğin şanslı (k'nın katı) olması gerektiğini bul
    needed_troops = (len(arr) + 1) // 2
    
    # Maliyetleri küçükten büyüye sırala (Açgözlü yaklaşım)
    costs.sort()
    
    # En ucuz maliyetli olanların toplamını döndür
    return sum(costs[:needed_troops])

if __name__ == '__main__':
    arr = [3, 5, 6, 7, 9, 11]
    k = 4
    print(minSoldiers(arr, k))  # Çıktı: 3