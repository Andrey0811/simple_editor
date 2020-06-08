import unittest
from engine import engine as e
from work_with_stl import work_with_stl as tr


class EngineTest(unittest.TestCase):
    points, triangles = tr.work_with_stl.from_stl('test_cube.stl')
    eng = e.engine(points, triangles)

    def test_flatten(self):
        self.eng.flatten(self.eng.scale, self.eng.distance)
        temp = self.eng.points
        assert temp == self.eng.points

    def test_move_1(self):
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

    def test_key_press(self):
        self.eng.key_press(event('Up'))
        temp = self.eng.points
        assert temp == self.eng.points
        self.eng.key_press(event('Down'))
        temp = self.eng.points
        assert temp == self.eng.points
        self.eng.key_press(event('Right'))
        temp = self.eng.points
        assert temp == self.eng.points
        self.eng.key_press(event('Left'))
        temp = self.eng.points
        assert temp == self.eng.points
        self.eng.key_press(event('w'))
        temp = self.eng.points
        assert temp == self.eng.points
        self.eng.key_press(event('s'))
        temp = self.eng.points
        assert temp == self.eng.points
        self.eng.key_press(event('a'))
        temp = self.eng.points
        assert temp == self.eng.points
        self.eng.key_press(event('d'))
        temp = self.eng.points
        assert temp == self.eng.points
        temp = self.eng.scale
        self.eng.key_press(event('p'))
        assert temp + self.eng.forward_value == self.eng.scale
        temp = self.eng.scale
        self.eng.key_press(event('o'))
        assert temp - self.eng.forward_value == self.eng.scale

    def test_reset_event(self):
        self.eng.prev_event.append(1)
        assert len(self.eng.prev_event) != 0
        self.eng.reset_event('')
        assert len(self.eng.prev_event) == 0


class event:
    def __init__(self, value: str):
        self.keysym = value


if __name__ == '__main__':
    unittest.main()