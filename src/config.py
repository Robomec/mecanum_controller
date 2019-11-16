import rospy

global config = Config()

class Config():

    def __init__(self):
        # distance in mm
        self.DISTANCE_LEFT_TO_RIGHT_WHEEL = rospy.get_param("DISTANCE_LEFT_TO_RIGHT_WHEEL", 200)
        # distance in mm
        self.DISTANCE_FRONT_TO_REAR_WHEEL = rospy.get_param("DISTANCE_FRONT_TO_REAR_WHEEL", 200)
        # motor type 'thinker', 
        self.motor_driver_type = rospy.get_param('motor_driver_type', 'thinker' )
        # wheel_perimeter in mm 
        self.wheel_perimeter('wheel_perimeter', 100)



def getConfig():
    return config