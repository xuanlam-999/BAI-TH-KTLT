S=input("Nhap chuoi: ")
for ch in S:
    if ch == "" or ch == "\t": 
        continue #Bỏ qua không in ký tự này và chuyển sang ký tự tiếp theo
    print(ch)
