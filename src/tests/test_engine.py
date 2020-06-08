import unittest
from src.geometry.engine import engine as e


class EngineTest(unittest.TestCase):
    points, triangles = e.from_stl('cube.stl')
    eng = e(points, triangles)

    def test_flatten(self):
        self.eng.flatten(self.eng.scale, self.eng.distance)
        temp = self.eng.points
        assert temp == self.eng.points

    def test_move(self):
        self.eng.move(2, 1, 3)
        temp = self.eng.points
        assert temp == self.eng.points
        self.eng.move(0, 0, 0)
        temp = self.eng.points
        assert temp == self.eng.points

    def test_rotate(self):
        self.eng.rotate(0, 0.5)
        temp = self.eng.points
        assert temp == self.eng.points
        self.eng.rotate(1, 0.5)
        temp = self.eng.points
        assert temp == self.eng.points
        self.eng.rotate(2, 0)
        temp = self.eng.points
        assert temp == self.eng.points
        self.eng.rotate(0, 0)
        assert temp == self.eng.points
        self.eng.rotate(1, 0)
        assert temp == self.eng.points
        self.eng.rotate(2, 0)
        assert temp == self.eng.points

    def test_change_scale(self):
        temp = self.eng.scale
        self.eng.scale += 0
        assert temp == self.eng.scale
        self.eng.scale += 5
        assert temp + 5 == self.eng.scale

    @staticmethod
    def test_four_triangles():
        points, triangles = e.from_stl('t.stl')
        points_true = [[1, 1, -1], [-1, 1, -1], [-1, 1, 1],
                       [1, 1, 1], [-1, -1, 1], [1, -1, 1]]
        triangles_true = [[0, 1, 2], [0, 2, 3], [2, 3, 4], [3, 4, 5]]
        assert points == points_true and triangles == triangles_true

    @staticmethod
    def test_to_stl():
        points = [[-1, -1, -1], [-1, -1, 1], [-1, 1, 1], [-1, 1, -1],
                  [1, -1, -1], [1, -1, 1], [1, 1, 1], [1, 1, -1]]
        triangles = [[0, 1, 2], [0, 2, 3], [2, 3, 7], [2, 7, 6],
                     [1, 2, 5], [2, 5, 6], [0, 1, 4], [1, 4, 5], [4, 5, 6],
                     [4, 6, 7], [3, 7, 4], [4, 3, 0]]
        e.to_stl(points, triangles, 'cube_test_to_stl.stl', '')
        with open('cube.stl', 'r') as f:
            l = f.read().split('\n')
        with open('cube_test_to_stl.stl', 'r') as f:
            r = f.read().split('\n')
        assert ''.join(l[1:]) == ''.join(r[1:])

    def test_from_binary_stl(self):
        pass


if __name__ == '__main__':
    unittest.main()
