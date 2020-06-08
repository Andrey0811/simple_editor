import unittest
from work_with_stl import work_with_stl as w


class TransferTest(unittest.TestCase):

    def test_four_triangles(self):
        points, triangles = w.work_with_stl.from_stl('test.stl')
        points_true = [[1, 1, -1], [-1, 1, -1],  [-1, 1, 1], [1, 1, 1], [-1, -1, 1], [1, -1, 1]]
        triangles_true = [[0, 1, 2], [0, 2, 3], [2, 3, 4], [3, 4, 5]]
        assert points == points_true and triangles == triangles_true

    def test_to_stl(self):
        points = [[-1, -1, -1], [-1, -1, 1], [-1, 1, 1], [-1, 1, -1], [1, -1, -1], [1, -1, 1], [1, 1, 1], [1, 1, -1]]
        triangles = [[0, 1, 2], [0, 2, 3], [2, 3, 7], [2, 7, 6], [1, 2, 5], [2, 5, 6], [0, 1, 4], [1, 4, 5], [4, 5, 6],
                     [4, 6, 7], [3, 7, 4], [4, 3, 0]]
        w.work_with_stl.to_stl(points, triangles, 'test_cube.stl', '')
        with open('test_cube_correct.stl', 'r') as f:
            l = f.read()
        with open('test_cube.stl', 'r') as f:
            r = f.read()
        assert l == r

    def test_from_binary_stl(self):
        pass


if __name__ == '__main__':
    unittest.main()