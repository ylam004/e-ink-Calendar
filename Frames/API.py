import requests
from datetime import datetime
from todoist.api import TodoistAPI
import keys

class APICaller:    
    @staticmethod
    def APIcall(caller):
        cur = datetime.now()
        
        
        if caller == 'Cal':
            return requests.get('https://calendarific.com/api/v2/holidays',\
                                params={'api_key':keys.CAL_API, 'country':'SG', 'year':str(cur.year)}\
                                ).json()
        
        elif caller == 'News':
            return requests.get('http://newsapi.org/v2/top-headlines',\
                                params={'country':'sg', 'apiKey':keys.NEWS_API}\
                                ).json()

        elif caller == 'Todo':
            todolist = []
            api = TodoistAPI(keys.TODO_API)
            api.sync()
            for i in range(len(api.state['items'])):
                temp = api.state['items'][i]
                if temp['checked'] == 0:
                    todolist.append([temp['content'],temp['due']['date']])
            return todolist

        elif caller == 'Weather':
            return requests.get('https://api.openweathermap.org/data/2.5/onecall',\
                                params={'lat':'1.370', 'lon':'103.955', 'exclude':'minutely,daily,current',\
                                'appid':keys.WEA_API, 'units':'metric'}\
                                ).json()
       
        

