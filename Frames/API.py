import requests
from datetime import datetime
from todoist.api import TodoistAPI

class APICaller:    
    @staticmethod
    def APIcall(caller):
        cur = datetime.now()
        CAL_API = <API Key> #calendarific.com
        NEWS_API = <API Key> #newsapi.org
        TODO_API = <API Key> #Todoist
        WEA_API = <API Key> #openweathermap.org
        
        if caller == 'Cal':
            return requests.get('https://calendarific.com/api/v2/holidays',\
                                params={'api_key':CAL_API, 'country':'SG', 'year':str(cur.year)}\
                                ).json()
        
        elif caller == 'News':
            return requests.get('http://newsapi.org/v2/top-headlines',\
                                params={'country':'sg', 'apiKey':NEWS_API}\
                                ).json()

        elif caller == 'Todo':
            todolist = []
            api = TodoistAPI(TODO_API)
            api.sync()
            for i in range(len(api.state['items'])):
                temp = api.state['items'][i]
                if temp['checked'] == 0:
                    todolist.append([temp['content'],temp['due']['date']])
            return todolist

        elif caller == 'Weather':
            return requests.get('https://api.openweathermap.org/data/2.5/onecall',\
                                params={'lat':'1.370', 'lon':'103.955', 'exclude':'minutely,daily,current',\
                                'appid':WEA_API, 'units':'metric'}\
                                ).json()
       
        

