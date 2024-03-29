from src.config import Config
from src.motors.motor import getMotors, Motor
from src.logging import Log

class MecanumController:

    def __init__(self):
        self.config = Config()
        self.wheel_separation_width = self.config.distance_left_to_right_wheel / 2
        self.wheel_separation_length = self.config.distance_front_to_rear_wheel / 2

    
    def init_motros(self):
        motors = getMotors()
        self.motor_front_left = motors['L1']
        self.motor_front_rigth = motors['R1']
        self.motor_rear_left = motors['L2']
        self.motor_rear_rigth = motors['R2']

    
    @staticmethod
    def convert_rads_to_rpm( rads: int) -> int:
        """convert rad/s Radian per second to rpm revolutions per minute"""
        return rads * 9.5493

    def setKinematics(self, linearX, linearY, angularZ):
        front_rigth_rads = (1/self.config.wheel_radius) * (linearX – linearY – (self.wheel_separation_width + self.wheel_separation_length)*angularZ)
        self.motor_front_left.setSpeed(
            self.convert_rads_to_rpm(
                front_rigth_rads
            )
        )
        Log.debug(f"Set Motor rad/s front rigth to: {front_rigth_rads}")
        front_left_rads = (1/self.config.wheel_radius) * (linearX + linearY + (self.wheel_separation_width + self.wheel_separation_length)*angularZ)
        self.motor_front_rigth(
            self.convert_rads_to_rpm(
                front_left_rads
            )
        )
        Log.debug(f"Set Motor rad/s front left to: {front_left_rads}")
        rear_left_rads = (1/self.config.wheel_radius) * (linearX + linearY – (self.wheel_separation_width + self.wheel_separation_length)*angularZ)
        self.motor_rear_left(
            self.convert_rads_to_rpm(
                rear_left_rads
            )
        )
        Log.debug(f"Set Motor rad/s rear left to: {rear_left_rads}")
        rear_rigth_rads = (1/self.config.wheel_radius) * (linearY – linearY + (self.wheel_separation_width + self.wheel_separation_length)*angularZ)
        self.motor_rear_rigth(
            self.convert_rads_to_rpm(
                 rear_rigth_rads
            )
        )
        Log.debug(f"Set Motor rad/s rear rigth to: {rear_rigth_rads}")
        