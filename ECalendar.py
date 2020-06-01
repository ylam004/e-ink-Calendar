from PIL import Image,ImageDraw,ImageFont
from datetime import datetime
import Frames
import time
import PIInterface as PI
import logging

logging.basicConfig(filename = 'cal_logs',\
                        filemode = 'a',\
                        format = '%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',\
                        datefmt = '%H:%M:%S',\
                        level = logging.DEBUG)

def update(draw):
    #Fonts
    check_todo = todo.out(draw)
    global lastTodo

    if (lastUpdate == None) or (datetime.now().day != lastUpdate.day):
        #Update frames
        weather.out(draw)
        calendar.out(draw)
        news.out(draw)
        lastTodo = check_todo
        return True

    elif datetime.now().hour != lastUpdate.hour:
        weather.out(draw)
        news.out(draw)
        lastTodo = check_todo
        return True

    elif lastTodo != check_todo:
        lastTodo = check_todo
        return True

    else:
        return False
        
if __name__ == '__main__':
    #----------------------------------------------Initialise----------------------------------------------#
    lastUpdate = None
    lastTodo = None

    #Fonts
    timeFont = ImageFont.truetype('fonts/arial.ttf', 12)
    
    #Dimensions
    WIDTH = 800
    HEIGHT = 480

    #Image drawer
    imageOut = Image.new('1', (WIDTH, HEIGHT), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(imageOut)

    #Grid lines
    x_1 = 5
    x_2 = 300
    x_3 = 795
    y_1 = 5
    y_2 = 85
    y_3 = 345
    y_4 = 465

    #Frames
    weather = Frames.Weather.Weather(x_2, y_1, x_3, y_2)
    weather.boder(2, 1)
    calendar = Frames.Cal.Cal(x_1, y_1, x_2, y_4)
    calendar.fill(0)
    news = Frames.News.News(x_2, y_3, x_3, y_4)
    news.boder(2, 1)
    todo = Frames.Todo.Todo(x_2, y_2, x_3, y_3)
    todo.boder(2, 1)

    while True:
        try:
            logging.info('Checking for updates')
            if update(draw):
                #Update time
                lastUpdate = datetime.now()
                draw.rectangle((660, 466, 800, 480), fill = 1)
                draw.text((660, 466), 'Last updated at {0:%I:%M%p}'.format(lastUpdate), font = timeFont, fill = 0)
                #Print image
                imageOut.show()
                PI.printOut(imageOut)
            
        except Exception as e:
            print(e)
            
        finally:
            time.sleep(300)
      


