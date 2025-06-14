# RSA 간단한 구현 예시 (작은 수로 시연용)
import math, random

# 소수 판정 함수 (작은 숫자용)
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

# 작은 랜덤 소수 두 개 선택
def generate_small_prime(lower, upper):
    while True:
        p = random.randint(lower, upper)
        if is_prime(p):
            return p

p = generate_small_prime(50, 100)
q = generate_small_prime(50, 100)
N = p * q
phi = (p-1)*(q-1)
# 공개키 지수 e 선택 (2 < e < phi, gcd(e, phi)=1)
e = 3
while math.gcd(e, phi) != 1:
    e += 2
# 개인키 지수 d 계산 (e*d ≡ 1 mod phi)
d = pow(e, -1, phi)  # python 3.8+ modular inverse
print(f"p={p}, q={q}, N={N}, e={e}, d={d}")

# 암호화/복호화 함수
def encrypt(m, e, N):
    return pow(m, e, N)
def decrypt(c, d, N):
    return pow(c, d, N)

# 테스트
message = 42
cipher = encrypt(message, e, N)
plaintext = decrypt(cipher, d, N)
print(f"원문: {message}, 암호문: {cipher}, 복호결과: {plaintext}")
