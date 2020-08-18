class Sheep:

    def __init__(self, x, y, speed, field):
        self.x = x
        self.y = y
        self.speed = speed
        self.field = field

    

    def PrintPosition(self):
        print("I am at: " + str(self.x) + ":" + str(self.y))  

    def PrintAllPositions(self):
        for s in self.field.Sheeps:
            print("I am at: " + str(s.x) + ":" + str(s.y)) 


    def Move(self, dir):
        if dir == 0:
            self.y = self.y + self.speed 
        elif dir == 1:
            self.y = self.y + round(self.speed/1.4)
            self.x = self.x + round(self.speed/1.4)
        elif dir == 2:
            self.x = self.x + self.speed   
        elif dir == 3:
            self.y = self.y - round(self.speed/1.4)
            self.x = self.x + round(self.speed/1.4)
        elif dir == 4:
            self.y = self.y - self.speed
        elif dir == 5:
            self.y = self.y - round(self.speed/1.4)
            self.x = self.x - round(self.speed/1.4)
        elif dir == 6:
            self.x = self.x - self.speed
        elif dir == 7:
            self.y = self.y + round(self.speed/1.4)
            self.x = self.x - round(self.speed/1.4)    

             
             
              
