import back_app
import transfer_stl as tr

path = 'example_file.stl/'
name = 'Galleon.stl'

points, triangles = tr.from_stl(path + name)

app = back_app.Action_3D(points, triangles, title=name)


def animation():
    app.clear()
    app.update()
    app.mainloop()


if __name__ == "__main__":
    animation()
