def a51_exam_format(X_str, Y_str, Z_str, cycles=3):
    print("--- BÀI THI: A5/1 STREAM CIPHER ---")
    print(f"Initial state:")
    print(f"X = ({X_str})")
    print(f"Y = ({Y_str})")
    print(f"Z = ({Z_str})\n")
    print("-" * 50)

    # Chuyển chuỗi thành mảng list để dễ thao tác
    X = [int(b) for b in X_str]
    Y = [int(b) for b in Y_str]
    Z = [int(b) for b in Z_str]
    
    keystream = []
    
    for i in range(cycles):
        print(f"**Cycle {i}:**")
        
        # 1. Đọc clock bits
        x8, y10, z10 = X[8], Y[10], Z[10]
        print(f"* Read clock bits: X[8]={x8}, Y[10]={y10}, Z[10]={z10}")
        
        # 2. Tính Majority
        maj = 1 if (x8 + y10 + z10) >= 2 else 0
        print(f"* Compute Majority: Maj({x8}, {y10}, {z10}) = {maj}")
        
        # 3. Phân loại Action
        clocked = []
        skipped = []
        if x8 == maj: clocked.append("X")
        else: skipped.append("X")
        if y10 == maj: clocked.append("Y")
        else: skipped.append("Y")
        if z10 == maj: clocked.append("Z")
        else: skipped.append("Z")
        print(f"* Action: {', '.join(clocked)} clocked (shifted); {', '.join(skipped)} skipped.")
        
        # 4. Tính Output Bit
        out_bit = X[18] ^ Y[21] ^ Z[22]
        keystream.append(out_bit)
        print(f"* Output Bit = X[18] ⊕ Y[21] ⊕ Z[22] = {X[18]} ⊕ {Y[21]} ⊕ {Z[22]} = {out_bit}")
        
        # 5. Tính Feedback và Dịch bit (Shift)
        fb_strs = []
        if x8 == maj:
            fb_x = X[13] ^ X[16] ^ X[17] ^ X[18]
            fb_strs.append(f"fb_X = X[13]⊕X[16]⊕X[17]⊕X[18] = {X[13]}⊕{X[16]}⊕{X[17]}⊕{X[18]} = {fb_x}")
            X = [fb_x] + X[:-1] # Dịch phải 1, nhét fb vào đầu
        
        if y10 == maj:
            fb_y = Y[20] ^ Y[21]
            fb_strs.append(f"fb_Y = Y[20]⊕Y[21] = {Y[20]}⊕{Y[21]} = {fb_y}")
            Y = [fb_y] + Y[:-1]
            
        if z10 == maj:
            fb_z = Z[7] ^ Z[20] ^ Z[21] ^ Z[22]
            fb_strs.append(f"fb_Z = Z[7]⊕Z[20]⊕Z[21]⊕Z[22] = {Z[7]}⊕{Z[20]}⊕{Z[21]}⊕{Z[22]} = {fb_z}")
            Z = [fb_z] + Z[:-1]
            
        print(f"* Compute Feedback: {', '.join(fb_strs)}")
        
        # 6. In ra trạng thái mới
        print("* New State:")
        print(f"  X_{i+1} = ({''.join(map(str, X))})")
        print(f"  Y_{i+1} = ({''.join(map(str, Y))})")
        print(f"  Z_{i+1} = ({''.join(map(str, Z))})")
        print("-" * 50)

    print(f"**Result:** Keystream bits produced: {', '.join(map(str, keystream))}\n")


if __name__ == "__main__":
 
    X_input = "0110011001100110011"
    Y_input = "1101110111011101110111"
    Z_input = "11010001101000110100001"

    
    a51_exam_format(X_input, Y_input, Z_input, cycles=3)