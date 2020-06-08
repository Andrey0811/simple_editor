import math


class Vertex:

    def __init__(self, point: list):
        (x, y, z) = point
        self.x = x
        self.y = y
        self.z = z

    def flatten(self, scale: float, distance: float):
        new_x = None
        new_y = None
        try:
            new_x = int(((self.y * distance) / (self.z + distance)) * scale)
            new_y = int(((self.x * distance) / (self.z + distance)) * scale)
        except ZeroDivisionError:
            raise ZeroDivisionError('Division on Zero: must distance != current_z')
        return new_y, new_x

    def rotate(self, axis: int, angle: float):
        angle = angle / 450 * 180 / math.pi

        if axis == 0:
            new_y = self.y * math.cos(angle) - self.z * math.sin(angle)
            new_z = self.z * math.cos(angle) + self.y * math.sin(angle)
            new_x = self.x
        elif axis == 1:
            new_x = self.x * math.cos(angle) - self.z * math.sin(angle)
            new_z = self.z * math.cos(angle) + self.x * math.sin(angle)
            new_y = self.y
        elif axis == 2:
            new_x = self.x * math.cos(angle) - self.y * math.sin(angle)
            new_y = self.y * math.cos(angle) + self.x * math.sin(angle)
            new_z = self.z
        else:
            raise ValueError('Error Axis')

        self.x = new_x
        self.y = new_y
        self.z = new_z

