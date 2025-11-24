input_file = open('D:/Kì 3 (năm 2)/Thực hành KTLT/Bài 6/1.1.py')
 
doc_file = input_file.read()
tinhkytu = len(doc_file)
tinh_word = len(doc_file.split())
tinh_line = len(doc_file.splitlines())

input_file.close() 

print(f" D:/Kì 3 (năm 2)/Thực hành KTLT/Bài 6/1.1.py")
print('Số ký tự:', tinhkytu)
print('Số từ:', tinh_word)
print('Số dòng:', tinh_line)
