from geometry import matrix, vertex, face
import easygui
from work_with_stl import work_with_stl as tr


class engine:

    def __init__(self, points, shapes, distance=5, scale=10):
        self.distance = distance
        self.scale = scale
        self.prev_event = []
        self.add_points(points)
        self.add_faces(shapes)
        self.forward_value = 10
        self.rotation_step = 0.5
        self.translation_step = 0.5
        self.scale_mul = 1

    def reset_event(self, event):
        self.prev_event = []

    def key_press(self, event):
        if event.keysym == 'Up':
            self.rotate(0, -self.rotation_step)
        elif event.keysym == 'Down':
            self.rotate(0, self.rotation_step)
        elif event.keysym == 'Right':
            self.rotate(1, self.rotation_step)
        elif event.keysym == 'Left':
            self.rotate(1, -self.rotation_step)
        elif event.keysym == 'w':
            self.move(0, -self.translation_step, 0)
        elif event.keysym == 's':
            self.move(0, self.translation_step, 0)
        elif event.keysym == 'a':
            self.move(-self.translation_step, 0, 0)
        elif event.keysym == 'd':
            self.move(self.translation_step, 0, 0)
        elif event.keysym == 'p':
            self.scale += self.forward_value
        elif event.keysym == 'o' and self.scale > 1:
            self.scale -= self.forward_value
        elif event.keysym == 'e':
            points, triangles = self.clicked()
            self.points = []
            self.shapes = []
            self.add_points(points)
            self.add_faces(triangles)

    def clicked(self):
        return tr.work_with_stl.from_stl(easygui.fileopenbox(filetypes=['*.stl']))

    def mouse_scale(self, event):
        self.scale += event.delta / 60
        
    def add_points(self, points: list):
        self.points = []
        for point in points:
            self.points.append(vertex.Vertex(point))
            
    def add_faces(self, shapes: list, default_color='gray'):
        self.shapes = []
        for shape in shapes:
            if type(shape[-1]) != str:
                shape.append(default_color)
            self.shapes.append(face.Face(shape))

    def rotate(self, axis: int, angle: float):
        for point in self.points:
            point.rotate(axis, angle)

    def move(self, x, y, z):
        mat = matrix.Matrix(4, 4)
        mat[(0, 0)] = 1
        mat[(1, 1)] = 1
        mat[(2, 2)] = 1
        mat[(3, 3)] = 1
        mat[(0, 3)] = x
        mat[(1, 3)] = y
        mat[(2, 3)] = z
        for point in self.points:
            temp = mat.__mul__(point)
            point.x = temp.x
            point.y = temp.y
            point.z = temp.z

    def flatten(self, scale: float, distance: float):
        for point in self.points:
            self.x, self.y = point.flatten(scale, distance)


