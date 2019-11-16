import pytest
from unittest import  mock
from src.mecanum_controller import MecanumController
from src.config import Config

@mock.patch('__main__.Config')
def create_instance

@pytest.mark.smoke
def test_mecanum_exists():
    test = MecanumController
    assert test == MecanumController

@pytest.mark.smoke
def test_mecanum_init():
    config_test = Config()
    instance = MecanumController()
    assert instance.config == config_test