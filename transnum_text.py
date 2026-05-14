print("\n--- BÀI PHỤ: DỊCH ASCII (CHỮ <-> SỐ) ---")

# 1. TỪ CHỮ SANG SỐ (Dùng cho Exercise 1: chữ "flow")
text_input = "flow"
try:
    num_output = int.from_bytes(text_input.encode('ascii'), byteorder='big')
    print(f"Chữ '{text_input}' chuyển thành Số: {num_output}")
except Exception as e:
    print("Lỗi:", e)

# 2. TỪ SỐ SANG CHỮ (Dùng cho Exercise 2: số 14445, hoặc Ex 4 sau khi giải mã RSA)
# Thay số đề cho vào đây
number_input = 14445 
try:
    byte_len = (number_input.bit_length() + 7) // 8
    text_output = number_input.to_bytes(byte_len, byteorder='big').decode('ascii')
    print(f"Số {number_input} dịch ra Chữ là: '{text_output}'")
except Exception as e:
    print("Lỗi (số không hợp lệ):", e)