class Face:

    def __init__(self, item):
        self.points = item[:-1]
        self.color = item[-1]
