from bs4 import BeautifulSoup
import requests
import re
url = 'https://www.imdb.com/list/ls005750764/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
movies = soup.find('h3', attrs={'class':'lister-item-header'} )
name = movies.text.strip()
print (name)
movie_containers = soup.find_all('div', class_ = 'lister-item mode-detail')
print(type(movie_containers))
print(len(movie_containers))

movie_genre = movie_containers[8].find('span', class_ = 'genre')
type(movie_genre)
len(movie_genre)
import pandas as pd
pages = [str(i) for i in range(1,6)]
from time import time 
from time import sleep
from random import randint
start_time = time()
requests = 0
for _ in range(5):
# A request would go here
    requests += 1
    sleep(randint(1,3))
    elapsed_time = time() - start_time
    print('Request: {}; Frequency: {} requests/s'.format(requests, requests/elapsed_time))
    from IPython.core.display import clear_output
    start_time = time()
    requests = 0
    for _ in range(5):
        requests  += 1
        sleep(randint(1,3))
        current_time = time()
        elapsed_time = current_time - start_time
        print('Request:{};Frequency:{} requests/s'.format(requests, requests/elapsed_time))
        clear_output(wait=True)
#Redelcaring the lists to store data in
names = []
Rating_value = []
timing = []
Type = []
from warnings import warn
#Preparing te mon =itoring of the loop
start_time = time()
requests = 0
#For every page in the interval 1-5
from requests import get
for page in pages:
    response = get('https://www.imdb.com/list/ls005750764/?st_dt=&mode=detail&page=' + page + '&sort=list_order,asc')
    sleep(randint(8,15))
    requests += 1
    elapsed_time = time() - start_time
    print('Request:{}; Frequency: {} requests/s'.format(requests, requests/elapsed_time))
    clear_output(wait = True)

        # Throw a warning for non-200 status codes
    if response.status_code != 200:
        warn('Request: {}; Status code: {}'.format(requests, response.status_code))

        # Break the loop if the number of requests is greater than expected
    if requests > 500:
            warn('Number of requests was greater than expected.')
            break

        # Parse the content of the request with BeautifulSoup
    soup = BeautifulSoup(response.text, 'lxml')

        # Select all the 100 movie containers from a single page
    movie_containers = soup.find_all('div', class_ = 'lister-item mode-detail')

        # For every movie of these 100
    for container in movie_containers:
        if container.find('span', class_= 'genre') is not None:
            name = container.h3.a.text
            names.append(name)
            print(names)
            len(names)
        #RATING VALUE
            imdb = container.strong
            Rating_value.append(imdb)
            print(Rating_value)
            len(Rating_value)
            #Timing
            Time= container.find('span', class_='runtime').text
            timing.append(Time)
            print(timing)
    #Type
            genre = container.find('span', class_ = 'genre').text
            Type.append(str(genre))
            print(Type)
    
movies = pd.DataFrame({'movie': names,
                        'Rating':Rating_value,
                        'Duration' : timing,
                        'Genre' : Type
                        })
print(movies.info())
movies.head(10)
                        
    