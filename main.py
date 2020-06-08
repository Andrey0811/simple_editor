from work_with_stl import work_with_stl as tr
from window import window as w

path = 'example_file.stl/'
name = 'cube.stl'

# path = 'work_with_stl/'
# name = 'Bone_Golem.stl'

points, triangles = tr.work_with_stl.from_stl(path + name)
# points, triangles = tr.work_with_stl.from_binary_stl(path + name)

window = w.window_templ(points, triangles, title=name)


def animation():
    window.clear()
    window.update()
    window.mainloop()


if __name__ == "__main__":
    animation()
