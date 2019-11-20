import abc
from src.config import Config
import rospy
from src.logging import Log


class Motor(abc.ABC):
    @abc.abstractmethod
    def setSpeed(self, rpm: int):
        """Sets speed of motor in rpm (Revolutions per minute)
            ms: int 
            if ms is negetiv the motor will drive in reverse 
        """
        pass

    @abc.abstractmethod
    def getSpeed(self) -> int:
        """returns the current speed in rpm (Revolutions per minute)"""
        pass


def getMotors() -> dict:
    """Returns a dict of motors
        R1: front rigth Motor
        L1: front left Motor 
        R2: rear  rigth Motor
        L2: rear  left Motor
    """
    config = Config()
    if config.motor_driver_type.lower() == config.THINKER_MOTOR_DIRVER.lower():
        return {
            "R1": "test",
            "L1": "test",
            "R2": "test",
            "L2": "test",
        }
        Log.info(f"Using {config.THINKER_MOTOR_DIRVER} Moter driver")
    else:
        er_msg = (
            f"Couln't find a motor driver! Given Parameter: {config.motor_driver_type}"
        )
        Log.fatal(er_msg)
        raise ValueError(er_msg)
