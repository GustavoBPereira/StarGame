from requests import get
from random import randint

def get_people():
    while True:
        people_id = randint(1,88)
        url_api = f'https://swapi.co/api/people/{people_id}'
        data = get(url_api) 

        json = data.json()

        name = json['name']
        height = json['height']
        if(name == 'unknown' or height == 'unknown'):
            continue
        else:
            break
        

    return {'name': name, 'height': height}