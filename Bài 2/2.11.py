from math import sqrt
a=int(input("nhap gia tri cua a: "))
b=int(input("nhap gia tri cua b: "))
c=int(input("nhap gia tri cua c: "))
if a==0:
   if b==0:
       print("phuong trinh vo nghiem")
   else:
       x=-c/b
       print("phuong trinh co nghiem",x)
else:
   delta=b*b-4*a*c
   if delta<0:
       print("phuong trinh vo nghiem")
   elif delta == 0:
       x=-b/(2*a)
       print("phuong trinh co nghiem la ",x)
   else:
       x1=(-b+ sqrt(delta))/(2*a)
       x2=(-b- sqrt(delta))/(2*a)
       print("phuong trinh co nghiem x1 la ",x1)
       print("phuong trinh co nghiem x2 la ",x2)
