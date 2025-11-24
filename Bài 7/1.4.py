def file_read_from_head(ten_file,so_dong):
    from itertools import islice
    with open(ten_file,encoding='utf-8') as f:
        for line in islice(f,so_dong):
            '''
               islice yêu cầu file trả về dòng nào đó rồi dừng lại
               và không đọc thêm dòng khác
            '''
            print(line)
file_read_from_head('D:/Kì 3 (năm 2)/Thực hành KTLT/hfhd.py',2)

