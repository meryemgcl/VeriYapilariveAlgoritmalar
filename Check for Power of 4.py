def isPowerOfFour(n: int) -> bool:
    # Sayı pozitif olmalı, 2'nin kuvveti olmalı ve 3'e bölümünden kalan 1 olmalı
    return n > 0 and (n & (n - 1)) == 0 and n % 3 == 1

if __name__ == "__main__":
    n = 64
    print(str(isPowerOfFour(n)).lower())