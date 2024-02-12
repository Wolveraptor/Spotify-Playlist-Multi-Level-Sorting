# Import required modules.
# json module is used for printing returned data.
import json
# spotipy is used for authenticating with the Spotify web API.
import spotipy
from spotipy.oauth2 import SpotifyOAuth
# spotify_developer_application is used for passing the spotify_client_id, spotify_client_secret, and spotify_redirect_uri variables.
from spotify_developer_application import (spotify_client_id,
                                           spotify_client_secret,
                                           spotify_redirect_uri)

# Authorization Code Flow to obtain current user's playlists.
get_current_users_playlists = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotify_client_id,
                                                                        client_secret=spotify_client_secret,
                                                                        redirect_uri=spotify_redirect_uri,
                                                                        # Scopes required for obtaining current user's playlists can be found here: https://developer.spotify.com/documentation/web-api/reference/get-a-list-of-current-users-playlists
                                                                        scope="playlist-read-private"))

# Create variable to store data from current_user_playlist method of spotipy
get_current_users_playlists_data = get_current_users_playlists.current_user_playlists()

# Print current user's playlists in console.
# This is the original data returned by Spotify.
# print(json.dumps(get_current_users_playlists.current_user_playlists(), indent=4, sort_keys=True))

# Create empty list to store dictionaries.
playlists_list = []

# Create loop to iterate through playlists.
for playlists in range(len(get_current_users_playlists_data["items"])):
    # Create empty dictionary to store data about each playlist.
    # This dictionary will be the value of the key which is the playlist.
    playlists_data_dictionary = {}
    # Update playlists_data_dictionary with key:value pair.
    playlists_data_dictionary.update({"name":get_current_users_playlists_data["items"][playlists]["name"]})
    # Update playlists_data_dictionary with key:value pair.
    playlists_data_dictionary.update({"owner":get_current_users_playlists_data["items"][playlists]["owner"]["display_name"]})
    # Update playlists_data_dictionary with key:value pair.
    playlists_data_dictionary.update({"id":get_current_users_playlists_data["items"][playlists]["id"]})
    # Update playlists_data_dictionary with key:value pair.
    playlists_data_dictionary.update({"tracks":get_current_users_playlists_data["items"][playlists]["tracks"]["total"]})
    # Update playlists_dictionary with key:value pair.
    # The key is the name of the playlist and the value is playlists_data_dictionary
    playlists_list.append(playlists_data_dictionary)

# Print current users's playlists in console
print(json.dumps(playlists_list, indent=4, sort_keys=False))