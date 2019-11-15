import abc

class Motor(abc.ABC):
    
    @abc.abstractmethod
    def setSpeed(self, ms: int):
        """Sets speed of motor in meter per second
            ms: int 
            if ms is negetiv the motor while drive in reverse 
        """
        pass

    @abc.abstractmethod
    def getSpeed(self) -> int:
        """returns the current speed in meter per second"""
        pass
    