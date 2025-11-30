import tkinter as tk
import random

# Danh sách các màu có thể có.
colours = ['Red','Blue','Green','Pink','Black',
           'Yellow','Orange','White','Purple','Brown']

timeleft = 120 
score = 0

def startGame(event):
    
    global timeleft
    if timeleft == 120:
        countdown()
        nextColour()
        # Chuyển focus vào ô nhập liệu ngay khi bắt đầu
        e.focus_set() 

def nextColour():

    global score
    global timeleft

    if timeleft > 0:#chưa hết time
        # Lấy văn bản người dùng nhập và chuyển sang chữ thường
        input_text = e.get().lower()
        
        # Lấy tên màu hiện tại (là màu hiển thị trên text)
        actual_colour_name = colours[1].lower() 
        
        # Kiểm tra xem người dùng đã nhập liệu chưa
        if input_text:
            # So sánh text người dùng nhập VỚI màu của chữ hiện tại
            if input_text == actual_colour_name:               
                score += 2#nếu đoán đúng
            else:
                score -= 1#nếu đoán sai
        
        # Xóa nội dung trong ô nhập liệu
        e.delete(0, tk.END)
        
        # Xáo trộn danh sách để tạo ra cặp màu mới
        random.shuffle(colours)
        
        '''Cấu hình lại Label:
        dùng colours[1] (mục tiêu)
        dùng colours[0] (cái cần bỏ qua)'''
        label.config(fg = str(colours[1]), text = str(colours[0]))
        
        # Cập nhật điểm số
        scoreLabel.config(text = "Score: " + str(score))

def countdown():
    """Hàm đếm ngược thời gian."""
    global timeleft
    
    # Nếu trò chơi đang diễn ra
    if timeleft > 0:
        # Giảm thời gian
        timeleft -= 1
        
        # Cập nhật nhãn thời gian
        timeLabel.config(text = "Time left: " + str(timeleft))
        
        # Chạy lại hàm sau 1000ms (1 giây)
        timeLabel.after(1000, countdown)
    else:
        # Khi hết giờ
        label.config(text="HẾT GIỜ!", fg="red")
        e.config(state='disabled') # Vô hiệu hóa ô nhập liệu
        messagebox.showinfo("Game Over", f"Điểm số cuối cùng của bạn là: {score}")

'''thiết lấp giao diện'''
root = tk.Tk()
root.title("Học màu Tiếng Anh")
root.geometry("400x250") 

# Thêm Nhãn hướng dẫn
instructions = tk.Label(root, 
                        text = "Gõ TÊN MÀU của chữ, KHÔNG phải nội dung chữ!\n(Nhấn Enter để BẮT ĐẦU)",
                        font = ('Helvetica', 12),
                        fg="darkgreen")
instructions.pack(pady=10)

# Thêm Nhãn điểm số
scoreLabel = tk.Label(root, text = "Score: 0",
                      font = ('Helvetica', 14, 'bold'), fg="blue")
scoreLabel.pack()

# Thêm Nhãn thời gian còn lại
timeLabel = tk.Label(root, text = f"Time left: {timeleft}", 
                     font = ('Helvetica', 14))
timeLabel.pack()

# Thêm Label hiển thị màu sắc (font lớn)
label = tk.Label(root, text="BẮT ĐẦU!", font = ('Helvetica', 60, 'bold'))
label.pack(pady=10)

# Thêm ô nhập liệu
e = tk.Entry(root, width=20, font = ('Helvetica', 16), justify='center')
e.pack(pady=5)

''' 7. Liên kết phím Enter: Bắt đầu game và kiểm tra đáp án
# Khi trò chơi chưa bắt đầu, Enter gọi startGame
# Khi trò chơi đã bắt đầu, Enter gọi nextColour (xử lý logic điểm)'''
root.bind('<Return>', lambda event: startGame(event) if timeleft == 120 else nextColour())

# Đặt focus ban đầu vào ô nhập liệu
e.focus_set()

root.mainloop()
