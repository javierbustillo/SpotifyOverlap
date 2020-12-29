from SpotifyAPI import SpotifyAPI
from itertools import chain, combinations

cmd = ''
uris = []
spotify_api = SpotifyAPI()

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s)+1))

while cmd != "end":
    cmd = input("Enter playlist uri or type end when done")
    if cmd != "end":
        cmd = cmd.split(":")
        uri = cmd[-1]
        uris.append(uri)

uri_powerset = powerset(uris)

for combination in uri_powerset:
    if len(combination) == 1:
        continue
    tracks = []
    for uri in combination:
        track_uris = []
        items = spotify_api.get_playlist_tracks(uri)
        for item in items:
            track_uris.append(item['track']["id"])
        tracks.append(track_uris)
    overlap = set(tracks[0]).intersection(*tracks[1:])

    names = []
    for uri in combination:
        names.append(spotify_api.get_playlist_title(uri))

    print(' - '.join(names))
    for uri in overlap:
        print(spotify_api.get_track(uri)["name"])
    print("\n\n")









