from PIL import Image,ImageDraw,ImageFont
from Frames import Frame, API
import datetime

class Todo(Frame.Frame):
    def out(self, draw):
        #Fonts
        titleFont = ImageFont.truetype('fonts/arial.ttf', 24)
        textFont = ImageFont.truetype('fonts/arial.ttf', 18)
        
        #Draw Frame
        super().out(draw)

        #Draw Tasks
        noOfTasks = 7
        todolist = API.APICaller.APIcall('Todo')
        j = noOfTasks +1
        for i in range(j):
            if i == 0:
                draw.rectangle((self.xMin, self.yMin+i/j*(self.height), self.xMax, self.yMin+(i+1)/j*(self.height)), fill = 0, outline = 0)
                draw.text(((self.xMin + 0.02*self.width), (self.yMin + 0.02*self.height)), 'TO DO LIST', font = titleFont, fill = 1)
                draw.text(((self.xMin + 0.69*self.width), (self.yMin + 0.02*self.height)), 'DUE DATE', font = titleFont, fill = 1)
            else:
                draw.rectangle((self.xMin, self.yMin+i/j*(self.height), self.xMax, self.yMin+(i+1)/j*(self.height)), fill = 1, outline = 0)
                if i<=len(todolist):
                    draw.text(((self.xMin + 0.02*self.width), (self.yMin+i/j*(self.height)+8)), str(i)+'. '+ todolist[i-1][0], font = textFont, fill = 0)
                    temp = todolist[i-1][1].split('-')
                    date = datetime.date(int(temp[0]), int(temp[1]), int(temp[2]))
                    draw.text(((self.xMin + 0.7*self.width), (self.yMin+i/j*(self.height)+8)), '{0:%d} {0:%B} {0:%Y}'.format(date), font = textFont, fill = 0)
                else:
                    draw.text(((self.xMin + 0.02*self.width), (self.yMin+i/j*(self.height)+8)), str(i)+'. ', font = textFont, fill = 0)
                
        return todolist
