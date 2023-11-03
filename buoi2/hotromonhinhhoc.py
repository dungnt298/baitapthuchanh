import tkinter as tk
from math import pi

def calculate_area(shape):
    try:
        if shape == "Hình tròn":
            radius = float(entry_radius.get())
            area = pi * radius**2
        elif shape == "Hình vuông":
            side = float(entry_side.get())
            area = side**2
        elif shape == "Tam giác":
            base = float(entry_base.get())
            height = float(entry_height.get())
            area = 0.5 * base * height

        result_label.config(text=f"Diện tích: {area:.2f}")
    except ValueError:
        result_label.config(text="Vui lòng nhập giá trị hợp lệ.")

root = tk.Tk()
root.title("Tính diện tích và chu vi")

shapes = ["Hình tròn", "Hình vuông", "Tam giác"]
selected_shape = tk.StringVar(value=shapes[0])

# Tạo các phần tử giao diện
shape_menu = tk.OptionMenu(root, selected_shape, *shapes)
shape_menu.pack()

label_radius = tk.Label(root, text="Bán kính:")
entry_radius = tk.Entry(root)
label_side = tk.Label(root, text="Cạnh:")
entry_side = tk.Entry(root)
label_base = tk.Label(root, text="Đáy:")
entry_base = tk.Entry(root)
label_height = tk.Label(root, text="Chiều cao:")
entry_height = tk.Entry(root)

calculate_button = tk.Button(root, text="Tính diện tích", command=lambda: calculate_area(selected_shape.get()))
result_label = tk.Label(root, text="")

# Đặt các phần tử giao diện lên cửa sổ
label_radius.pack()
entry_radius.pack()
label_side.pack()
entry_side.pack()
label_base.pack()
entry_base.pack()
label_height.pack()
entry_height.pack()
calculate_button.pack()
result_label.pack()

# Khởi chạy vòng lặp giao diện
root.mainloop()
