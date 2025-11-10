lst = input('nhập giá trị của list: ')
in_lst=[int(a) for a in lst.split()]
print('max list là: ' , max(in_lst))
print('min list là: ' , min(in_lst))

print('vị trí của phần từ lớn nhất là: ',in_lst.index(max(in_lst)))
print('vị trí của phần từ bé nhất là: ',in_lst.index(min(in_lst)))
