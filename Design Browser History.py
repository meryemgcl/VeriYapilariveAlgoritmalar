class BrowserHistory:
    def __init__(self, homepage: str): 
        # Ana geçmişi tek bir liste (stack) üzerinde tutuyoruz
        self.history = [homepage]
        # Şu an hangi sayfada olduğumuzu belirten bir işaretçi (pointer)
        self.current_idx = 0

    def visit(self, url: str): 
        # Yeni bir sayfa ziyaret edildiğinde, mevcut indeksin ilerisinde 
        # kalan tüm "forward" geçmişini tek hamlede siliyoruz.
        self.history = self.history[:self.current_idx + 1]
        self.history.append(url)
        self.current_idx += 1

    def back(self, steps: int) -> str: 
        # Geriye gidebileceğimiz maksimum adım sayısı ile istenen adımı kıyaslıyoruz
        # Döngü kullanmadan O(1) sürede yeni indeksi belirliyoruz
        self.current_idx = max(0, self.current_idx - steps)
        return self.history[self.current_idx]

    def forward(self, steps: int) -> str: 
        # İleriye gidebileceğimiz maksimum sınır dizinin son elemanıdır
        self.current_idx = min(len(self.history) - 1, self.current_idx + steps)
        return self.history[self.current_idx]
      
if __name__ == "__main__": 
    # Test Senaryosu
    obj = BrowserHistory("gfg.org")
    obj.visit("google.com")
    obj.visit("facebook.com")
    obj.visit("youtube.com")

    print(obj.back(1))     # Çıktı: facebook.com
    print(obj.back(1))     # Çıktı: google.com
    print(obj.forward(1))  # Çıktı: facebook.com

    obj.visit("linkedin.com")

    print(obj.forward(2))  # Çıktı: linkedin.com (İleri geçmiş silindiği için yerinde kalır)
    print(obj.back(2))     # Çıktı: google.com
    print(obj.back(7))     # Çıktı: gfg.org (Sınırı aşsa da ana sayfada durur)