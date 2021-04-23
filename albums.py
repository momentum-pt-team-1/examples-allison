albums = {
    'Queen'[('A Night at the Opera', 1969), ('Queen', 1973), ('Sheer Heart Attack', 1974)],: 
    'Beatles': [('Abbey Road', 1969), ("Help", 1975), ("A Hard Day's Night", 1964)]
}

def list_albums(album_dict):
    for artist, albums in album_dict.items():
        for album in albums:
            print(f"{artist}'s albums include {album[0]}")

list_albums(albums)

def add_albums(album_dict):
    artist = input("Name your artist: ")
    album_list = input("List the albums: ")
    if artist in album_dict.keys():
        album_dict[artist].append(album_list)
    else:
        album_dict[artist] = album_list
    # list_albums(album_dict)
    # return album_dict

add_albums(albums)
list_albums(albums)
