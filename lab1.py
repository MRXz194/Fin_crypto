def decimal_to_binary_and_xor(a, b):
    print(f"--- BÀI 1: NHỊ PHÂN VÀ XOR ---")
    print(f"a = {a} -> Nhị phân: {bin(a)}")
    print(f"b = {b} -> Nhị phân: {bin(b)}")
    xor_result = a ^ b
    print(f"a XOR b (Nhị phân) = {bin(xor_result)}")
    print(f"a XOR b (Thập phân) = {xor_result}\n")

def decode_ascii_array(arr, xor_key=0):
    print(f"--- BÀI 2 & 3: DỊCH MÃ ASCII ---")
    # Nếu có xor_key, nó sẽ XOR từng phần tử trước khi dịch. Nếu xor_key = 0, giữ nguyên.
    message = "".join([chr(x ^ xor_key) for x in arr])
    print(f"Thông điệp thu được: {message}\n")


if __name__ == "__main__":
    # Bài 1
    a = 123
    b = 543
    decimal_to_binary_and_xor(a, b)

    # Bài 2: Dãy ASCII không bị XOR
    A = [105, 110, 116, 114, 111, 50, 99, 114, 121, 112, 116, 111, 123, 119, 51, 
         108, 99, 48, 109, 51, 95, 116, 48, 95, 106, 48, 117, 114, 110, 51, 121, 125]
    decode_ascii_array(A, xor_key=0)

    # Bài 3: Dãy ASCII bị giấu bởi XOR (Giả sử key XOR là 10)
    B = [99, 100, 126, 120, 101, 56, 105, 120, 115, 122, 126, 101, 113, 59] # Nhập nốt dãy B của đề vào đây
    decode_ascii_array(B, xor_key=10)