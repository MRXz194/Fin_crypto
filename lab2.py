import math

def find_gcd(a, b):
    print(f"--- BÀI 1: GCD ---")
    print(f"Ước chung lớn nhất của {a} và {b} là: {math.gcd(a, b)}\n")

def find_coprime_pairs(arr):
    print(f"--- BÀI 2: CÁC CẶP NGUYÊN TỐ CÙNG NHAU (GCD = 1) ---")
    pairs = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if math.gcd(arr[i], arr[j]) == 1:
                pairs.append((arr[i], arr[j]))
    print(f"Tìm thấy {len(pairs)} cặp: {pairs}\n")

def square_and_multiply(base, exponent, mod):
    print(f"--- BÀI 3: SQUARE AND MULTIPLY (Tính {base}^{exponent} mod {mod}) ---")
    binary_exp = bin(exponent)[2:] # Bỏ tiền tố '0b'
    print(f"Số mũ {exponent} dạng nhị phân: {binary_exp}")
    
    z = 1
    print(f"{'Bit':<5} | {'Square (z = z^2 mod m)':<30} | {'Multiply (z = z * x mod m)'}")
    print("-" * 75)
    for bit in binary_exp:
        sq_z = (z * z) % mod
        if bit == '1':
            mul_z = (sq_z * base) % mod
            print(f"{bit:<5} | z = {z}^2 mod {mod} = {sq_z:<13} | z = {sq_z} * {base} mod {mod} = {mul_z}")
            z = mul_z
        else:
            print(f"{bit:<5} | z = {z}^2 mod {mod} = {sq_z:<13} | Bỏ qua")
            z = sq_z
    print(f"KẾT QUẢ CUỐI CÙNG: {z}\n")

def multiplicative_inverse(x, N):
    print(f"--- BÀI 4: TÌM NGHỊCH ĐẢO MODULO ---")
    try:
        inv = pow(x, -1, N)
        print(f"Nghịch đảo của {x} modulo {N} là: {inv}\n")
    except ValueError:
        print(f"Không tồn tại nghịch đảo của {x} modulo {N}\n")


if __name__ == "__main__":
    # Bài 1
    find_gcd(52698, 61430)

    # Bài 2
    A = [290345, 218585, 143231, 164172, 155768, 423151, 239707, 153544, 287390, 480837]
    find_coprime_pairs(A)

    # Bài 3
    square_and_multiply(85, 625, 7) # Tính 85^625 mod 7

    # Bài 4
    multiplicative_inverse(65537, 35256)