import math


class Vertex:

    def __init__(self, point):
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
            raise ZeroDivisionError()
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

    def distance(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def __add__(self, v: 'Vertex') -> 'Vertex':
        if isinstance(v, Vertex):
            return Vertex((self.x + v.x, self.y + v.y, self.z + v.z))
        else:
            raise TypeError('Add not with a vector!')

    def __sub__(self, v: 'Vertex') -> 'Vertex':
        if isinstance(v, Vertex):
            return Vertex((self.x - v.x, self.y - v.y, self.z - v.z))
        else:
            raise TypeError('Sub not with a vector!')

    def __neg__(self):
        return Vertex((-self.x, -self.y, -self.z))

    def __mul__(self, val) -> 'Vertex':
        if isinstance(val, int) or isinstance(val, float):
            return Vertex((self.x * val, self.y * val, self.z * val))
        elif isinstance(val, Vertex):
            return Vertex((self.x * val.x, self.y * val.y, self.z * val.z))
        else:
            raise TypeError('Multiplication not with vector, int or float')

    def normalize(self):
        dist = self.distance()
        if dist != 0:
            self.x /= dist
            self.y /= dist
            self.z /= dist
        else:
            raise TypeError('Normalizing zero vector')

    def dot(self, v: 'Vertex') -> float:
        if isinstance(v, Vertex):
            return self.x * v.x + self.y * v.y + self.z * v.z
        else:
            raise TypeError('Dot not with a vector')

    def cross(self, v: 'Vertex') -> 'Vertex':
        if isinstance(v, Vertex):
            return Vertex((self.y * v.z - self.z * v.y, self.z * v.x - self.x * v.z, self.x * v.y - self.y * v.x))
        else:
            raise TypeError('Cross not with a vector')
