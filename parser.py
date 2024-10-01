import requests
from bs4 import BeautifulSoup as bs


def parse_genre_by_artist(artist: str):
    URL = "https://www.last.fm/music/{}"

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


artist = input()
print(parse_genre_by_artist(artist))
