from PIL import Image,ImageDraw,ImageFont
from datetime import datetime
import calendar
from Frames import Frame, API

class Cal(Frame.Frame):
    def out(self, draw):
        cur = datetime.now() #Current date and time
        cal = calendar.Calendar(6).monthdayscalendar(2020, cur.month) #Get lists of weeks
        #Fonts
        calFont = ImageFont.truetype('fonts/arial.ttf', 13)
        dayFont = ImageFont.truetype('fonts/arial.ttf', 54)
        dateFont = ImageFont.truetype('fonts/arial.ttf', 80)
        monthFont = ImageFont.truetype('fonts/arial.ttf', 40)
        
        #Draw Frame
        super().out(draw)

        #Draw date
        draw.text((((self.width-dayFont.getsize('{0:%A}'.format(cur))[0])/2 + self.xMin), (self.yMin + 0.02*self.height)), '{0:%A}'.format(cur), font = dayFont, fill = (self.infill+1)%2) #Day of the week
        draw.text((((self.width-dateFont.getsize('{0:%d}'.format(cur))[0])/2 + self.xMin), (self.yMin + 0.16*self.height)), '{0:%d}'.format(cur), font = dateFont, fill = (self.infill+1)%2) #Day of the week
        draw.text((((self.width-monthFont.getsize('{0:%B} {0:%Y}'.format(cur))[0])/2 + self.xMin), (self.yMin + 0.35*self.height)), '{0:%B} {0:%Y}'.format(cur), font = monthFont, fill = (self.infill+1)%2) #Date
        
        #Record horizontal line
        y_border = 55
        y_coord = [self.yMax - y_border]#Bottom to top
        for i in range(7):
            y_coord.append(self.yMax - y_border - (i+1)*0.06*self.height)

        #Record vertical line
        x_border = 30
        x_coord = [self.xMin+x_border]#left to right
        for i in range(6):
            x_coord.append(self.xMin +x_border + (i+1)/7*(self.width-2*x_border))
        x_coord.append(self.xMax-x_border)

        #Draw Text
        days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
        for i in range(7):
            #Find center alignment
            wtemp, htemp = calFont.getsize(days[i])
            xloc = (x_coord[i+1] - x_coord[i] - wtemp)/2 + x_coord[i]
            yloc = (y_coord[-2] - y_coord[-1] - htemp)/2 + y_coord[-1]
            draw.text((xloc, yloc), days[i], font = calFont, fill = (self.infill+1)%2)
            
        #Draw Numbers
        for i in range(len(cal)):
            for j in range(7):
                if cal[i][j] != 0:
                    wtemp, htemp = calFont.getsize(str(cal[i][j]))
                    xcen = (x_coord[j+1] - x_coord[j])/2 + x_coord[j]
                    ycen = (y_coord[-3-i] - y_coord[-2-i])/2 + y_coord[-2-i]
                    xloc = xcen - wtemp/2 
                    yloc = ycen - htemp/2 
                    if cal[i][j] == cur.day:
                        draw.ellipse((xcen-10, ycen-10, xcen+10, ycen+10), fill = (self.infill+1)%2)
                        draw.text((xloc, yloc), str(cal[i][j]), font = calFont, fill = (self.infill)%2)
                    else:
                        draw.text((xloc, yloc), str(cal[i][j]), font = calFont, fill = (self.infill+1)%2)
        draw.line((self.xMin+x_border, self.yMax - y_border, self.xMax-x_border, self.yMax - y_border), fill = (self.infill+1)%2)

        #Add Holidays
        holiday = self.holidayApi()
        if holiday[1] == []:
            draw.text((self.xMin+x_border, self.yMax - y_border), 'Upcoming Holiday: \n\n  ' + 'New Year\'s Day'\
                      + '                        ' + '{0:%d} {0:%B}'.format(datetime(2021, 1, 1)), font = calFont, fill = (self.infill+1)%2)
        else:
            draw.text((self.xMin+x_border, self.yMax - y_border), 'Upcoming Holiday: \n\n  ' + holiday[1][0]['name']\
                      + '                        ' + '{0:%d} {0:%B}'.format(holiday[1][0]['date']), font = calFont, fill = (self.infill+1)%2)

    def holidayApi(self):
        cur = datetime.now() #Current date and time
        holiday_response = API.APICaller.APIcall('Cal')['response']['holidays']
        cur_mth_hol = []
        nxt_hol = []
        for i in range(len(holiday_response)):
            if holiday_response[i]['type'][0] == 'Season' or holiday_response[i]['type'][0] == 'Observance':
                continue
            if holiday_response[i]['date']['datetime']['month']<cur.month:
                continue
            elif holiday_response[i]['date']['datetime']['month'] == cur.month:
                cur_mth_hol.append(holiday_response[i]['date']['datetime']['day'])
                if holiday_response[i]['date']['datetime']['day'] >= cur.day:
                    dt = datetime(holiday_response[i]['date']['datetime']['year'],holiday_response[i]['date']['datetime']['month'],holiday_response[i]['date']['datetime']['day'])
                    nxt_hol.append({'name':holiday_response[i]['name'], 'date':dt})
            elif nxt_hol == []:
                dt = datetime(holiday_response[i]['date']['datetime']['year'],holiday_response[i]['date']['datetime']['month'],holiday_response[i]['date']['datetime']['day'])
                nxt_hol.append({'name':holiday_response[i]['name'], 'date':dt})
            else:
                break
        return [cur_mth_hol, nxt_hol]
        
