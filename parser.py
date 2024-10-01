import requests
from bs4 import BeautifulSoup as bs


URL = "https://www.last.fm/music/{}"


def parse_genre_by_artist(artist: str):
    response = requests.get(URL.format(artist)) 

    if response.status_code != 200:
        return []

    soup = bs(response.text, 'html.parser')

    catalogue = soup.find('section', {'class': 'catalogue-tags'})
    # print(soup.find_all(class_='tag'))

    try:
        tags = [el.text.strip() for el in catalogue.find_all(class_='tag')]
    except:
        return []

    return tags


def parse_similar_artists(artist: str):
    response = requests.get(URL.format(artist) + '/+similar') 

    if response.status_code != 200:
        return []

    soup = bs(response.text, 'html.parser')

    catologue = soup.find('ol', class_='similar-artists')

    try:
        similar_artists = [el.text.strip() for el in catologue.find_all('h3')]
    except:
        return []

    return similar_artists


def parse_artist_bio(artist: str):
    response = requests.get(URL.format(artist) + '/+wiki') 

    if response.status_code != 200:
        return []

    soup = bs(response.text, 'html.parser')

    wiki = soup.find('div', class_='wiki-content')
    bio = [el.text.strip() for el in wiki.find_all('p')]
    
    return bio


artist = input()
print(parse_artist_bio(artist)[0])
