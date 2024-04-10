artist_names = ["The Lumineers", "Tame Impala", "Billie Eilish", "The Lumineers", "Arctic Monkeys", "Tame Impala"]
unique_artists = set()

for artist in artist_names:
    unique_artists.add(artist)
    
print("Unique lineup of artists",unique_artists)






artists_genres = {
    "The Lumineers": "Folk",
    "Tame Impala": "Psychedelic Rock",
    "Billie Eilish": "Pop",
    "Arctic Monkeys": "Indie Rock"
}

genres_artists = {}

for artist, genre in artists_genres.items():
    if genre in genres_artists:
        genres_artists[genre].add(artist)
    else:
        genres_artists[genre] = {artist}
        



for genre, artists in genres_artists.items():
    print(f"{genre}: {artists}")
    
    
    




playlist1 = {"Song A", "Song B", "Song C"}
playlist2 = {"Song D", "Song E", "Song F"}
playlist3 = {"Song A", "Song B", "Song C"}

playlists = [playlist1, playlist2, playlist3]


playlist_tuples = [tuple(playlist) for playlist in playlists]


duplicate_found = len(set(playlist_tuples)) != len(playlist_tuples)

print("Duplicate playlists found:", duplicate_found)

