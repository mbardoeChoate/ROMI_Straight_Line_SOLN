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
    # Setup
    # Need acces to the reset functions of each encoder
    left_reset = drivetrain.leftEncoder.reset
    right_reset = drivetrain.rightEncoder.reset

    # Action
    drivetrain.resetEncoders()

    # Assert
    left_reset.assert_called_once()
    right_reset.assert_called_once()


def test_averageDistanceMeter(drivetrain: Drivetrain, monkeypatch: MonkeyPatch) -> None:
    # Setup
    def mock_getRightDistanceMeter(self):
        return 3.0

    def mock_getLeftDistanceMeter(self):
        return 2.0

    monkeypatch.setattr(Drivetrain, "getLeftDistanceMeter", mock_getRightDistanceMeter)
    monkeypatch.setattr(Drivetrain, "getRightDistanceMeter", mock_getLeftDistanceMeter)
    # Action

    dist = drivetrain.averageDistanceMeter()

    # Assert
    assert dist == 2.5


def test_arcadeDrive(drivetrain: Drivetrain) -> None:
    # Setup
    arcadeDrive = drivetrain.drive.arcadeDrive

    # Action

    drivetrain.drive.arcadeDrive(0.2, 0.3)

    # Assert

    arcadeDrive.assert_called_once()
