# Import required modules.
# json module is used for printing returned data.
import json
# spotipy is used for authenticating with the Spotify web API.
import spotipy
from spotipy.oauth2 import SpotifyOAuth
# spotify_developer_application is used for passing the spotify_client_id, spotify_client_secret, spotify_redirect_uri, spotify_playlist_id variables.
from spotify_developer_application import (spotify_client_id,
                                           spotify_client_secret,
                                           spotify_redirect_uri,
                                           spotify_playlist_id)

# Authorization Code Flow to obtain current user's playlists.
get_playlist_items = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotify_client_id,
                                                               client_secret=spotify_client_secret,
                                                               redirect_uri=spotify_redirect_uri,
                                                               # Scopes required for reordering current user's playlist can be found here: https://developer.spotify.com/documentation/web-api/reference/get-a-list-of-current-users-playlists
                                                               scope='playlist-modify-public'))

# Create variable to store data from playlist_items method of spotipy
get_playlist_items_data = get_playlist_items.playlist_items(spotify_playlist_id,
                                                            offset=0,
                                                            additional_types=['track'])
            
# Create empty list to store dictionaries.
tracks_list = []

# Create loop to iterate through playlist tracks.
for tracks in range(len(get_playlist_items_data["items"])):
    # Create empty dictionary to store data about each track.
    tracks_data_dictionary = {}
    # Update tracks_data_dictionary with key:value pair.
    tracks_data_dictionary.update({"artist":get_playlist_items_data["items"][tracks]["track"]["artists"][0]["name"]})
    # Update tracks_data_dictionary with key:value pair.
    tracks_data_dictionary.update({"album":get_playlist_items_data["items"][tracks]["track"]["album"]["name"]})
    # Update tracks_data_dictionary with key:value pair.
    tracks_data_dictionary.update({"release_date":get_playlist_items_data["items"][tracks]["track"]["album"]["release_date"]})
    # Update tracks_data_dictionary with key:value pair.
    tracks_data_dictionary.update({"track":get_playlist_items_data["items"][tracks]["track"]["name"]})
    # Update tracks_data_dictionary with key:value pair.
    tracks_data_dictionary.update({"track_number":get_playlist_items_data["items"][tracks]["track"]["track_number"]})
    # Update tracks_data_dictionary with key:value pair.
    tracks_data_dictionary.update({"disc_number":get_playlist_items_data["items"][tracks]["track"]["disc_number"]})
    # Update tracks_data__dictionary with key:value pair.
    tracks_data_dictionary.update({"id":get_playlist_items_data["items"][tracks]["track"]["id"]})
    tracks_list.append(tracks_data_dictionary)

# Create while loop to look for next set of paginated results.
while get_playlist_items_data["next"]:
    # Set variable get_playlist_items_data value to the next set of paginated results.
    get_playlist_items_data = get_playlist_items.next(get_playlist_items_data)
    # Create loop to iterate through playlist tracks.
    for tracks in range(len(get_playlist_items_data["items"])):
        # Create empty dictionary to store data about each track.
        tracks_data_dictionary = {}
        # Update tracks_data_dictionary with key:value pair.
        tracks_data_dictionary.update({"artist":get_playlist_items_data["items"][tracks]["track"]["artists"][0]["name"]})
        # Update tracks_data_dictionary with key:value pair.
        tracks_data_dictionary.update({"album":get_playlist_items_data["items"][tracks]["track"]["album"]["name"]})
        # Update tracks_data_dictionary with key:value pair.
        tracks_data_dictionary.update({"release_date":get_playlist_items_data["items"][tracks]["track"]["album"]["release_date"]})
        # Update tracks_data_dictionary with key:value pair.
        tracks_data_dictionary.update({"track":get_playlist_items_data["items"][tracks]["track"]["name"]})
        # Update tracks_data_dictionary with key:value pair.
        tracks_data_dictionary.update({"track_number":get_playlist_items_data["items"][tracks]["track"]["track_number"]})
        # Update tracks_data_dictionary with key:value pair.
        tracks_data_dictionary.update({"disc_number":get_playlist_items_data["items"][tracks]["track"]["disc_number"]})
        # Update tracks_data__dictionary with key:value pair.
        tracks_data_dictionary.update({"id":get_playlist_items_data["items"][tracks]["track"]["id"]})
        tracks_list.append(tracks_data_dictionary)

# Sort list of dictionaries by multiple keys.
# Sorting is performed by artist, release_date, album, disc_number, and then track_number
# The casefold() method returns all characters as lowercase.
# If this is not performed, uppercase and lowercase characters will be sorted separately even if they are the same character.
# By default, sorting is performed in ASCIIbetical order which puts uppercase letters before lowercase letters.
tracks_list = sorted(tracks_list,
                           key=lambda track:
                           (track["artist"].casefold(),
                            track["release_date"].casefold(),
                            track["album"].casefold(),
                            track["disc_number"],
                            track["track_number"]))

# Print current users's playlist tracks in console
print(json.dumps(tracks_list, indent=4, sort_keys=False))

# Create empty list to store track ids.
ids_list = []

# Create loop to iterate through tracks.
for ids in range(len(tracks_list)):
    # Append track id to ids_list
    ids_list.append(tracks_list[ids]["id"])

# Print track ids in console.
print(ids_list)

# Create empty list to store ids in nested lists.
# This is required as there is a maximum of 100 items in one request.
ids_list_of_lists = []

# Slice the ids_list into smaller 100 item lists and add them to ids_list_of_lists
# Need to add additional comments for clarity for list slicing.
# Additional information can be found here: https://www.geeksforgeeks.org/break-list-chunks-size-n-python/
# Additional information can be found here: https://stackoverflow.com/questions/33491703/meaning-of-x-x-1-in-python
start = 0
end = len(ids_list) 
step = 100
for i in range(start, end, step): 
    x = i 
    ids_list_of_lists.append((ids_list[x:x+step]))

# Print nested list of track ids in console.
print(ids_list_of_lists)

# Create loop to iterate through ids lists to delete all tracks in the playlist.
for ids_list in range(len(ids_list_of_lists)):
    get_playlist_items.playlist_remove_all_occurrences_of_items(spotify_playlist_id,
                                                                items=ids_list_of_lists[ids_list])

# Create loop to iterate through ids lists to add tracks to the playlist.
for ids_list in range(len(ids_list_of_lists)):
        get_playlist_items.playlist_add_items(spotify_playlist_id,
                                              ids_list_of_lists[ids_list])