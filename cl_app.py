# class Song:
#     def __init__(self, id, artist, Url_spotify, Track, Album, Album_type, Uri, Danceability, Energy, Key, Loudness, Speechiness, Acousticness, Instrumentalness, Liveness, Valence, Tempo, Duration_ms, Url_youtube, Title, Channel, Views, Likes, Comments, Description, Licensed, official_video, Stream):
#         self.id = id
#         self.artist = artist
#         self.Url_spotify = Url_spotify
#         self.Track = Track
#         self.Album = Album
#         self.Album_type = Album_type
#         self.Uri = Uri
#         self.Danceability = Danceability
#         self.Energy = Energy
#         self.Key = Key
#         self.Loudness = Loudness
#         self.Speechiness = Speechiness
#         self.Acousticness = Acousticness
#         self.Instrumentalness = Instrumentalness
#         self.Liveness = Liveness
#         self.Valence = Valence
#         self.Tempo = Tempo
#         self.Duration_ms = Duration_ms
#         self.Url_youtube = Url_youtube
#         self.Title = Title
#         self.Channel = Channel
#         self.Views = Views
#         self.Likes = Likes
#         self.Comments = Comments
#         self.Description = Description
#         self.Licensed = Licensed
#         self.official_video = official_video
#         self.Stream = Stream
#         self.Danceability = Danceability
#         self.Energy = Energy
#         self.Key = Key
#         self.Loudness = Loudness
#         self.Speechiness = Speechiness
#         self.Acousticness = Acousticness
#         self.Instrumentalness = Instrumentalness
#         self.Liveness = Liveness
#         self.Valence = Valence
#         self.Tempo = Tempo
#         self.Duration_ms = Duration_ms
#         self.Url_youtube = Url_youtube
#         self.Title = Title
#         self.Channel = Channel
#         self.Views = Views
#         self.Likes = Likes
#         self.Comments = Comments
#         self.Description = Description
#         self.Licensed = Licensed
#         self.official_video = official_video
#         self.Stream = Stream
#

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


if __name__ == "__main__":
    songs, header = read_data()
    for song in songs:
        print(song)
    print(len(songs))