def calculate_min_reduction_cost(numbers):
    """
    Diziyi tek bir elemana indirgemek için gereken minimum maliyeti hesaplar.
    Maliyet hesabı: (n - 1) * min_element
    """
    if not numbers:
        return 0
    
    # Python'da len() ve min() operasyonlarını doğrudan kullanmak daha akıcıdır.
    # n-1 adımın her birinde en küçük elemanı kullanmak teorik olarak min maliyeti verir.
    size = len(numbers)
    min_val = min(numbers)
    
    return (size - 1) * min_val

if __name__ == "__main__":
    # Örnek veri seti
    data_points = [4, 3, 2]
    
    total_cost = calculate_min_reduction_cost(data_points)
    
    print(f"Minimum işlem maliyeti: {total_cost}")