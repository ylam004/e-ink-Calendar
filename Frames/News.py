from PIL import Image,ImageDraw,ImageFont
from Frames import Frame, API

class News(Frame.Frame):
    def out(self, draw):
        #Fonts
        newsFont = ImageFont.truetype('fonts/arial.ttf', 15)
        
        #Draw Frame
        super().out(draw)

        #Draw headlines
        headlines = self.newsApi()
        out = ''
        for i in range(3):
            if i < len(headlines):
                if i != 0:
                    out = out + '\n'
                temp = '> ' + headlines[i]
                if newsFont.getsize(temp)[0] > self.width:
                    spaces = temp.find(' ', 70)
                    if newsFont.getsize(temp[0:spaces])[0] > self.width:
                        spaces = temp.rfind(' ', 0, 70)
                    temp = temp[0:spaces] + '\n  ' + temp[spaces:]
                out = out + temp
        draw.text(((self.xMin + 3), (self.yMin + 0.05 * self.height)), out, font = newsFont, fill = 0)

    def newsApi(self):
        response = API.APICaller.APIcall('News')
        validSource = ['CNA', 'The Straits Times', 'TODAYonline', 'Business Times']
        headlines = []
        for i in range(len(response['articles'])):
            if response['articles'][i]['source']['name'] in validSource:
                temp = response['articles'][i]['title']
                headlines.append(temp)
        return headlines
                
                
