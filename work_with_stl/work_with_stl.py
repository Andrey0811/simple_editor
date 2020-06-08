import re
import numpy as np
from struct import unpack


reg = re.compile(r'facet normal *(?P<x_n>.+) (?P<y_n>.+) (?P<z_n>.+)\n.*'
                 r'\n* *vertex *(?P<x1>.+) (?P<y1>.+) (?P<z1>.+)'
                 r'\n* *vertex *(?P<x2>.+) (?P<y2>.+) (?P<z2>.+)'
                 r'\n* *vertex *(?P<x3>.+) (?P<y3>.+) (?P<z3>.+)\n* *endloop\n* *endfacet')

reg_light = re.compile(r'v\w* *(?P<x1>.+) (?P<y1>.+) (?P<z1>.+)')


class work_with_stl:

    @staticmethod
    def from_stl(name: str):
        points = []
        triangles = []
        #idx = 0
        with open(name, 'r') as f:
            lines = f.read()
            list_str = reg.findall(lines)
            print(len(list_str))
            for item in list_str:
                #idx += 1
                a = [-1, -1, -1]
                for i in range(3):
                    temp = [float(item[3 + 3 * i]), float(item[4 + 3 * i]), float(item[5 + 3 * i])]
                    if not temp in points:
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
                #print(idx)

        return points, triangles

    @staticmethod
    def to_stl(points: list, triangles: list, name='file_1.stl', path='example_file.stl/'):
        with open(path + name, 'w') as f:
            f.write(f'solid {name}\n')
            for triangle in triangles:
                f.write(f' facet normal  0.000000e+00 0.000000e+00  0.000000e+00\n  outer loop\n'
                        f'   vertex {points[triangle[0]][0]} {points[triangle[0]][1]} {points[triangle[0]][2]}\n'
                        f'   vertex {points[triangle[1]][0]} {points[triangle[1]][1]} {points[triangle[1]][2]}\n'
                        f'   vertex {points[triangle[2]][0]} {points[triangle[2]][1]} {points[triangle[2]][2]}\n'
                        f'  endloop\n endfacet\n')
            f.write('endsolid')

    @staticmethod
    def from_binary_stl(name: str):
        with open(name, "rb") as f:
            header = f.read(80)
            count_triangles = unpack('i', f.read(4))[0]
            record_dtype = np.dtype([
                ('Normals', np.float32, (3,)),
                ('Vertex1', np.float32, (3,)),
                ('Vertex2', np.float32, (3,)),
                ('Vertex3', np.float32, (3,)),
                ('attr', '<i2', (1,)),
            ])
            data = np.zeros((count_triangles,), dtype=record_dtype)
            for i in range(0, count_triangles, 10):
                d = np.fromfile(f, dtype=record_dtype, count=10)
                data[i:i + len(d)] = d

            # можно не запаковывать в точки, а сразу их анализировать, но это не особо время скоратит
            # normals = data['Normals']
            v1 = data['Vertex1']
            v2 = data['Vertex2']
            v3 = data['Vertex3']
            points = np.hstack(((v1[:, np.newaxis, :]), (v2[:, np.newaxis, :]), (v3[:, np.newaxis, :])))
            points_set = []
            triangles = []
            idx = 0
            for item in points:
                idx += 1
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
                print(idx)

        return points_set, triangles
