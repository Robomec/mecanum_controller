import pytest
from src.mecanum_controller import MecanumController
from src.config import Config


@pytest.mark.smoke
def test_mecanum_exists():
    test = MecanumController
    assert test == MecanumController


def test_mecanum_rads_to_rpm_5():
    """Quelle:https://www.convertunits.com/from/radian/second/to/RPM"""
    rads = 5
    exp_rpm = 47.746482982127
    act_rpm = MecanumController.convert_rads_to_rpm(rads)
    assert round(exp_rpm, 0) == round(act_rpm, 0)


def test_mecanum_rads_to_rpm_7642():
    """Quelle:https://www.convertunits.com/from/radian/second/to/RPM"""
    rads = 7642
    exp_rpm = 72975.7245898829
    act_rpm = MecanumController.convert_rads_to_rpm(rads)
    assert round(exp_rpm, 0) == round(act_rpm, 0)


def test_mecanum_rads_to_rpm_1000():
    """Quelle:https://www.convertunits.com/from/radian/second/to/RPM"""
    rads = 1000
    exp_rpm = 9549.2965964254
    act_rpm = MecanumController.convert_rads_to_rpm(rads)
    assert round(exp_rpm, 0) == round(act_rpm, 0)


def test_mecanum_rads_to_rpm_10000():
    """Quelle:https://www.convertunits.com/from/radian/second/to/RPM"""
    rads = 10000
    exp_rpm = 95492.965964254
    act_rpm = MecanumController.convert_rads_to_rpm(rads)
    assert round(exp_rpm, 0) == round(act_rpm, 0)
