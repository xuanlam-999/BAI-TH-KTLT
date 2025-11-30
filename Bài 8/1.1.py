import turtle

window = turtle.Screen()#tao mot cua so
window.bgcolor("lightgreen")#dat mau nen

painter = turtle.Turtle()
painter.fillcolor('blue')
painter.pencolor('blue')
painter.pensize(3)

def vehinhvuong(t,s):
    for i in range(4):#lap lai 4 lan
        t.forward(s)#di thang mot doan s
        t.left(90)#re trai 90 do
for i in range(1,180):
    painter.left(18)#con tro xoay trai 18 do
    vehinhvuong(painter,200)#canh dai 200pixel
