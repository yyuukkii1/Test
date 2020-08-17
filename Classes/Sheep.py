class Sheep:

    def __init__(self, x, y, speed, field):
        self.x = x
        self.y = y
        self.speed = speed
        self.field = field

    def Move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def PrintPosition(self):
        print("I am at: " + str(self.x) + ":" + str(self.y))  

    def PrintAllPositions(self):
        for s in self.field.Sheeps:
            print("I am at: " + str(s.x) + ":" + str(s.y)) 
