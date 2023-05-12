from unittest.mock import MagicMock

import pytest

from drivetrain import Drivetrain
from pytest import MonkeyPatch


@pytest.fixture
def drivetrain() -> Drivetrain:
    # Create a drivetrain, but it has mock
    # classes for its dependencies
    drive = Drivetrain()
    drive.left_motor = MagicMock()
    drive.right_motor = MagicMock()
    drive.leftEncoder = MagicMock()
    drive.rightEncoder = MagicMock()
    drive.drive = MagicMock()
    drive.gyro = MagicMock()
    return drive


def test_reset_encoders(drivetrain: Drivetrain):
    '''A test to make sure that when we reset the encoders all the encoders are reset.
    '''
    # Setup
    # Need access to the reset functions of each encoder
    left_reset = drivetrain.leftEncoder.reset
    right_reset = drivetrain.rightEncoder.reset

    # Action
    drivetrain.resetEncoders()

    # Assert
    left_reset.assert_called_once()
    right_reset.assert_called_once()


@pytest.mark.parametrize(('left_Distance', 'right_Distance', 'output'), (
        (2, 3, 2.5),
        (10, 20, 15),
        (-3, 3, 0)
), )
def test_averageDistanceMeter(drivetrain: Drivetrain, monkeypatch: MonkeyPatch, left_Distance, right_Distance,
                              output) -> None:
    # Setup
    def mock_getRightDistanceMeter(self):
        return left_Distance

    def mock_getLeftDistanceMeter(self):
        return right_Distance

    monkeypatch.setattr(Drivetrain, "getLeftDistanceMeter", mock_getRightDistanceMeter)
    monkeypatch.setattr(Drivetrain, "getRightDistanceMeter", mock_getLeftDistanceMeter)
    # Action

    dist = drivetrain.averageDistanceMeter()

    # Assert
    assert dist == output


def test_arcadeDrive(drivetrain: Drivetrain) -> None:
    # Setup
    arcadeDrive = drivetrain.drive.arcadeDrive

    # Action

    drivetrain.drive.arcadeDrive(0.2, 0.3)

    # Assert

    arcadeDrive.assert_called_once()
