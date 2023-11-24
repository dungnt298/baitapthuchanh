import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Button, StringVar, OptionMenu, Canvas, Frame, Scrollbar, Listbox, END, filedialog


class DataAnalysisApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Data Analysis App")

        # Biến lưu trữ đường dẫn tệp dữ liệu
        self.file_path = None

        # DataFrame để lưu trữ dữ liệu
        self.df = pd.DataFrame()

        # Tạo biến StringVar để lưu trữ tên cột được chọn
        self.selected_column = StringVar()
        self.selected_column.set("")

        # Tạo dropdown menu để chọn cột
        self.column_dropdown = OptionMenu(master, self.selected_column, "")
        self.column_dropdown.grid(row=0, column=1, padx=10, pady=10)

        # Nút chọn file
        self.browse_button = Button(master, text="Browse File", command=self.browse_file)
        self.browse_button.grid(row=0, column=0, padx=10, pady=10)

        # Nút phân tích và hiển thị đồ thị
        self.analyze_button = Button(master, text="Analyze Data", command=self.analyze_and_plot)
        self.analyze_button.grid(row=0, column=2, padx=10, pady=10)

        # Khung chứa danh sách kết quả phân tích
        self.result_frame = Frame(master)
        self.result_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Thanh cuộn cho khung chứa danh sách
        self.scrollbar = Scrollbar(self.result_frame, orient="vertical")
        self.result_listbox = Listbox(self.result_frame, yscrollcommand=self.scrollbar.set, width=50)
        self.scrollbar.config(command=self.result_listbox.yview)

        # Hiển thị thanh cuộn và danh sách
        self.scrollbar.pack(side="right", fill="y")
        self.result_listbox.pack(side="left", fill="both", expand=True)

    def browse_file(self):
        # Hiển thị hộp thoại mở tệp và lấy đường dẫn tệp
        self.file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

        # Nếu có đường dẫn, đọc dữ liệu và cập nhật menu dropdown
        if self.file_path:
            self.update_dropdown()

    def update_dropdown(self):
        # Đọc dữ liệu từ tệp và cập nhật menu dropdown
        self.df = pd.read_csv(self.file_path)
        column_names = self.df.columns
        self.selected_column.set(column_names[0])  # Đặt giá trị mặc định cho dropdown
        menu = self.column_dropdown["menu"]
        menu.delete(0, "end")

        for column_name in column_names:
            menu.add_command(label=column_name, command=lambda value=column_name: self.selected_column.set(value))

    def analyze_and_plot(self):
        # Xóa nội dung cũ trong danh sách
        self.result_listbox.delete(0, END)

        # Lấy tên cột được chọn
        selected_column = self.selected_column.get()

        # Kiểm tra xem có đường dẫn tệp không
        if self.file_path is None:
            self.result_listbox.insert(END, "Please select a file.")
            return

        # Tính toán các giá trị thống kê
        max_value = self.df[selected_column].max()
        min_value = self.df[selected_column].min()
        mean_value = self.df[selected_column].mean()

        # Hiển thị kết quả trong danh sách
        self.result_listbox.insert(END, f"Maximum Value: {max_value}")
        self.result_listbox.insert(END, f"Minimum Value: {min_value}")
        self.result_listbox.insert(END, f"Mean Value: {mean_value}")

        # Vẽ đồ thị phân bố
        plt.figure(figsize=(8, 6))
        plt.hist(self.df[selected_column], bins=20, color='skyblue', edgecolor='black')
        plt.title(f'Distribution of {selected_column}')
        plt.xlabel(selected_column)
        plt.ylabel('Frequency')
        plt.show()


# Tạo và chạy ứng dụng
root = Tk()
app = DataAnalysisApp(root)
root.mainloop()
