import tkinter as tk
window = tk.Tk()
window.title('xin chao')
window.geometry("700x500")

def click_turn_off():#cac ham xu ly skien
    window.configure(bg='blue') #doi mau nen sang xanh

def click_turn_on():
    window.configure(bg='white')#doi mau nen sang trang

turn_on = tk.Button(window,font=('Arial',12),text='Turn on', bg = 'pink',command=click_turn_on)
turn_on.place(x=200,y= 350)
#bg: mau background,fg : mau chu
turn_off = tk.Button(window,font=('Arial',12),text='Turn off', bg = 'pink',command=click_turn_off)
turn_off.place(x=450,y= 350)
