from unittest import TestCase
from models.vehicle import Vehicle
from models.position import Position


class TestVehicleDistance(TestCase):

    def test_traversed_distance(self):

        vehicle = Vehicle('foo')
        vehicle.add_position(Position(0, 0, 1))
        vehicle.add_position(Position(3, 4, 2))
        vehicle.add_position(Position(0, 0, 3))

        self.assertEqual(vehicle.distance_traveled(), 10)


class TestVehicleAverageSpeed(TestCase):
    def test_regular_speed(self):
        vehicle = Vehicle('foo')
        vehicle.add_position(Position(0, 0, 1))
        vehicle.add_position(Position(3, 4, 2))
        vehicle.add_position(Position(0, 0, 3))

        self.assertEqual(vehicle.average_speed(), 5)

    def test_vehicle_one_position(self):
        vehicle = Vehicle('foo')
        vehicle.add_position(Position(0, 0, 0))

        self.assertEqual(vehicle.average_speed(), 0)

    def test_vehicle_with_no_positions(self):
        vehicle = Vehicle('foo')

        self.assertEqual(vehicle.average_speed(), 0)
