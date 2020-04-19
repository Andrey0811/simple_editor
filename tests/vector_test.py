import unittest
import vector as v


class GeometryTest(unittest.TestCase):

    zero = v.Vector(0, 0, 0)

    def test_distance(self):
        a = v.Vector(-1, -1, -1)
        assert self.zero.distance() == 0
        assert a.distance() - 1.732 < 0.001

    def test_add(self):
        a = v.Vector(-1, 2, 7)
        a.__add__(self.zero)
        assert a.x == -1 and a.y == 2 and a.z == 7

    def test_sub(self):
        pass

    def test_neg(self):
        zero_neg = self.zero.__neg__()
        a = v.Vector(1, 1, 1).__neg__()
        assert zero_neg.x == zero_neg.y == zero_neg.z == self.zero.x == self.zero.y == self.zero.z
        assert a.x == -1 and a.y == -1 and a.z == -1

    def test_mul(self):
        zero1 = self.zero.__mul__(5)
        zero2 = self.zero.__mul__(self.zero)
        a = v.Vector(1, 2, 3).__mul__(v.Vector(3, 2, 1))
        assert zero1.x == zero1.y == zero1.z == zero2.x == zero2.y == zero2.z == self.zero.x == self.zero.y == self.zero.z
        assert a.x == 3 and a.y == 4 and a.z == 3

    def test_normalize(self):
        a = v.Vector(2, 0, 0)
        a.normalize()
        assert a.x == 1 and a.y == 0 and a.z == 0

    def test_dot(self):
        a = v.Vector(1, 2, 3)
        assert a.dot(v.Vector(3, 2, 1)) == 10
        assert a.dot(self.zero) == 0

    def test_cross(self):
        a = v.Vector(1, 2, 3).cross(v.Vector(3, 2, 1))
        assert a.x == -4 and a.y == 8 and a.z == -4


if __name__ == '__main__':
    unittest.main()




