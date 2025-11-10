chuoigoc = input('nhap chuoi: ')
chuoimoi = ""
for kytu in chuoigoc:
    if kytu.isdigit(): #nếu là số thì bỏ qua
        continue
    else:
        chuoimoi += kytu
print('chuoi sau khi loai bo so: ',chuoimoi)
