def des_sbox(ma_sv_3_so_cuoi):
    print("--- BÀI THI: DES S-BOX ---")
    x = ma_sv_3_so_cuoi % 64
    bin_str = bin(x)[2:].zfill(6) # Đảm bảo đủ 6 bit
    
    row_bin = bin_str[0] + bin_str[5]
    col_bin = bin_str[1:5]
    
    row_dec = int(row_bin, 2)
    col_dec = int(col_bin, 2)
    
    print(f"Số tính được: x = {x}")
    print(f"Chuỗi 6 bit: {bin_str}")
    print(f"-> Hàng (Row): {row_bin} (Hệ 10: {row_dec})")
    print(f"-> Cột (Col): {col_bin} (Hệ 10: {col_dec})")
    print(f"Việc của bạn: Tra bảng S1 đề cho ở Hàng {row_dec}, Cột {col_dec} lấy kết quả!\n")

def elgamal_signature(p, alpha, d, x, kE):
    print("--- BÀI THI: CHỮ KÝ ELGAMAL ---")
    # Public key CA
    beta = pow(alpha, d, p)
    print(f"1. Beta (Public Key) = {alpha}^{d} mod {p} = {beta}")
    
    # Ký (Sign)
    r = pow(alpha, kE, p)
    try:
        kE_inv = pow(kE, -1, p - 1)
        s = ((x - d * r) * kE_inv) % (p - 1)
        print(f"2. Chữ ký (r, s):")
        print(f"   r = {alpha}^{kE} mod {p} = {r}")
        print(f"   kE^-1 mod {p-1} = {kE_inv}")
        print(f"   s = ({x} - {d}*{r}) * {kE_inv} mod {p-1} = {s}")
    except Exception as e:
        print("Lỗi tìm nghịch đảo kE:", e)
    
    # Xác minh (Verify)
    LHS = pow(alpha, x, p)
    RHS = (pow(beta, r, p) * pow(r, s, p)) % p
    print(f"3. Xác minh (Verify):")
    print(f"   Vế trái (LHS) = alpha^x mod p = {LHS}")
    print(f"   Vế phải (RHS) = beta^r * r^s mod p = {RHS}")
    print(f"   Hợp lệ? -> {LHS == RHS}\n")

def diffie_hellman(p, alpha, a, b):
    print("--- BÀI THI: DIFFIE-HELLMAN ---")
    kA = pow(alpha, a, p)
    kB = pow(alpha, b, p)
    k_common = pow(kB, a, p) # Hoặc pow(kA, b, p)
    print(f"Alice public key (kA) = {alpha}^{a} mod {p} = {kA}")
    print(f"Bob public key (kB)   = {alpha}^{b} mod {p} = {kB}")
    print(f"Khóa chung (k_AB)     = {k_common}\n")

def sha1_padding(L):
    print("--- BÀI THI: SHA-1 PADDING ---")
    # L + 1 + k + 64 = 0 mod 512 => k = (512 - (L + 65) % 512) % 512
    k = (512 - (L + 65) % 512) % 512
    print(f"Độ dài ban đầu L = {L} bits")
    print(f"Số lượng bit '0' cần đệm (k) = {k}")
    print(f"Định dạng block cuối: {L} bits msg + 1 bit '1' + {k} bits '0' + 64 bits biểu diễn độ dài.\n")


if __name__ == "__main__":
    # Bài DES: Nhập 3 số cuối mã sinh viên của bạn
    des_sbox(123) 

    # Bài Elgamal: p, alpha, khóa bí mật d, thông điệp x, khóa ngẫu nhiên kE
    elgamal_signature(p=997, alpha=6, d=25, x=184, kE=185)

    # Bài Diffie-Hellman: p, alpha, khóa bí mật Alice (a), khóa bí mật Bob (b)
    diffie_hellman(p=27361, alpha=6, a=20260, b=28489)

    # Bài SHA-1: Nhập độ dài L bits của đề bài
    sha1_padding(20260)