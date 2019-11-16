import abc

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
    