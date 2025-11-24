def file_append(ten_tep,vanban_moi):
    with open(ten_tep,'a',encoding='utf-8') as f:
        tep_moi = f.write('\n'+ vanban_moi)
        
    with open(ten_tep, 'r', encoding='utf-8') as f:
        noi_dung_tep = f.read()
            
        print("\n--- TOÀN BỘ NỘI DUNG TỆP SAU KHI NỐI ---")
        print(noi_dung_tep)
file_append('D:/Kì 3 (năm 2)/Thực hành KTLT/hfhd.py','\n Xuân Lâm')
