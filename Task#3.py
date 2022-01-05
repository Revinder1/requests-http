import requests
from datetime import datetime
from pprint import pprint


def get_questions(days):
    current_date = int(datetime.timestamp(datetime.now()))  # Время в секундах, начиная с 1970 года по текущую секунду
    start_date = current_date - days * 86400  # В сутках 86400 секунд
    params = {
        'fromdate': start_date,
        'todate': current_date,
        'tagged': 'Python',
        'site': 'stackoverflow'
    }
    resp = requests.get('https://api.stackexchange.com/2.3/questions', params=params)
    resp.raise_for_status()
    for question in resp.json()['items']:
        print((question['title']))
        print('------------------------')
    # pprint(resp.json())


get_questions(2)
