def nQueen(n: int) -> list:
    result = []
    
    # Vezirlerin çakışmasını O(1) sürede kontrol etmek için kümeler kullanıyoruz
    cols = set()          # Sütun kontrolü
    diag1 = set()         # Sol üstten sağ alta çaprazlar (row - col)
    diag2 = set()         # Sağ üstten sol alta çaprazlar (row + col)
    
    # Mevcut çözümdeki vezirlerin sütun konumlarını tutan liste
    current_board = []

    def backtrack(row: int):
        # Base case: Tüm vezirler yerleştirildiyse çözümü kaydet
        if row == n:
            result.append(list(current_board))
            return

        for col in range(n):
            # Matematiksel çapraz kontrolü (Döngüye gerek kalmadan O(1) kontrol)
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue

            # Veziri yerleştir ve durumları güncelle
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            current_board.append(col + 1)  # Soru 1 tabanlı indeks istediği için +1

            # Bir sonraki satıra geç
            backtrack(row + 1)

            # Geri izleme (Backtrack): Değişiklikleri geri al
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)
            current_board.pop()

    backtrack(0)
    return result

if __name__ == "__main__":
    n = 4
    result = nQueen(n)
    for ans in result:
        print(*ans)