from src.geometry import matrix, vertex, face
import re
import numpy as np
from struct import unpack


class engine:
    global reg
    reg = re.compile(r'facet normal *(?P<x_n>.+) (?P<y_n>.+) (?P<z_n>.+)\n.*'
                     r'\n* *vertex *(?P<x1>.+) (?P<y1>.+) (?P<z1>.+)'
                     r'\n* *vertex *(?P<x2>.+) (?P<y2>.+) (?P<z2>.+)'
                     r'\n* *vertex *(?P<x3>.+) (?P<y3>.+) (?P<z3>.+)\n* '
                     r'*endloop\n* *endfacet')

    global reg_light
    reg_light = re.compile(r'v\w* *(?P<x1>.+) (?P<y1>.+) (?P<z1>.+)')

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

    @staticmethod
    def from_stl(name: str):
        points = []
        triangles = []
        x = open(name, 'r')
        with open(name, 'r') as f:
            lines = f.read()
            list_str = reg.findall(lines)
            print(len(list_str))
            for item in list_str:
                a = [-1, -1, -1]
                for i in range(3):
                    temp = [float(item[3 + 3 * i]),
                            float(item[4 + 3 * i]),
                            float(item[5 + 3 * i])]
                    if temp not in points:
                        points.append(temp)
                        a[i] = len(points) - 1
                        continue

                    j = 0
                    for point in points:
                        if point == temp:
                            a[i] = j
                            break
                        j += 1

                triangles.append(a)
        return points, triangles

    @staticmethod
    def to_stl(points: list, triangles: list,
               name='file_1.stl', path='samples/'):
        with open(path + name, 'w') as f:
            f.write(f'solid {name}\n')
            for triangle in triangles:
                f.write(f' facet normal  '
                        f'0.000000e+00 0.000000e+00  0.000000e+00\n  '
                        f'outer loop\n'
                        f'   vertex {points[triangle[0]][0]} '
                        f'{points[triangle[0]][1]} '
                        f'{points[triangle[0]][2]}\n'
                        f'   vertex {points[triangle[1]][0]} '
                        f'{points[triangle[1]][1]} '
                        f'{points[triangle[1]][2]}\n'
                        f'   vertex {points[triangle[2]][0]} '
                        f'{points[triangle[2]][1]} '
                        f'{points[triangle[2]][2]}\n'
                        f'  endloop\n endfacet\n')
            f.write('endsolid')

    @staticmethod
    def from_binary_stl(name: str):
        with open(name, "rb") as f:
            header = f.read(80)
            count_triangles = unpack('i', f.read(4))[0]
            record_doc_type = np.dtype([
                ('Normals', np.float32, (3,)),
                ('Vertex1', np.float32, (3,)),
                ('Vertex2', np.float32, (3,)),
                ('Vertex3', np.float32, (3,)),
                ('attr', '<i2', (1,)),
            ])
            data = np.zeros((count_triangles,), dtype=record_doc_type)
            for i in range(0, count_triangles, 10):
                d = np.fromfile(f, dtype=record_doc_type, count=10)
                data[i:i + len(d)] = d

            # normals = data['Normals']
            v1 = data['Vertex1']
            v2 = data['Vertex2']
            v3 = data['Vertex3']
            points = np.hstack(((v1[:, np.newaxis, :]),
                                (v2[:, np.newaxis, :]),
                                (v3[:, np.newaxis, :])))
            points_set = []
            triangles = []
            for item in points:
                a = [-1, -1, -1]
                i = 0
                for poi in item:
                    if list(poi) not in points_set:
                        points_set.append(list(poi))
                        a[i] = len(points_set) - 1
                    else:
                        a[i] = points_set.index(list(poi))
                    i += 1

                triangles.append(a)
        return points_set, triangles
