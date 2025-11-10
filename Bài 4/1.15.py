tu_tieng_anh = input('nhập từ tiếng anh viết tách nhau bằng dấu cách: ')

tutienganh_chuoi = tu_tieng_anh.split()

sap_xep = sorted(tutienganh_chuoi)

for tu in sap_xep:
    print(tu)
