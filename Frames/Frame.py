from PIL import Image,ImageDraw,ImageFont

class Frame:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.boder(0, 1)
        self.infill = 1

    def boder(self, Size, fill):
        self.boderSize = Size
        self.xMin = self.x1 + self.boderSize
        self.yMin = self.y1 + self.boderSize
        self.xMax = self.x2 - self.boderSize
        self.yMax = self.y2 - self.boderSize              
        self.width = self.xMax - self.xMin 
        self.height = self.yMax - self.yMin
        self.boderFill = fill

    def fill(self, fill):
        self.infill = fill

    def out(self, draw):
        if self.boderSize == 0:
            draw.rectangle((self.x1, self.y1, self.x2, self.y2), fill = self.infill, outline = 0)
        else:
            draw.rectangle((self.x1, self.y1, self.x2, self.y2), fill = self.boderFill, outline = 0)
            draw.rectangle((self.xMin, self.yMin, self.xMax, self.yMax), fill = self.infill, outline = 0)



        


        

        



        
        

        

