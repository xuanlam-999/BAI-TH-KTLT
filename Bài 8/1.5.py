import tkinter as tk

def hien_ket_qua():
    selection = "Bạn đã chọn: " + str(var.get())
    label_ketqua.config(text=selection)

window = tk.Tk()
window.title("Radio Button")
window.geometry("300x200")

# biến chung để lưu giá trị của nhóm radio button
# khi chọn nút nào, biến này sẽ nhận value của nút đó
var = tk.IntVar() 

R1 = tk.Radiobutton(window, text="Lựa chọn 3", variable=var, value=1, command=hien_ket_qua)
R1.place(x=20,y=20)

R2 = tk.Radiobutton(window, text="Lựa chọn 2", variable=var, value=2, command=hien_ket_qua)
R2.place(x=20,y=80)

R3 = tk.Radiobutton(window, text="Lựa chọn 1", variable=var, value=3, command=hien_ket_qua)
R3.place(x=20,y=140)

label_ketqua = tk.Label(window)
label_ketqua.pack()

window.mainloop()
