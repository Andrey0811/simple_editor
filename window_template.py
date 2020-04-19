import tkinter
import easygui
import transfer_stl as tr


class Window_template:

    def __init__(self, width: int, height: int, title: str, background: str, outline_color='black'):
        self.zeros = [int(width/2), int(height/2)]
        self.window = tkinter.Tk()
        self.window.title(title)
        self.image = tkinter.Canvas(self.window, width=width, height=height, bg=background)
        self.image.pack()
        btn = tkinter.Button(self.window, text='Open File', command=self.clicked)
        btn.pack(side='right', padx=5, pady=5)
        self.outline_color = outline_color
    
    def create_shape(self, points: list, color: str):
        coords = []
        for point in points:
            coords.append(point[0] + self.zeros[0])
            coords.append(point[1] + self.zeros[1])
        self.image.create_polygon(coords, fill=color, outline=self.outline_color)

    def clicked(self):
        return tr.from_stl(easygui.fileopenbox(filetypes=['*.stl']))
        #pass

    def clear(self):
        self.image.delete('all')

    def mainloop(self):
        self.window.mainloop()
