# 🛠 AI Easy Test - Hardware Specifications

Tài liệu này liệt kê các linh kiện cần thiết để xây dựng mô hình vật lý cho robot AI Easy Test.

## 1. Bộ não trung tâm (Controller)
*   **Main CPU:** NVIDIA Jetson Orin Nano hoặc Raspberry Pi 5 (Dùng để chạy Trí tuệ nhân tạo và xử lý hình ảnh thời gian thực).
*   **Microcontroller:** Arduino Mega 2560 (Dùng để điều khiển các động cơ bước của cánh tay robot và cảm biến lực).

## 2. Hệ thống Thị giác (Vision System)
*   **Camera:** Raspberry Pi NoIR Camera (Camera không có bộ lọc hồng ngoại để nhìn rõ tĩnh mạch).
*   **Laser/Light Source:** Đèn LED hồng ngoại (850nm) hoặc Laser NIR (Giúp làm nổi bật các mạch máu dưới da).

## 3. Hệ thống Robot (Actuators)
*   **Robot Arm:** Bộ khung cánh tay robot 3-4 trục (Sử dụng động cơ Stepper Nema 17 để đảm bảo độ chính xác).
*   **End Effector:** Ngón tay robot tích hợp giá giữ ống tiêm (Syringe Holder) và cảm biến áp lực.
*   **Wheeled Base:** 4 bánh xe Mecanum (Cho phép di chuyển đa hướng trong không gian hẹp).

## 4. Hệ thống Phân tích & Tiện ích
*   **Monitor:** Màn hình cảm ứng 10.1 inch (Hiển thị quy trình và kết quả cho bệnh nhân).
*   **Connectivity:** Module Wi-Fi 6 (Tích hợp sẵn trên Main CPU).
*   **Testing Box:** Ngăn chứa bộ kit xét nghiệm nhanh (Point-of-care testing).

## 5. Phụ kiện Y tế (Consumables)
*   Kim tiêm và ống nghiệm dùng một lần.
*   Bình chứa dung dịch sát trùng.
*   Cuộn băng cá nhân tự động (Auto-dispenser).
