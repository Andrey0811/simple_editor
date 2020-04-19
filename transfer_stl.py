import re

reg = re.compile(r'facet normal *(?P<x_n>.+) (?P<y_n>.+) (?P<z_n>.+)\n.*'
                 r'\n* *vertex *(?P<x1>.+) (?P<y1>.+) (?P<z1>.+)'
                 r'\n* *vertex *(?P<x2>.+) (?P<y2>.+) (?P<z2>.+)'
                 r'\n* *vertex *(?P<x3>.+) (?P<y3>.+) (?P<z3>.+)\n* *endloop\n* *endfacet')


def from_stl(name: str):
    points = []
    triangles = []
    with open(name, 'r') as f:
        lines = f.read()
        list_str = reg.findall(lines)
        for item in list_str:
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

    return points, triangles


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

