def find_bitonic_point(data):
    """
    Bitonik bir dizideki (önce artan, sonra azalan) tepe noktasını bulur.
    Zaman Karmaşıklığı: O(log n)
    """
    if not data:
        return None
        
    left, right = 0, len(data) - 1

    while left < right:
        mid = left + (right - left) // 2

        # Eğer orta eleman bir sonrakinden küçükse, tepe noktası sağ taraftadır.
        if data[mid] < data[mid + 1]:
            left = mid + 1
        # Aksi halde tepe noktası ya mid'dir ya da sol taraftadır.
        else:
            right = mid

    # Döngü bittiğinde left == right olur ve tepe noktasını işaret eder.
    return data[left]

if __name__ == "__main__":
    # Test verisi
    sample_array = [1, 2, 4, 5, 7, 8, 3]
    
    peak_value = find_bitonic_point(sample_array)
    print(f"Dizideki bitonik (tepe) noktası: {peak_value}")