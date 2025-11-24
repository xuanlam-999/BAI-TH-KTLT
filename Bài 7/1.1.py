input_file = open('D:/Kì 3 (năm 2)/Thực hành KTLT/Bài 6/1.1.py')
for line in input_file:
    reversed_line = line.rstrip()[::-1]
    '''
đầu vào line
Làm sạch: rstrip()'Xin chào.\n'(đầu vào)'Xin chào.'(đầu ra)
[start:stop:step]
    '''
    print(reversed_line)
input_file.close()
