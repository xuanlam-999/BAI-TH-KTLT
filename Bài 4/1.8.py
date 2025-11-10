
    chuoi_nhap = input("nhap tu: ")
    danh_sach_tu = chuoi_nhap.split()

    # Xử lý trường hợp danh sách rỗng
    if not danh_sach_tu:
        print("Không có từ nào được nhập.")
        return # Kết thúc hàm nếu không có từ

    #Tìm độ dài lớn nhất (VỊ TRÍ ĐÃ SỬA)
    do_dai_lon_nhat = len(max(danh_sach_tu, key=len))

    # 3. Tìm và in ra mọi từ có độ dài đó
    tu_dai_nhat = []
    for tu in danh_sach_tu:
        # Lệnh này bây giờ có thể truy cập biến do_dai_lon_nhat
        if len(tu) == do_dai_lon_nhat: 
            tu_dai_nhat.append(tu)

    print("\n--- Kết quả ---")
    print("Độ dài lớn nhất: ",do_dai_lon_nhat)
    
    #set() để loại bỏ các từ lặp lại nếu có
    tu_dai_nhat_duy_nhat = list(set(tu_dai_nhat))
    
    print(f"Từ dài nhất (hoặc các từ có cùng độ dài): {', '.join(tu_dai_nhat_duy_nhat)}")


