import tkinter as tk
from tkinter import messagebox

# Xây dựng form hiển thị thông tin cá nhân
def create_personal_info_form():
    """Tạo cửa sổ hiển thị thông tin cá nhân."""
    root_a = tk.Toplevel()
    root_a.title("Thông tin cá nhân")
        
    info = {
        "Họ tên": "Phùng Xuân Lâm",
        "Ngày tháng năm sinh": "26/12/2006",
        "MSSV": "245752021610018",
        "Ngành học": "điều khiển và tđh"
    }
    
    # Tạo và đặt các nhãn (Label)
    row_count = 0
    for key, value in info.items():
        # Label cho Tên trường
        tk.Label(root_a, text=f"{key}:", font=('Arial',
                                                10,
                                               'bold'),
                                                anchor='w').grid(row=row_count,
                                                                 column=0,
                                                                 padx=10,
                                                                 pady=5,
                                                                 sticky='w')
        # Label cho Giá trị
        tk.Label(root_a, text=value, font=('Arial', 10), anchor='w').grid(row=row_count, column=1, padx=10, pady=5, sticky='w')
        row_count += 1
        
    # Nút đóng
    tk.Button(root_a, text="Đóng", command=root_a.destroy).grid(row=row_count, column=0, columnspan=2, pady=10)
    
#  Xây dựng form với Radio Button và Button Click
def create_radio_button_form():
    """Tạo cửa sổ với Radio Button và xử lý sự kiện nút bấm."""
    root_b = tk.Toplevel()
    root_b.title("Welcome")
    
    # Cần dùng IntVar() để lưu số tương ứng (1, 2, 3)
    radio_value = tk.IntVar(value=1) # Thiết lập giá trị mặc định là 1 (First)
    
    def on_click_me():
        """Hàm xử lý khi nhấn nút 'Click Me'."""
        selected_num = radio_value.get()
        selected_text = ""
        
        # Xác định văn bản tương ứng với số đã chọn
        if selected_num == 1:
            selected_text = "First"
        elif selected_num == 2:
            selected_text = "Second"
        elif selected_num == 3:
            selected_text = "Third"
        
        # Hiển thị thông tin đã chọn bằng messagebox
        messagebox.showinfo("Thông tin Radio Button", 
                            f"Bạn đã chọn: {selected_text} (Tương ứng với số: {selected_num})")
    

    tk.Radiobutton(root_b, text="First", variable=radio_value, value=1).pack(side=tk.LEFT, padx=5, pady=10)
    
    tk.Radiobutton(root_b, text="Second", variable=radio_value, value=2).pack(side=tk.LEFT, padx=5, pady=10)
    
    tk.Radiobutton(root_b, text="Third", variable=radio_value, value=3).pack(side=tk.LEFT, padx=5, pady=10)
    
    tk.Button(root_b, text="Click Me", command=on_click_me).pack(side=tk.LEFT, padx=15)


# Cửa sổ chính để khởi chạy các Form
if __name__ == "__main__":
    main_root = tk.Tk()
    main_root.title("Bài tập Tkinter")
    
    tk.Label(main_root, text="Chọn Form muốn hiển thị:").pack(pady=10)
    
    tk.Button(main_root, text="Mở Form Thông tin cá nhân (a)", command=create_personal_info_form).pack(pady=5)
    
    tk.Button(main_root, text="Mở Form Radio Button (b)", command=create_radio_button_form).pack(pady=5)
    
    main_root.mainloop()
