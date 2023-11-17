import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

def apply_edge_detection(image_path, output_path, low_threshold=50, high_threshold=150):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Áp dụng phương pháp Canny để tách biên ảnh
    edges = cv2.Canny(image, low_threshold, high_threshold)

    # Hiển thị và lưu ảnh kết quả
    cv2.imshow('Original Image', image)
    cv2.imshow('Edge Detection', edges)
    cv2.imwrite(output_path, edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def browse_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")])
    if file_path:
        entry_path.delete(0, tk.END)
        entry_path.insert(0, file_path)

def apply_edge_detection_gui():
    input_path = entry_path.get()
    output_path = 'edge_detected_image.jpg'
    low_threshold = int(entry_low_threshold.get())
    high_threshold = int(entry_high_threshold.get())
    apply_edge_detection(input_path, output_path, low_threshold, high_threshold)

# Tạo cửa sổ Tkinter
root = tk.Tk()
root.title("Tách biên ảnh")

# Tạo và định vị các thành phần trong giao diện
label_path = tk.Label(root, text="Đường dẫn ảnh:")
label_path.grid(row=0, column=0, padx=10, pady=10)

entry_path = tk.Entry(root, width=50)
entry_path.grid(row=0, column=1, padx=10, pady=10)

button_browse = tk.Button(root, text="Chọn ảnh", command=browse_image)
button_browse.grid(row=0, column=2, padx=10, pady=10)

label_low_threshold = tk.Label(root, text="Ngưỡng thấp:")
label_low_threshold.grid(row=1, column=0, padx=10, pady=10)

entry_low_threshold = tk.Entry(root, width=10)
entry_low_threshold.grid(row=1, column=1, padx=10, pady=10)

label_high_threshold = tk.Label(root, text="Ngưỡng cao:")
label_high_threshold.grid(row=1, column=2, padx=10, pady=10)

entry_high_threshold = tk.Entry(root, width=10)
entry_high_threshold.grid(row=1, column=3, padx=10, pady=10)

button_apply = tk.Button(root, text="Tách biên ảnh", command=apply_edge_detection_gui)
button_apply.grid(row=2, column=1, padx=10, pady=10)

# Chạy vòng lặp chính của cửa sổ Tkinter
root.mainloop()
