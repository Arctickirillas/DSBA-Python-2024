import csv
import argparse

songs = []
LAST_INDEX = 24

def read_data(path: str = 'data/Spotify_Youtube.csv'):
    with open(path, 'r') as file:
        header = file.readline().strip().split(',')
        songs = [element for element in csv.reader(file)]
    return songs, header


def get_shape(songs: []):
    return len(songs), len(songs[0])


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


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--file')
    args = parser.parse_args()

    songs, header = read_data(args.file)
    # print(songs)
    # print(header)
    print(get_min_max(songs, 9))
    print(get_shape(songs))
    print(get_average_likes(songs))