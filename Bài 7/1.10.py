def tim_tu_dai_nhat(ten_file):
    
    with open(ten_file, 'r', encoding='utf-8') as f:
        noi_dung = f.read()
    
    # Hàm split(): cắt chuỗi tại các khoảng trắng để tạo thành danh sách từ
    danh_sach_tu = noi_dung.split()
    
    if len(danh_sach_tu) == 0:
        return " file rỗng "
    
    do_dai_max = 0
    for tu in danh_sach_tu:
        if len(tu) > do_dai_max:
            do_dai_max = len(tu)
            
    ket_qua = []
    for tu in danh_sach_tu:
        if len(tu) == do_dai_max:
            ket_qua.append(tu)
            
    return ket_qua

danh_sach_kq = tim_tu_dai_nhat('D:/Kì 3 (năm 2)/Thực hành KTLT/hfhd.txt')

print(f"Những từ dài nhất là: {danh_sach_kq}")
