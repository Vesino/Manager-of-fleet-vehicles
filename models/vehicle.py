from models.position import Position


class Vehicle:

    def __init__(self, name: str) -> None:
        self.name = name
        self.positions = []

    def add_position(self, position: Position):
        self.positions.append(position)

    def distance_traveled(self) -> int:
        distance = 0

        length = len(self.positions)
        if length < 2:
            return distance

        for i, position in enumerate(self.positions, start=1):
            if i == length:
                break

            distance += position.distance_to(self.positions[i])

        return distance

    def average_speed(self) -> int:
        max_time = max(self.positions, key=lambda p: p.t).t
        # time window offset
        min_time = min(self.positions, key=lambda p: p.t).t
        max_time -= min_time
        average = self.distance_traveled() / max_time if max_time else 0

        return average
