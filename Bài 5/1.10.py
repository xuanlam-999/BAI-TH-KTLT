# Import hàm bubbleSort từ module sorting_algorithms
from sorting_algorithms import bubbleSort

def input_list():
    """Nhập danh sách các số nguyên từ bàn phím."""
    while True:
        try:
            # Nhập số lượng phần tử N
            n = int(input("Nhập số lượng phần tử N: "))
            if n <= 0:
                print("N phải là số nguyên dương. Vui lòng nhập lại.")
                continue
            
            # Nhập N phần tử, cách nhau bởi dấu cách hoặc xuống dòng
            print(f"Nhập {n} phần tử của danh sách, cách nhau bởi dấu cách:")
            
            # Đọc một dòng, tách thành các chuỗi và chuyển thành số nguyên
            nlist = list(map(int, input().split()[:n]))
            
            # Kiểm tra xem đã nhập đủ N phần tử chưa
            if len(nlist) != n:
                 print(f"Bạn đã nhập {len(nlist)} phần tử, cần nhập đủ {n} phần tử. Vui lòng nhập lại.")
                 continue
                 
            return nlist
            
        except ValueError:
            print("Lỗi: Đầu vào không hợp lệ. Vui lòng chỉ nhập các số nguyên.")
        except Exception as e:
            print(f"Đã xảy ra lỗi: {e}")

# --- Chương trình chính ---
if __name__ == "__main__":
    
    print("--- CHƯƠNG TRÌNH SẮP XẾP NỔI BỌT ---")
    
    # 1. Nhập danh sách từ người dùng
    my_list = input_list()
    
    print(f"\nDanh sách ban đầu: {my_list}")
    
    # 2. Gọi hàm bubbleSort từ module đã import
    # Hàm sắp xếp này hoạt động trực tiếp (in-place) trên my_list
    bubbleSort(my_list)
    
    # 3. In ra kết quả
    print(f"Danh sách sau khi sắp xếp (Bubble Sort): {my_list}")
