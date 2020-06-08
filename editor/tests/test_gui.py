import unittest
import src.main_gui as w
from src.geometry.engine import engine as e


class GuiTest(unittest.TestCase):
    points, triangles = e.from_stl('cube.stl')
    root = w.MainGui(points, triangles)

    def test_key_press(self):
        self.root.key_press(Event('Up'))
        temp = self.root.engine.points
        assert temp == self.root.engine.points
        self.root.key_press(Event('Down'))
        temp = self.root.engine.points
        assert temp == self.root.engine.points
        self.root.key_press(Event('Right'))
        temp = self.root.engine.points
        assert temp == self.root.engine.points
        self.root.key_press(Event('Left'))
        temp = self.root.engine.points
        assert temp == self.root.engine.points
        self.root.key_press(Event('w'))
        temp = self.root.engine.points
        assert temp == self.root.engine.points
        self.root.key_press(Event('s'))
        temp = self.root.engine.points
        assert temp == self.root.engine.points
        self.root.key_press(Event('a'))
        temp = self.root.engine.points
        assert temp == self.root.engine.points
        self.root.key_press(Event('d'))
        temp = self.root.engine.points
        assert temp == self.root.engine.points
        temp = self.root.engine.scale
        self.root.key_press(Event('p'))
        assert temp + self.root.engine.forward_value == self.root.engine.scale
        temp = self.root.engine.scale
        self.root.key_press(Event('o'))
        assert temp - self.root.engine.forward_value == self.root.engine.scale

    def test_reset_event(self):
        self.root.engine.prev_event.append(1)
        assert len(self.root.engine.prev_event) != 0
        self.root.reset_event('')
        assert len(self.root.engine.prev_event) == 0


class Event:
    def __init__(self, value: str):
        self.keysym = value


if __name__ == '__main__':
    unittest.main()
