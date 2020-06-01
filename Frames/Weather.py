from PIL import Image,ImageDraw,ImageFont
from datetime import datetime
from Frames import Frame, API

class Weather(Frame.Frame):
    def out(self, draw):
        #Draw Frame
        super().out(draw)
        
        #Fonts
        wFont = ImageFont.truetype('fonts/arial.ttf', 15)
        wIcons = ImageFont.truetype('fonts/meteocons-webfont.ttf', 35)
        icons_list = {u'01d':u'B',u'01n':u'C',u'02d':u'H',u'02n':u'I',u'03d':u'N',u'03n':u'N',u'04d':u'Y',u'04n':u'Y',u'09d':u'R',\
                      u'09n':u'R',u'10d':u'R',u'10n':u'R',u'11d':u'P',u'11n':u'P',u'13d':u'W',u'13n':u'W',u'50d':u'M',u'50n':u'W'}   

        #Draw weather
        weather = self.weatherApi();
        draw.text(((self.xMin + 40 - wFont.getsize(weather[0])[0]/2), (self.yMin + 0.10*self.height)), weather[0], font = wFont, fill = 0)
        draw.text(((self.xMin + 40 - wIcons.getsize(icons_list[weather[1]])[0]/2), (self.yMin + 0.32*self.height)), icons_list[weather[1]], font = wIcons, fill = 0)
        draw.text(((self.xMin + 40 - wFont.getsize(weather[2]+'°C')[0]/2), (self.yMin + 0.75*self.height)), weather[2]+'°C', font = wFont, fill = 0)

        draw.text(((self.xMin + 110 - wFont.getsize(weather[3])[0]/2), (self.yMin + 0.10*self.height)), weather[3], font = wFont, fill = 0)
        draw.text(((self.xMin + 110 - wIcons.getsize(icons_list[weather[4]])[0]/2), (self.yMin + 0.32*self.height)), icons_list[weather[4]], font = wIcons, fill = 0)
        draw.text(((self.xMin + 110 - wFont.getsize(weather[5]+'°C')[0]/2), (self.yMin + 0.75*self.height)), weather[5]+'°C', font = wFont, fill = 0)
        
        draw.text(((self.xMin + 180 - wFont.getsize(weather[6])[0]/2), (self.yMin + 0.10*self.height)), weather[6], font = wFont, fill = 0)
        draw.text(((self.xMin + 180 - wIcons.getsize(icons_list[weather[7]])[0]/2), (self.yMin + 0.32*self.height)), icons_list[weather[7]], font = wIcons, fill = 0)
        draw.text(((self.xMin + 180 - wFont.getsize(weather[8]+'°C')[0]/2), (self.yMin + 0.75*self.height)), weather[8]+'°C', font = wFont, fill = 0)

        draw.text(((self.xMin + 250 - wFont.getsize(weather[9])[0]/2), (self.yMin + 0.10*self.height)), weather[9], font = wFont, fill = 0)
        draw.text(((self.xMin + 250 - wIcons.getsize(icons_list[weather[10]])[0]/2), (self.yMin + 0.32*self.height)), icons_list[weather[10]], font = wIcons, fill = 0)
        draw.text(((self.xMin + 250 - wFont.getsize(weather[11]+'°C')[0]/2), (self.yMin + 0.75*self.height)), weather[11]+'°C', font = wFont, fill = 0)

    def weatherApi(self):
        weather_response = API.APICaller.APIcall('Weather')
        output = []
        time = [3, 6, 12, 24]
            
        for i in time:
            weather = weather_response.get('hourly')[i]
            weather_time = datetime.utcfromtimestamp(weather.get('dt') + weather_response.get('timezone_offset')).strftime('%H:%M')
            weather_icon = weather.get('weather')[0].get('icon')
            weather_temp = '{0:.2f}'.format(weather.get('temp'))
            output.append(weather_time)
            output.append(weather_icon)
            output.append(weather_temp)
            
        return output
            

        
    
