class Terrain:

    def __init__(self, size):
        self.x = size[0]
        self.y = size[1]
        self.objects = []

    def add(self, obj):
        self.objects.append(obj)

    def update(self):
        #update all objects?
        pass
