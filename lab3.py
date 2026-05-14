def string_to_int(msg):
    print("--- BÀI 1: CHUỖI -> SỐ ---")
    val = int.from_bytes(msg.encode('ascii'), byteorder='big')
    print(f"Chuỗi '{msg}' chuyển thành số: {val}\n")

def int_to_string(val):
    print("--- BÀI 2: SỐ -> CHUỖI ---")
    length = (val.bit_length() + 7) // 8
    msg = val.to_bytes(length, byteorder='big').decode('ascii')
    print(f"Số {val} chuyển thành chuỗi: '{msg}'\n")

def rsa_operation(p, q, M=None, C=None, e=None, d=None):
    print("--- BÀI 3 & 4: RSA ENCRYPT/DECRYPT ---")
    N = p * q
    phi = (p - 1) * (q - 1)
    print(f"Tham số: N = {N}, Phi(N) = {phi}")

    # Tìm khóa còn thiếu
    if e is not None and d is None:
        d = pow(e, -1, phi)
        print(f"-> Tính được Private Key (d) = {d}")
    elif d is not None and e is None:
        e = pow(d, -1, phi)
        print(f"-> Tính được Public Key (e) = {e}")

    # Mã hóa hoặc giải mã
    if M is not None:
        C_calc = pow(M, e, N)
        print(f"-> Mã hóa: Thông điệp M={M} thành Bản mã C={C_calc}")
    if C is not None:
        M_calc = pow(C, d, N)
        print(f"-> Giải mã: Bản mã C={C} thành Bản rõ M={M_calc}")
        
        # Thử dịch Bản rõ ra ASCII (dành cho Bài 4 tìm thông điệp)
        try:
            length = (M_calc.bit_length() + 7) // 8
            msg = M_calc.to_bytes(length, byteorder='big').decode('ascii')
            print(f"   (Dịch M sang Text: '{msg}')")
        except:
            pass
    print("\n")

if __name__ == "__main__":
    # Bài 1 & 2
    string_to_int("flow")
    int_to_string(14445)

    # Bài 3.1: Biết p, q, e, M -> Tìm C
    rsa_operation(p=251, q=191, e=65537, M=26729)

    # Bài 3.2: Biết p, q, d, C -> Tìm M
    rsa_operation(p=233, q=151, d=9473, C=29600)

    # Bài 4: Bẻ khóa RSA tìm Text
    rsa_operation(p=81401, q=27109, e=65537, C=412589464)