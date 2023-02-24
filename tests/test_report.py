import json
from unittest import TestCase

from models.position import Position

from models.vehicle import Vehicle
from manager.report import Report
from data.vehiclePositions import vehiclePositions


def make_vehicle(value):
    vehicle = Vehicle(value["name"])
    for pos in list(value["positions"]):
        vehicle.add_position(Position(pos["x"], pos["y"], pos["t"]))

    return vehicle


class TestReport(TestCase):
    report: Report

    @classmethod
    def setUp(cls):
        vehicles = [make_vehicle(raw_vehicle)
                    for raw_vehicle in vehiclePositions]
        cls.report = Report(vehicles)

    def test_report_three_most_traveled(self):
        result = [vehicle.name
                  for vehicle in self.report.get_most_traveled_vehicles(3)]

        self.assertEqual(result, ['C', 'B', 'A'])

    def test_report_three_fastest(self):
        result = [vehicle.name
                  for vehicle in self.report.get_fastest_vehicles(3)]

        self.assertEqual(result, ['A', 'C', 'B'])

    def test_needed_maintenance(self):
        vehicle_1 = Vehicle("El Clio")
        vehicle_1.add_position(Position(0, 0, 1))
        vehicle_1.add_position(Position(1, 1, 2))
        vehicle_1.add_position(Position(2, 2, 3))

        vehicle_2 = Vehicle("El senor de los cielos")
        vehicle_2.add_position(Position(1, 0, 1))
        vehicle_2.add_position(Position(1, 2, 2))
        vehicle_2.add_position(Position(2, 2, 3))

        vehicle_3 = Vehicle("El sevichitos")
        vehicle_3.add_position(Position(1, 1, 1))
        vehicle_3.add_position(Position(2, 2, 2))
        vehicle_3.add_position(Position(3, 3, 3))

        report = Report([vehicle_1, vehicle_2, vehicle_3])

        result = {vehicle.name for vehicle in report.get_vehicles_needing_maintenance(3)}

        self.assertEqual(result, {vehicle_1.name, vehicle_2.name})
