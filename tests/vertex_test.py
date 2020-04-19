import unittest
import vertex as v


class VertexTest(unittest.TestCase):
    a = v.Vertex([0, 0, 0])
    b = v.Vertex([1, 2, 3])

    def test_rotate(self):
        self.a.rotate(0, 360)
        assert self.a.x == self.a.y == self.a.z == 0
        self.a.rotate(0, 180)
        assert self.a.x == self.a.y == self.a.z == 0
        self.a.rotate(0, 90)
        assert self.a.x == self.a.y == self.a.z == 0
        self.b.rotate(0, 720)
        assert self.b.x == 1 and self.b.y - 0.075 < 0.001 and self.b.z + 3.6 < 0.001
        self.b.rotate(0, 15)
        assert self.b.x == 1 and self.b.y - 3.424 < 0.001 and self.b.z - 1.127 < 0.001
        self.b.rotate(0, 30)
        assert self.b.x == 1 and self.b.y + 1.959 < 0.001 and self.b.z + 3.026 < 0.001

    def test_flatten(self):
        x, y = self.b.flatten(1, -3)
        assert x == None and y == None
        x, y = self.b.flatten(5, -2)
        assert x == -10 and y == -20


if __name__ == '__main__':
    unittest.main()
