import unittest
from src.geometry import vertex as v


class VertexTest(unittest.TestCase):
    a = v.Vertex((0, 0, 0))
    b = v.Vertex((1, 2, 3))

    def test_rotate(self):
        self.a.rotate(0, 360)
        assert self.a.x == self.a.y == self.a.z == 0
        self.a.rotate(0, 180)
        assert self.a.x == self.a.y == self.a.z == 0
        self.a.rotate(0, 90)
        assert self.a.x == self.a.y == self.a.z == 0
        self.b.rotate(0, 720)
        assert self.b.x == 1 and self.b.y - 0.075 < 0.001 \
               and self.b.z + 3.6 < 0.001
        self.b.rotate(0, 15)
        assert self.b.x == 1 and self.b.y - 3.424 < 0.001 \
               and self.b.z - 1.127 < 0.001
        self.b.rotate(0, 30)
        assert self.b.x == 1 and self.b.y + 1.959 < 0.001 \
               and self.b.z + 3.026 < 0.001
        self.assertRaises(ValueError, self.a.rotate, 5, 1)

    def test_flatten(self):
        x, y = self.b.flatten(1, -2)
        assert x == -2 and y == -4
        x, y = self.b.flatten(5, -1)
        assert x == -2 and y == -5
        # self.assertRaises(ZeroDivisionError, self.a.flatten, 1, 0)

    zero = v.Vertex((0, 0, 0))

    def test_distance(self):
        a = v.Vertex((-1, -1, -1))
        assert self.zero.distance() == 0
        assert a.distance() - 1.732 < 0.001

    def test_add(self):
        a = v.Vertex((-1, 2, 7))
        a.__add__(self.zero)
        assert a.x == -1 and a.y == 2 and a.z == 7
        self.assertRaises(TypeError, a.__add__, '')

    def test_sub(self):
        a = v.Vertex((-1, 2, 7))
        a.__sub__(self.zero)
        assert a.x == -1 and a.y == 2 and a.z == 7
        self.assertRaises(TypeError, a.__sub__, '')

    def test_neg(self):
        zero_neg = self.zero.__neg__()
        a = v.Vertex((1, 1, 1)).__neg__()
        assert zero_neg.x == zero_neg.y == zero_neg.z \
               == self.zero.x == self.zero.y == self.zero.z
        assert a.x == -1 and a.y == -1 and a.z == -1

    def test_mul(self):
        zero1 = self.zero.__mul__(5)
        zero2 = self.zero.__mul__(self.zero)
        a = v.Vertex((1, 2, 3)).__mul__(v.Vertex((3, 2, 1)))
        assert zero1.x == zero1.y == zero1.z == zero2.x == zero2.y == zero2.z \
               == self.zero.x == self.zero.y == self.zero.z
        assert a.x == 3 and a.y == 4 and a.z == 3
        self.assertRaises(TypeError, a.__mul__, '')

    def test_normalize(self):
        a = v.Vertex((2, 0, 0))
        a.normalize()
        assert a.x == 1 and a.y == 0 and a.z == 0
        a = v.Vertex((0, 0, 0))
        self.assertRaises(TypeError, a.normalize)

    def test_dot(self):
        a = v.Vertex((1, 2, 3))
        assert a.dot(v.Vertex((3, 2, 1))) == 10
        assert a.dot(self.zero) == 0
        self.assertRaises(TypeError, a.dot, 1)

    def test_cross(self):
        a = v.Vertex((1, 2, 3)).cross(v.Vertex((3, 2, 1)))
        assert a.x == -4 and a.y == 8 and a.z == -4
        self.assertRaises(TypeError, v.Vertex((1, 2, 3)).cross, 1)


if __name__ == '__main__':
    unittest.main()
