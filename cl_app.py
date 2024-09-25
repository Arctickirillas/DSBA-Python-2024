from colorsys import yiq_to_rgb
from xxsubtype import bench

import pandas as pd


class Song:
    def __init__(self, row: pd.Series):
        self.title = row.Title
        self.artist = row.Artist
        self.likes = row.Likes

        self.musicality = row[['Danceability', 'Energy', 'Key', 'Loudness', 'Speechiness',
        'Acousticness', 'Instrumentalness', 'Liveness', 'Valence', 'Tempo']]

    def __repr__(self):
        return f"|{self.title} by {self.artist} with {self.likes} likes|"


class Database:
    def __init__(self, path: str = 'data/Spotify_Youtube.csv'):
        df = pd.read_csv(path, index_col=0)
        df.dropna(subset=['Danceability', 'Energy', 'Key', 'Loudness', 'Speechiness', 'Acousticness',
                          'Instrumentalness', 'Liveness', 'Valence', 'Tempo'], inplace=True)
        self.db = {}
        self.shape = df.shape
        for index, row in df.iterrows():
            self.add_song(row)

    def add_song(self, row: pd.Series):
        self.db[row.Artist] = self.db.get(row.Artist, []) + [Song(row)]

    def display(self):
        print(self.db)

    def search(self, artist, n: int = 3):
        songs = self.db.get(artist)
        if songs is None:
            return []
        return sorted(songs, key=lambda song: song.likes, reverse=True)[:n]

    def get_shape(self):
        return self.shape

    def find_similar_songs(self, song: str):
        result = []
        for element in sum(self.db.values(), []):
            if not isinstance(element.title, float) and song.lower() in element.title.lower():
                result.append(element)
        for i, element in (enumerate(result)):
            print(f"({i})", element)
        index = int(input("Choose a song you prefer\n"))
        return result[index]



    # TODO: return the closest song by search and then find similar by musicality
songs = []
LAST_INDEX = 24

def get_min_max(songs: [], column: int):
    if column < 0 or column > len(songs[0]):
        raise IndexError('out of range')
    if songs[0][column].replace('.','', 1).isnumeric():
        return (min([float(songs[i][column]) for i in range(len(songs)) if songs[i][column] != '']),
                max([float(songs[i][column]) for i in range(len(songs)) if songs[i][column] != '']))
    else:
        raise TypeError('column must be a number')


def get_average_likes(songs: []):
    song_map = dict()
    likes_map = dict()
    for element in songs:
        song_map[element[1]] = song_map.get(element[1], 0) + 1
        likes_map[element[1]] = likes_map.get(element[1], 0) + float(element[23]) if element[23] else 0
    for i in song_map:
        song_map[i] =  likes_map[i] / song_map[i]
    return sorted(song_map.items(), key=lambda x: x[1], reverse=True)

DB = Database()
# DB.display()display
# print(DB.search("SICK LEGEND"))
# print(DB.get_shape())
# DB.display()
print(DB.find_similar_songs("feel good"))

# if __name__ == "__main__":
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--file')
    # args = parser.parse_args()
    #
    # songs, header = read_data(args.file)
    # print(get_min_max(songs, 9))
    # print(get_shape(songs))
    # print(get_average_likes(songs))