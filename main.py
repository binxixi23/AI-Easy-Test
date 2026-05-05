import cv2
from src.vision import VesselDetector
from src.robot_ctrl import ArmController

class AIEasyTest:
    def __init__(self):
        print("System: AI Easy Test Initializing...")
        self.vision = VesselDetector()
        self.arm = ArmController()
        self.is_connected = True

    def run_cycle(self):
        # 1. Tìm tĩnh mạch
        target = self.vision.get_vein_coordinates()
        
        if target:
            # 2. Cố định và lấy máu
            self.arm.secure_hand()
            self.arm.move_to(target)
            self.arm.draw_blood()
            
            # 3. Xét nghiệm nhanh & Hậu cần
            self.arm.apply_bandaid()
            print("Process Complete. Data uploaded to Cloud.")

if __name__ == "__main__":
    robot = AIEasyTest()
    robot.run_cycle()
