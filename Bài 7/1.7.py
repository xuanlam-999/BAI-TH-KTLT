def demsodong(fname):
    with open(fname,'r',encoding='utf-8') as f:
        lines = f.readlines()
        return len(lines)

print('tổng số dòng là: ', demsodong('D:/Kì 3 (năm 2)/Thực hành KTLT/Bài 7/1.6.py'))
