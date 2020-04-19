import window_template
import face
import vertex


class Action_3D:

    def reset_event(self, event):
        self.prev_event = []
    
    def do_event(self, event):
        if self.prev_event:
            self.rotate(0, (event.y - self.prev_event[1]) / 20)
            self.rotate(1, (event.x - self.prev_event[0]) / 20)
            self.clear()
            self.update()
        self.prev_event = [event.x, event.y]

    def key_press(self, event):
        if event.keysym == 'Up':
            self.flatten(2, -5)
        elif event.keysym == 'Down':
            self.rotate(0, 0.5)
        elif event.keysym == 'Right':
            self.rotate(1, 0.5)
        elif event.keysym == 'Left':
            self.rotate(1, -0.5)
        elif event.keysym == 'p':
            self.scale += 1
        elif event.keysym == 'o' and self.scale > 1:
            self.scale -= 1
        elif event.keysym == 'e':
            points, triangles = self.clicked()
            self.points = []
            self.shapes = []
            self.add_points(points)
            self.add_faces(triangles)

        self.clear()
        self.update()

    def mouse_scale(self, event):
        self.scale += event.delta / 60
        self.clear()
        self.update()
        
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
            
    def __init__(self, points, shapes, width=800, height=600, distance=5, scale=100, title='3D', background='white'):
        self.distance = distance
        self.scale = scale
        self.root = window_template.Window_template(width, height, title, background)
        self.root.window.bind('<B1-Motion>', self.do_event)
        self.prev_event = []
        self.root.window.bind('<ButtonRelease-1>', self.reset_event)
        self.root.window.bind('<MouseWheel>', self.mouse_scale)
        self.root.window.bind_all('<Key>', self.key_press)
        self.add_points(points)
        self.add_faces(shapes)

    def rotate(self, axis: int, angle: float):
        for point in self.points:
            point.rotate(axis, angle)

    def flatten(self, scale: float, distance: float):
        for point in self.points:
            self.x, self.y = point.flatten(scale, distance)

    def update(self):
        points = []
        for point in self.points:
            points.append(point.flatten(self.scale, self.distance))

        shapes = []
        for shape in self.shapes:
            avg_z = 0
            temp = []
            for point in shape.points:
                avg_z -= self.points[point].z
                temp.append(points[point])
            temp.append(shape.color)
            temp.append(avg_z / len(shape.points))
            shapes.append(temp)

        shapes = sorted(shapes, key=lambda x: x[-1])

        for shape in shapes:
            self.root.create_shape(shape[0:-2], shape[-2])

    def clicked(self):
        return self.root.clicked()

    def clear(self):
        self.root.clear()

    def mainloop(self):
        self.root.mainloop()
