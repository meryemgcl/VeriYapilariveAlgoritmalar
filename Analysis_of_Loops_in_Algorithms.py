from itertools import chain

def process_data_ranges(m_limit, n_limit, step_size):
    """
    İki farklı veri aralığını ardışık olarak işleyen yardımcı fonksiyon.
    Karmaşıklık: O(m + n)
    """
    
    # m ve n aralıklarını tek bir iterator üzerinde birleştiriyoruz.
    # Bu yöntem, bellekte iki ayrı liste tutmak yerine akış (stream) oluşturur.
    target_generator = chain(
        range(1, m_limit + 1, step_size), 
        range(1, n_limit + 1, step_size)
    )

    for value in target_generator:
        # Buraya O(1) maliyetli asıl mantık gelecek
        _ = value * 2  # Örnek işlem

# Kullanım örneği
if __name__ == "__main__":
    m, n, c = 100, 150, 5
    process_data_ranges(m, n, c)