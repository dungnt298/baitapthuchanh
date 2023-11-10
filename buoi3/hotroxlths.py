import tkinter as tk
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def xu_ly_tin_hieu(so_nhap_vao):
    try:
        so_nhap_vao = [float(x) for x in so_nhap_vao.split(",")]
        ket_qua = sum(so_nhap_vao)
        ket_qua_label.config(text=f"Kết quả: {ket_qua}")
    except ValueError:
        ket_qua_label.config(text="Nhập không hợp lệ")

def tinh_trung_binh(so_nhap_vao):
    try:
        so_nhap_vao = [float(x) for x in so_nhap_vao.split(",")]
        trung_binh = sum(so_nhap_vao) / len(so_nhap_vao)
        ket_qua_label.config(text=f"Trung bình: {trung_binh}")
    except ValueError:
        ket_qua_label.config(text="Nhập không hợp lệ")

def tinh_tan_suat(so_nhap_vao):
    try:
        so_nhap_vao = [float(x) for x in so_nhap_vao.split(",")]
        tan_suat = Counter(so_nhap_vao)
        ket_qua_label.config(text=f"Tần suất: {tan_suat}")
    except ValueError:
        ket_qua_label.config(text="Nhập không hợp lệ")

def ve_bieu_do(so_nhap_vao):
    try:
        so_nhap_vao = [float(x) for x in so_nhap_vao.split(",")]
        plt.figure(figsize=(5, 4))
        plt.plot(so_nhap_vao)
        plt.title("Biểu đồ tín hiệu số")
        plt.xlabel("Thời gian")
        plt.ylabel("Giá trị")
        canvas = FigureCanvasTkAgg(plt.gcf(), master=root)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    except ValueError:
        ket_qua_label.config(text="Nhập không hợp lệ")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Xử Lý Tín Hiệu Số")

# Tạo ô nhập liệu
nhap_lieu_entry = tk.Entry(root)
nhap_lieu_entry.pack(pady=10)

# Tạo nút xử lý
xu_ly_button = tk.Button(root, text="Xử Lý", command=lambda: xu_ly_tin_hieu(nhap_lieu_entry.get()))
xu_ly_button.pack()

# Tạo nút tính trung bình
trung_binh_button = tk.Button(root, text="Tính Trung Bình", command=lambda: tinh_trung_binh(nhap_lieu_entry.get()))
trung_binh_button.pack()

# Tạo nút tính tần suất
tan_suat_button = tk.Button(root, text="Tính Tần Suất", command=lambda: tinh_tan_suat(nhap_lieu_entry.get()))
tan_suat_button.pack()

# Tạo nút vẽ biểu đồ
ve_bieu_do_button = tk.Button(root, text="Vẽ Biểu Đồ", command=lambda: ve_bieu_do(nhap_lieu_entry.get()))
ve_bieu_do_button.pack()

# Hiển thị kết quả
ket_qua_label = tk.Label(root, text="Kết quả: ")
ket_qua_label.pack(pady=10)

# Bắt đầu vòng lặp sự kiện
root.mainloop()
