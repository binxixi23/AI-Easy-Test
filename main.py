import tkinter as tk
from src.gui import RobotDashboard
import time

def run_simulation(gui):
    # Bước 1: Khởi động
    gui.update_status("Đang khởi động hệ thống...", 10)
    time.sleep(1.5)

    # Bước 2: Tìm mạch máu
    gui.update_status("Đang quét tĩnh mạch bằng Laser NIR...", 30)
    time.sleep(2)

    # Bước 3: Lấy máu
    gui.update_status("Đang thực hiện lấy máu tự động...", 60)
    time.sleep(2)

    # Bước 4: Xét nghiệm & dán băng
    gui.update_status("Đang sát trùng và dán băng cá nhân...", 85)
    time.sleep(1.5)

    # Bước 5: Hoàn tất
    gui.update_status("Quy trình hoàn tất! Bạn có thể rút tay.", 100)
    gui.show_result("Glucose: 5.4 mmol/L - Bình thường")

if __name__ == "__main__":
    root = tk.Tk()
    app = RobotDashboard(root)
    
    # Chạy mô phỏng sau khi cửa sổ hiện lên 1 giây
    root.after(1000, lambda: run_simulation(app))
    
    root.mainloop()
