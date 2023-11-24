import cv2
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog


def enhance_image(image_path, alpha=1.5, beta=30):
    # Đọc ảnh từ đường dẫn
    img = cv2.imread(image_path)

    # Kiểm tra xem ảnh có đọc được hay không
    if img is None:
        print(f"Error: Unable to read image at {image_path}")
        return

    # Tăng cường độ sáng và độ tương phản
    enhanced_img = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

    # Hiển thị ảnh gốc và ảnh tăng cường
    cv2.imshow('Original Image', img)
    cv2.imshow('Enhanced Image', enhanced_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Lưu ảnh tăng cường
    cv2.imwrite('enhanced_image.jpg', enhanced_img)


def browse_image():
    # Mở hộp thoại chọn tệp ảnh
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")])
    entry_path.delete(0, tk.END)
    entry_path.insert(0, file_path)


def enhance_image_with_custom_params():
    image_path = entry_path.get()
    alpha = simpledialog.askfloat("Alpha", "Enter alpha value:")
    beta = simpledialog.askinteger("Beta", "Enter beta value:")

    enhance_image(image_path, alpha=alpha, beta=beta)


# Tạo cửa sổ chính
window = tk.Tk()
window.title("Image Enhancement")

# Tạo widget và button
label_path = tk.Label(window, text="Image Path:")
label_path.grid(row=0, column=0)

entry_path = tk.Entry(window, width=40)
entry_path.grid(row=0, column=1)

btn_browse = tk.Button(window, text="Browse", command=browse_image)
btn_browse.grid(row=0, column=2)

btn_enhance = tk.Button(window, text="Enhance Image", command=enhance_image_with_custom_params)
btn_enhance.grid(row=1, column=1)

# Mở cửa sổ
window.mainloop()
