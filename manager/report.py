from models.vehicle import Vehicle


class Report:
    vehicles: list[Vehicle]

    def __init__(self, vehicles: list[Vehicle]) -> None:
        self.vehicles = vehicles

    def get_most_traveled_vehicles(self, k) -> list[Vehicle]:
        result = sorted(self.vehicles, key=lambda v: v.distance_traveled(), reverse=True)

        return result[:k]

    def get_fastest_vehicles(self, k) -> list[Vehicle]:
        result = sorted(self.vehicles, key=lambda v: v.average_speed(), reverse=True)

        return result[:k]

    def get_vehicles_needing_maintenance(self, k) -> list[Vehicle]:
        set_of_collided_v = set()
        hash_positions = dict()

        for vehicle in self.vehicles:
            for position in vehicle.positions:
                if str(position) not in hash_positions:
                    hash_positions[str(position)] = vehicle
                else:
                    set_of_collided_v.add(vehicle)
                    set_of_collided_v.add(hash_positions[str(position)])

        return list(set_of_collided_v)[:k]
