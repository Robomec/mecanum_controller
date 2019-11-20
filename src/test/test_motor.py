import pytest
from src.motors.motor import Motor


def test_motor_exists():
    test = Motor
    assert test == Motor
