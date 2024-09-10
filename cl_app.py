songs = []
LAST_INDEX = 24

def read_data(path: str = 'data/Spotify_Youtube.csv'):
    songs = []

    with open(path, 'r') as file:
        header = file.readline().strip().split(',')
        for line in file:
            line = line.strip().split(',')
            if len(line) > LAST_INDEX and line[0].isdigit():
                songs.append(line)
    return songs, header


def get_shape(songs: []):
    return len(songs), len(songs[0])


def get_max(songs, column):
    m = 0
    if songs[0][column].isdigit():
        for i in range(len(songs)):
            if float(songs[i][column]) > m:
                m = float(songs[i][column])
        return m
    return -1


if __name__ == "__main__":
    songs, header = read_data()
    print("Max:", get_max(songs, 0))
    print(get_shape(songs))