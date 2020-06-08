from tkinter import *
import easygui
from .geometry import engine as e


class MainGui:

    def __init__(self, points, shapes, distance=5, scale=10,
                 width: int = 1000, height: int = 600,
                 title: str = '3D Scene',
                 background: str = 'white', outline_color='black'):
        self.zeros = [int((width - 200) / 2), int((height - 200) / 2)]
        self.engine = e.engine(points, shapes, distance, scale)

        self.window = Tk()
        self.window.title(title)
        self.window.minsize(width, height)
        self.window.bind('<ButtonRelease-1>', self.reset_event)
        self.window.bind('<MouseWheel>', self.mouse_scale)
        self.window.bind_all('<Key>', self.key_press)
        self.window.bind('<B1-Motion>', self.do_event)
        self.outline_color = outline_color

        self.image = Canvas(self.window, width=width - 200, height=height - 200, bg=background)
        self.image.pack(side='right')
        # self.image.bind('<Configure>', self.updateCanvasCoords)

        self.btn = Button(self.window, text='Open File', command=self.clicked)
        self.btn.pack(side='right', padx=5, pady=5)

        self.outer_frame = Frame(self.window)
        self.outer_frame.pack(fill='both', expand=True)

        self.selection_panel = Frame(self.outer_frame, height=200, width=200)
        self.selection_panel.pack(side='left', fill=Y, expand=0, anchor=W)

        # self.lighting_button = Button(self.selection_panel, text='Toggle Lighting', fg='blue', command=self.toggle_lighting)
        # self.lighting_button.pack(fill=X, expand=0)

        # self.shading_button = Button(self.selection_panel, text='Toggle Shading', fg='blue', command=self.toggle_shading)
        # self.shading_button.pack(fill=X, expand=0)

        # self.create_pyramid_button = Button(self.selection_panel, text='New Pyramid', fg='green', command=self.make_pyramid)
        # self.create_pyramid_button.pack(fill=X, expand=0)

        # self.create_cylinder_button = Button(self.selection_panel, text='New Cylinder', fg='green', command=self.make_cylinder)
        # self.create_cylinder_button.pack(fill=X, expand=0)

        # self.create_cube_button = Button(self.selection_panel, text='New Cube', fg='green', command=self.make_cube)
        # self.create_cube_button.pack(fill=X, expand=0)

        # self.delete_figure_button = Button(self.selection_panel, text='Delete Figure', fg='red', command=self.delete_figure)
        # self.delete_figure_button.pack(fill=X, expand=0)

        self.right_frame = Frame(self.outer_frame)
        self.right_frame.pack(side='right', fill='both', expand=True)

        self.control_panel = Frame(self.right_frame, height=400)
        self.control_panel.pack(side='bottom')

        self.scrollbar = Scrollbar(self.selection_panel, orient='vertical')
        self.l = Listbox(self.selection_panel, selectmode=EXTENDED, height=30,
                         yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.l.yview)
        self.scrollbar.pack(side='right', fill='y')
        # self.l.bind('<<ListboxSelect>>', self.on_selection_changed)
        self.l.pack(fill='both', expand=True)

        self.reset_controls = Frame(self.control_panel, height=400, borderwidth=2, relief=RIDGE)
        self.reset_controls.pack(side='top')

        # self.reset_button = Button(self.reset_controls, text='Reset', fg='red', command=self.reset)
        # self.reset_button.pack(side='left')

        self.scale_controls_steps = Frame(self.control_panel, borderwidth=4, relief=RIDGE)
        self.scale_controls_steps.pack(side='left')

        self.scale_up_button = Button(self.scale_controls_steps, text='▲',
                                      command=self.change_scale_step_size_up,
                                      repeatdelay=500,
                                      repeatinterval=25)
        self.scale_up_button.pack(side='top')

        self.scale_controls_steps_label = Label(self.scale_controls_steps, text='1')
        # scale_controls_steps_label.bind('<Button-1>', self.reset_scale_step_size)
        self.scale_controls_steps_label.pack()

        self.scale_down_button = Button(self.scale_controls_steps, text='▼',
                                        command=self.change_scale_step_size_down,
                                        repeatdelay=500,
                                        repeatinterval=25)
        self.scale_down_button.pack(side='bottom')

        self.scale_controls = Frame(self.control_panel, borderwidth=4, relief=RIDGE)
        self.scale_controls.pack(side='left')

        self.scale_controls_label = Label(self.scale_controls, text='Scale', fg="green")
        self.scale_controls_label.pack(side='top')

        self.translation_controls_steps = Frame(self.control_panel, borderwidth=4, relief=RIDGE)
        self.translation_controls_steps.pack(side='left')

        self.translation_up_button = Button(self.translation_controls_steps, text='▲',
                                            command=self.change_translation_step_size_up,
                                            repeatdelay=500,
                                            repeatinterval=50)
        self.translation_up_button.pack(side='top')

        self.translation_controls_steps_label = Label(self.translation_controls_steps, text='5')
        # self.translation_controls_steps_label.bind('<Button-1>', self.reset_translation_step_size)
        self.translation_controls_steps_label.pack()

        self.translation_down_button = Button(self.translation_controls_steps, text='▼',
                                              command=self.change_translation_step_size_down,
                                              repeatdelay=500, repeatinterval=50)
        self.translation_down_button.pack(side='bottom')

        self.translate_controls = Frame(self.control_panel, borderwidth=4, relief=RIDGE)
        self.translate_controls.pack(side='left')

        self.translate_controls_label = Label(self.translate_controls, text='Translation', fg='green')
        self.translate_controls_label.pack()

        self.translate_control_supper = Frame(self.translate_controls)
        self.translate_control_supper.pack()

        self.translate_controls_lower = Frame(self.translate_controls)
        self.translate_controls_lower.pack()

        self.backward_button = Button(self.translate_control_supper, text='⟱',
                                      command=self.backward,
                                      repeatdelay=500, repeatinterval=50)
        self.backward_button.pack(side='left')

        self.up_button = Button(self.translate_control_supper, text='↑',
                                command=self.up, repeatdelay=500,
                                repeatinterval=50)
        self.up_button.pack(side='left')

        self.forward_button = Button(self.translate_control_supper, text='⟰',
                                     command=self.forward, repeatdelay=500,
                                     repeatinterval=50)
        self.forward_button.pack(side='left')

        self.leftButton = Button(self.translate_controls_lower, text='←',
                                 command=self.left, repeatdelay=500,
                                 repeatinterval=50)
        self.leftButton.pack(side='left')

        self.up_button = Button(self.translate_controls_lower, text='↓',
                                command=self.down, repeatdelay=500,
                                repeatinterval=50)
        self.up_button.pack(side='left')

        self.right_button = Button(self.translate_controls_lower, text='→',
                                   command=self.right, repeatdelay=500,
                                   repeatinterval=50)
        self.right_button.pack(side='left')

        self.rotation_controls_steps = Frame(self.control_panel, borderwidth=4, relief=RIDGE)
        self.rotation_controls_steps.pack(side='left')

        self.rotation_up_button = Button(self.rotation_controls_steps, text='▲',
                                         command=self.change_rotation_step_size_up, repeatdelay=500,
                                         repeatinterval=50)
        self.rotation_up_button.pack(side='top')

        self.rotation_controls_steps_label = Label(self.rotation_controls_steps, text='0.25')
        # self.rotation_controls_steps_label.bind('<Button-1>', self.reset_rotation_step_size)
        self.rotation_controls_steps_label.pack()

        self.rotation_down_button = Button(self.rotation_controls_steps, text='▼',
                                           command=self.change_rotation_step_size_down,
                                           repeatdelay=500,
                                           repeatinterval=50)
        self.rotation_down_button.pack(side='bottom')

        self.rotation_controls = Frame(self.control_panel, borderwidth=4, relief=RIDGE)
        self.rotation_controls.pack(side='left')

        self.rotation_controls_label = Label(self.rotation_controls, text='Rotation', fg='green')
        self.rotation_controls_label.pack()

        self.rotation_controls_x = Frame(self.rotation_controls)
        self.rotation_controls_x.pack(side='left')

        self.rotation_controls_y = Frame(self.rotation_controls)
        self.rotation_controls_y.pack(side='left')

        self.rotation_controls_z = Frame(self.rotation_controls)
        self.rotation_controls_z.pack(side='left')

        self.x_plus_button = Button(self.rotation_controls_x, text='X+',
                                    command=self.x_plus, repeatdelay=500,
                                    repeatinterval=50)
        self.x_plus_button.pack(side='top')

        self.x_minus_button = Button(self.rotation_controls_x, text='X-',
                                     command=self.x_sub, repeatdelay=500,
                                     repeatinterval=50)
        self.x_minus_button.pack(side='bottom')

        self.y_plus_button = Button(self.rotation_controls_y, text='Y+',
                                    command=self.y_plus, repeatdelay=500,
                                    repeatinterval=50)
        self.y_plus_button.pack(side='top')

        self.y_minus_button = Button(self.rotation_controls_y, text='Y-',
                                     command=self.y_sub, repeatdelay=500,
                                     repeatinterval=50)
        self.y_minus_button.pack(side='bottom')

        self.z_plus_button = Button(self.rotation_controls_z, text='Z+',
                                    command=self.z_plus, repeatdelay=500,
                                    repeatinterval=50)
        self.z_plus_button.pack(side='top')

        self.z_minus_button = Button(self.rotation_controls_z, text='Z-',
                                     command=self.z_sub, repeatdelay=500,
                                     repeatinterval=50)
        self.z_minus_button.pack(side='bottom')

    def create_shape(self, points: list, color: str):
        coords = []
        for point in points:
            coords.append(point[0] + self.zeros[0])
            coords.append(point[1] + self.zeros[1])
        self.image.create_polygon(coords, fill=color, outline=self.outline_color)

    def update(self):
        points = []
        for point in self.engine.points:
            points.append(point.flatten(self.engine.scale, self.engine.distance))

        shapes = []
        for shape in self.engine.shapes:
            avg_z = 0
            temp = []
            for point in shape.points:
                avg_z -= self.engine.points[point].z
                temp.append(points[point])
            temp.append(shape.color)
            temp.append(avg_z / len(shape.points))
            shapes.append(temp)

        shapes = sorted(shapes, key=lambda x: x[-1])

        for shape in shapes:
            self.create_shape(shape[0:-2], shape[-2])

    def do_event(self, event):
        if self.engine.prev_event:
            self.engine.rotate(0, (event.y - self.engine.prev_event[1]) / 20)
            self.engine.rotate(1, (event.x - self.engine.prev_event[0]) / 20)
            self.clear()
            self.update()
        self.engine.prev_event = [event.x, event.y]

    def reset_event(self, event):
        self.engine.prev_event = []

    def key_press(self, event):
        if event.keysym == 'Up':
            self.engine.rotate(0, -self.engine.rotation_step)
        elif event.keysym == 'Down':
            self.engine.rotate(0, self.engine.rotation_step)
        elif event.keysym == 'Right':
            self.engine.rotate(1, self.engine.rotation_step)
        elif event.keysym == 'Left':
            self.engine.rotate(1, -self.engine.rotation_step)
        elif event.keysym == 'w':
            self.engine.move(0, -self.engine.translation_step, 0)
        elif event.keysym == 's':
            self.engine.move(0, self.engine.translation_step, 0)
        elif event.keysym == 'a':
            self.engine.move(-self.engine.translation_step, 0, 0)
        elif event.keysym == 'd':
            self.engine.move(self.engine.translation_step, 0, 0)
        elif event.keysym == 'p':
            self.engine.scale += self.engine.forward_value
        elif event.keysym == 'o' and self.engine.scale > 1:
            self.engine.scale -= self.engine.forward_value
        elif event.keysym == 'e':
            points, triangles = self.clicked()
            self.engine.points = []
            self.engine.shapes = []
            self.engine.add_points(points)
            self.engine.add_faces(triangles)
        self.clear()
        self.update()

    def clicked(self):
        return self.engine.from_stl(easygui.fileopenbox(filetypes=['*.stl']))

    def mouse_scale(self, event):
        self.engine.scale += event.delta / 60
        self.clear()
        self.update()

    def clear(self):
        self.image.delete('all')

    def mainloop(self):
        self.window.mainloop()

    # TODO
    # def update_canvas_coords(self, event):
    #     pass

    # TODO
    # def update_title_bar(self):
    #     pass

    # TODO
    # def toggle_lighting(self):
    #     pass

    # TODO
    # def toggle_shading(self):
    #     pass

    def forward(self):
        self.engine.scale *= self.engine.forward_value
        self.clear()
        self.update()

    def backward(self):
        self.engine.scale *= self.engine.forward_value
        self.clear()
        self.update()

    def left(self):
        self.engine.move(-self.engine.translation_step, 0, 0)
        self.clear()
        self.update()

    def right(self):
        self.engine.move(self.engine.translation_step, 0, 0)
        self.clear()
        self.update()

    def up(self):
        self.engine.move(0, -self.engine.translation_step, 0)
        self.clear()
        self.update()

    def down(self):
        self.engine.move(0, self.engine.translation_step, 0)
        self.clear()
        self.update()

    def x_plus(self):
        self.engine.rotate(1, self.engine.rotation_step)
        self.clear()
        self.update()

    def x_sub(self):
        self.engine.rotate(1, -self.engine.rotation_step)
        self.clear()
        self.update()

    def y_plus(self):
        self.engine.rotate(0, self.engine.rotation_step)
        self.clear()
        self.update()

    def y_sub(self):
        self.engine.rotate(0, -self.engine.rotation_step)
        self.clear()
        self.update()

    def z_plus(self):
        self.engine.rotate(2, self.engine.rotation_step)
        self.clear()
        self.update()

    def z_sub(self):
        self.engine.rotate(2, -self.engine.rotation_step)
        self.clear()
        self.update()

    # TODO
    # def make_pyramid(self):
    #     self.clear()
    #     self.update()

    # def make_cube(self):
    #     self.clear()
    #     self.update()

    # TODO
    # def make_cylinder(self):
    #     self.clear()
    #     self.update()

    # def delete_figure(self):
    #     self.clear()
    #     self.update()

    def change_rotation_step_size_down(self):
        self.engine.rotation_step -= 0.25
        self.rotation_controls_steps_label.text = str(self.engine.rotation_step)
        self.rotation_controls_steps_label.pack()

    def change_rotation_step_size_up(self):
        self.engine.rotation_step += 0.25
        self.rotation_controls_steps_label.text = str(self.engine.rotation_step)
        self.rotation_controls_steps_label.pack()

    # TODO
    # def reset_rotation_step_size(self):
    #     pass

    def change_translation_step_size_down(self):
        self.engine.translation_step -= 0.25
        self.translation_controls_steps_label.text = str(self.engine.translation_step)
        self.translation_controls_steps_label.pack()

    def change_translation_step_size_up(self):
        self.engine.translation_step += 0.25
        self.translation_controls_steps_label.text = str(self.engine.translation_step)
        self.translation_controls_steps_label.pack()

    # TODO
    # def reset_translation_step_size(self):
    #     pass

    def change_scale_step_size_down(self):
        self.engine.forward_value -= 0.1
        self.scale_controls_steps_label.text = str(self.engine.forward_value)
        self.scale_controls_steps_label.pack()

    def change_scale_step_size_up(self):
        self.engine.forward_value += 0.1
        self.scale_controls_steps_label.text = str(self.engine.forward_value)
        self.scale_controls_steps_label.pack()

    # TODO
    # def reset_scale_step_size(self):
    #     pass

    # TODO
    # def reset(self):
    #     pass

    # TODO
    # def on_selection_changed(self):
    #     pass
