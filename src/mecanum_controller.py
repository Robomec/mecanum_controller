from src.config import Config


class MecanumController:
    
    def __init__(self):
        self.config = Config()
        self.wheel_separation_width = self.config.distance_left_to_right_wheel / 2
        self.wheel_separation_length = self.config.distance_front_to_rear_wheel / 2

    
    def init_motros(self):
        pass
