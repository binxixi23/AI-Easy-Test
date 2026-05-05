import tkinter as tk
from tkinter import ttk

class RobotDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Easy Test - Patient Monitor")
        self.root.geometry("600x400")
        self.root.configure(bg='#f0f8ff') # Màu xanh nhạt y tế

        # Tiêu đề
        self.label_title = tk.Label(root, text="AI EASY TEST v1.0", font=("Arial", 24, "bold"), bg='#f0f8ff', fg='#0047ab')
        self.label_title.pack(pady=20)

        # Trạng thái hiện tại
        self.status_var = tk.StringVar(value="Vui lòng đặt tay vào vị trí...")
        self.label_status = tk.Label(root, textvariable=self.status_var, font=("Arial", 14), bg='#ffffff', width=40, height=2, relief="groove")
        self.label_status.pack(pady=10)

        # Thanh tiến trình (Progress Bar)
        self.progress = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
        self.progress.pack(pady=30)

        # Kết quả xét nghiệm
        self.result_label = tk.Label(root, text="", font=("Arial", 12, "italic"), bg='#f0f8ff')
        self.result_label.pack(pady=10)

    def update_status(self, text, progress_val):
        self.status_var.set(text)
        self.progress['value'] = progress_val
        self.root.update()

    def show_result(self, result_text):
        self.result_label.config(text=f"KẾT QUẢ: {result_text}", fg="green")
