from unittest import TestCase
from src.models import ParkingSlot

class TestAssignSlot(TestCase):
    def test_assign_slot(self):
        check_vehicle_type = "car"
        expected_result = 16
        self.assertEqual(ParkingSlot().assign_slot(vehicle_type=check_vehicle_type),expected_result)

    def test_assign_slot1(self):
        check_vehicle_type = "wjkfjf"
        expected_result = None
        self.assertEqual(ParkingSlot().assign_slot(vehicle_type=check_vehicle_type),expected_result)