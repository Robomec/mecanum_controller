import rospy
import math


class Config:

    THINKER_MOTOR_DIRVER = "thinker"

    def __init__(self):
        # distance in mm
        self.distance_left_to_right_wheel = rospy.get_param(
            "DISTANCE_LEFT_TO_RIGHT_WHEEL", 200
        )
        # distance in mm
        self.distance_front_to_rear_wheel = rospy.get_param(
            "DISTANCE_FRONT_TO_REAR_WHEEL", 200
        )
        # motor type 'thinker',
        self.motor_driver_type = rospy.get_param("motor_driver_type", "thinker")
        # wheel_perimeter in mm
        self.wheel_perimeter = wheel_perimeter("wheel_perimeter", 100)
        # wheel_radius in mm
        self.wheel_radius = self.wheel_perimeter / (2 * math.pi)
