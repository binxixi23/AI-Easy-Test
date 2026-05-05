class BloodAnalyzer:
    def process_sample(self):
        print("[Analyzer] Đang xét nghiệm máu trong hộp kín...")
        return {"Glucose": "5.4 mmol/L", "Oxy": "98%"}

    def upload_results(self, data):
        print(f"[Cloud] Đang gửi kết quả {data} qua Wi-Fi...")
