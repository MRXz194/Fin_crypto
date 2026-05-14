def modular_calc():
    print("--- CÔNG CỤ TÍNH TOÁN MODULO ---")
    print("1. Tính a % n")
    print("2. Tính (a^b) % n (Lũy thừa nhanh)")
    print("3. Tính nghịch đảo modulo (a^-1 mod n)")
    
    choice = input("\nChọn phép tính (1/2/3): ")
    
    if choice == '1':
        a = int(input("Nhập a: "))
        n = int(input("Nhập n: "))
        print(f"=> {a} mod {n} = {a % n}")
        
    elif choice == '2':
        a = int(input("Nhập cơ số a: "))
        b = int(input("Nhập số mũ b: "))
        n = int(input("Nhập modulo n: "))
        # pow(a, b, n) là hàm lũy thừa nhanh có sẵn trong Python
        result = pow(a, b, n)
        print(f"=> ({a}^{b}) mod {n} = {result}")
        
    elif choice == '3':
        a = int(input("Nhập a: "))
        n = int(input("Nhập n: "))
        try:
            # pow(a, -1, n) tính nghịch đảo modulo trong Python 3.8+
            inv = pow(a, -1, n)
            print(f"=> {a}^-1 mod {n} = {inv}")
        except ValueError:
            print(f"=> Không tồn tại nghịch đảo của {a} mod {n} (do gcd({a}, {n}) != 1)")

if __name__ == "__main__":
    modular_calc()
