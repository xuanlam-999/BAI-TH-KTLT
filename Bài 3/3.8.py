import math
def Tinh(R):

 if R<=0:
     print("xin hay nhap R la so duong")
     return
 chu_vi= 2*math.pi*R;
 dien_tich= math.pi*R*R;
 print("chu vi bang: ",chu_vi)
 print("dien tich bang: ",dien_tich)

R = int(input("Nhập bán kính hình tròn: "))
Tinh(5)
#cần tính khi R bằng mấy thì thay chỗ số 5
