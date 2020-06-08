from src.geometry import engine as e
from src import main_gui as w

path = 'samples/'
name = 'Galleon.stl'

# path = 'work_with_stl/'
# name = 'Bone_Golem.stl'

points, triangles = e.engine.from_stl(path + name)
# points, triangles = e.from_binary_stl(path + name)

window = w.MainGui(points, triangles, title=name)


def animation():
    window.clear()
    window.update()
    window.mainloop()


if __name__ == "__main__":
    animation()
