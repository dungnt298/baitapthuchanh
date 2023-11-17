import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

def apply_smoothing(image_path, output_path, smoothing_type='blur', kernel_size=5):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    if smoothing_type == 'blur':
        smoothed_image = cv2.blur(gray_image, (kernel_size, kernel_size))
    elif smoothing_type == 'gaussian':
        smoothed_image = cv2.GaussianBlur(gray_image, (kernel_size, kernel_size), 0)
    elif smoothing_type == 'median':
        smoothed_image = cv2.medianBlur(gray_image, kernel_size)
    else:
        print("Loại làm mịn không hỗ trợ")
        return

    cv2.imwrite(output_path, smoothed_image)

    cv2.imshow('Original Image', gray_image)
    cv2.imshow('Smoothed Image', smoothed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def browse_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")])
    if file_path:
        entry_path.delete(0, tk.END)
        entry_path.insert(0, file_path)

def apply_filter():
    input_path = entry_path.get()
    output_path = 'smoothed_image.jpg'
    smoothing_type = var.get()
    kernel_size = int(entry_kernel.get())
    apply_smoothing(input_path, output_path, smoothing_type, kernel_size)

# Tạo cửa sổ Tkinter
root = tk.Tk()
root.title("Làm mịn ảnh")

# Tạo và định vị các thành phần trong giao diện
label_path = tk.Label(root, text="Đường dẫn ảnh:")
label_path.grid(row=0, column=0, padx=10, pady=10)

entry_path = tk.Entry(root, width=50)
entry_path.grid(row=0, column=1, padx=10, pady=10)

button_browse = tk.Button(root, text="Chọn ảnh", command=browse_image)
button_browse.grid(row=0, column=2, padx=10, pady=10)

label_filter = tk.Label(root, text="Loại làm mịn:")
label_filter.grid(row=1, column=0, padx=10, pady=10)

var = tk.StringVar()
var.set("blur")

radio_blur = tk.Radiobutton(root, text="Blur", variable=var, value="blur")
radio_blur.grid(row=1, column=1)

radio_gaussian = tk.Radiobutton(root, text="Gaussian", variable=var, value="gaussian")
radio_gaussian.grid(row=1, column=2)

radio_median = tk.Radiobutton(root, text="Median", variable=var, value="median")
radio_median.grid(row=1, column=3)

label_kernel = tk.Label(root, text="Kích thước kernel:")
label_kernel.grid(row=2, column=0, padx=10, pady=10)

entry_kernel = tk.Entry(root, width=10)
entry_kernel.grid(row=2, column=1, padx=10, pady=10)

button_apply = tk.Button(root, text="Áp dụng làm mịn", command=apply_filter)
button_apply.grid(row=2, column=2, padx=10, pady=10)

# Chạy vòng lặp chính của cửa sổ Tkinter
root.mainloop()
