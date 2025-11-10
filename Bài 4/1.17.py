try:
    n_str = input('Nhập số nguyên n: ')

    n = int(n_str)
    
except ValueError:
    
    print('vui long nhap so nguyen.')
    
    exit()
if n<1:
    print('hãy nhập số nguyên dương')
else:
    
    for i in range (1,n):
        print(i)
    
