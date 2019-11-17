from src.config import Config
import math

class MecanumController:

    def __init__(self):
        self.config = Config()
        self.wheel_separation_width = self.config.distance_left_to_right_wheel / 2
        self.wheel_separation_length = self.config.distance_front_to_rear_wheel / 2

    
    def init_motros(self):
        self.motor_front_left = None
        self.motor_front_rigth = None
        self.motor_rear_left = None
        self.motor_rear_rigth = None

    
    @staticmethod
    def convert_rads_to_rpm( rads: int) -> int:
        """convert rad/s Radian per second to rpm revolutions per minute"""
        return rads * 9.5493