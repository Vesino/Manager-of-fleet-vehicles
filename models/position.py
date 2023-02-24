

from math import sqrt


class Position:
    
    x: int
    y: int
    t: int
    
    def __init__(self, x: int, y: int, t: int) -> None:
        self.x = x
        self.y = y
        self.t = t

    def __hash__(self):
        return hash((self.x, self.y, self.t))

    def __str__(self):
        return f"{self.x}-{self.y}-{self.t}"

    def distance_to(self, other: 'Position'):
        dx = other.x - self.x
        dy = other.y - self.y
        
        return sqrt(dx * dx + dy * dy)
        