from tkinter import *
#hàm
def NewFile(): 
    print("New File! (Tạo tệp mới!)")

def OpenFile():
    print("Open File! ")

def Exit_program():
    print("Exiting Program...")
    window.quit() # Lệnh thoát ứng dụng Tkinter

def InsText():
    print("Insert Text")

def InsPic():
    print("Insert Picture")

def About():
    print("Đây là ví dụ đơn giản về menu")



#tao window form 
window = Tk()
window.title("tk")
window.geometry("400x300")

#ạo thanh menu
menu = Menu(window)
window.config(menu=menu) # gán thanh menu vào cửa sổ gốc

# 'File'
filemenu = Menu(menu,tearoff=0) # tearoff=0 loại bỏ đường gạch đứt
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open", command=OpenFile)
filemenu.add_separator() #tạo đường kẻ ngang
filemenu.add_command(label="Exit", command=Exit_program)

# 'Insert' 
insertmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Insert", menu=insertmenu)
insertmenu.add_command(label="Text", command=InsText)
insertmenu.add_command(label="Picture", command=InsPic)

# 'Help' 
helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

window.mainloop()

