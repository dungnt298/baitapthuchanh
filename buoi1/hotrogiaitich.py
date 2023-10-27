import sympy as sp
import tkinter as tk
from tkinter import Label, Entry, Button, Frame

# Hàm giải phương trình
def solve_equation():
    equation_str = equation_entry.get()
    x = sp.symbols('x')
    equation = sp.Eq(sp.sympify(equation_str), 0)
    solution = sp.solve(equation, x)
    equation_result_label.config(text=f"Kết quả: {solution}")

# Hàm tính đạo hàm
def calculate_derivative():
    expression_str = derivative_entry.get()
    x = sp.symbols('x')
    expression = sp.sympify(expression_str)
    derivative = sp.diff(expression, x)
    derivative_result_label.config(text=f"Đạo hàm: {derivative}")

# Hàm tính tích phân
def calculate_integral():
    expression_str = integral_entry.get()
    x = sp.symbols('x')
    expression = sp.sympify(expression_str)
    lower_limit = sp.sympify(integral_lower_limit_entry.get())
    upper_limit = sp.sympify(integral_upper_limit_entry.get())
    integral = sp.integrate(expression, (x, lower_limit, upper_limit))
    integral_result_label.config(text=f"Tích phân: {integral}")

def calculate_limit():
    expression_str = limit_entry.get()
    x = sp.symbols('x')
    expression = sp.sympify(expression_str)
    limit_point = sp.sympify(limit_point_entry.get())
    limit_result = sp.limit(expression, x, limit_point)
    limit_result_label.config(text=f"Giới hạn: {limit_result}")

# Tạo giao diện tkinter
root = tk.Tk()
root.title("Tính Đạo Hàm và Tích Phân")
root.geometry("600x200")
equation_frame = Frame(root)
equation_frame.grid(row = 0, column = 0)
equation_label = Label(equation_frame, text="Giải phương trình:")
equation_label.grid(row = 0, column = 0)
equation_entry = Entry(equation_frame)
equation_entry.grid(row = 1, column = 0)
solve_equation_button = Button(equation_frame, text="Giải", command=solve_equation)
solve_equation_button.grid(row = 2, column = 0)
equation_result_label = Label(equation_frame, text="Kết quả: ")
equation_result_label.grid(row = 3, column = 0)
# Frame cho tính đạo hàm
derivative_frame = Frame(root)
derivative_frame.grid(row = 0, column = 1)
derivative_label = Label(derivative_frame, text="Tính đạo hàm:")
derivative_label.grid(row = 0, column = 1)
derivative_entry = Entry(derivative_frame)
derivative_entry.grid(row = 1, column = 1)
calculate_derivative_button = Button(derivative_frame, text="Tính", command=calculate_derivative)
calculate_derivative_button.grid(row = 2, column = 1)
derivative_result_label = Label(derivative_frame, text="Đạo hàm: ")
derivative_result_label.grid(row = 3, column = 1)

# Frame cho tính tích phân
integral_frame = Frame(root)
integral_frame.grid(row = 0, column = 2)
integral_label = Label(integral_frame, text="Tính tích phân (cận trên và dưới):")
integral_label.grid(row = 0, column = 2)
integral_entry = Entry(integral_frame)
integral_entry.grid(row = 1, column = 2)
integral_lower_limit_label = Label(integral_frame, text="Giới hạn dưới:")
integral_lower_limit_label.grid(row = 2, column = 2)
integral_lower_limit_entry = Entry(integral_frame)
integral_lower_limit_entry.grid(row = 3, column = 2)
integral_upper_limit_label = Label(integral_frame, text="Giới hạn trên:")
integral_upper_limit_label.grid(row = 4, column = 2)
integral_upper_limit_entry = Entry(integral_frame)
integral_upper_limit_entry.grid(row = 5, column = 2)
calculate_integral_button = Button(integral_frame, text="Tính", command=calculate_integral)
calculate_integral_button.grid(row = 6, column = 2)
integral_result_label = Label(integral_frame, text="Tích phân: ")
integral_result_label.grid(row = 7, column = 2)

# Frame cho tính giới hạn
limit_frame = Frame(root)
limit_frame.grid(row = 0, column = 3)
limit_label = Label(limit_frame, text="Tính giới hạn (tại một điểm):")
limit_label.grid(row = 0, column = 3)
limit_entry = Entry(limit_frame)
limit_entry.grid(row = 1, column = 3)
limit_point_label = Label(limit_frame, text="Điểm giới hạn:")
limit_point_label.grid(row = 2, column = 3)
limit_point_entry = Entry(limit_frame)
limit_point_entry.grid(row = 3, column = 3)
calculate_limit_button = Button(limit_frame, text="Tính", command=calculate_limit)
calculate_limit_button.grid(row = 4, column = 3)
limit_result_label = Label(limit_frame, text="Giới hạn: ")
limit_result_label.grid(row = 5, column = 3)

# Khởi chạy giao diện
root.mainloop()
#tung commit