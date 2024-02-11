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

# Authorization Code Flow to obtain current user's profile.
get_current_users_profile = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotify_client_id,
                                               client_secret=spotify_client_secret,
                                               redirect_uri=spotify_redirect_uri,
                                               # Scopes required for obtaining current user's profile can be found here: https://developer.spotify.com/documentation/web-api/reference/get-current-users-profile
                                               scope="user-read-private user-read-email"))

# Create variable to store data from current_user method of spotipy
get_current_users_profile_data = get_current_users_profile.current_user()

# Print current's user profile in console.
# This is the original data returned by Spotify.
# print(json.dumps(get_current_users_profile.current_user(), indent=4, sort_keys=True))

# Create empty dictionary to store nested dictionaries.
users_dictionary = {}

# Create loop to iterate through playlists.
for user in range(len(get_current_users_profile_data)):
    # Create empty dictionary to store data about the user.
    # This dictionary will be the value of the key which is the user.
    users_data_dictionary = {}
    # Update users_data_dictionary with key:value pair.
    users_data_dictionary.update({"email":get_current_users_profile_data["email"]})
    # Update users_dictionary with key:value pair.
    users_data_dictionary.update({"country":get_current_users_profile_data["country"]})
    # Update users_data_dictionary with key:value pair.
    users_data_dictionary.update({"id":get_current_users_profile_data["id"]})
    # Update users_data_dictionary with key:value pair.
    users_data_dictionary.update({"product":get_current_users_profile_data["product"]})
    # Update users_data_dictionary with key:value pair.
    users_data_dictionary.update({"followers":get_current_users_profile_data["followers"]["total"]})
    # Update playlists_dictionary with key:value pair.
    # The key is the name of the playlist and the value is playlists_data_dictionary
    users_dictionary.update({get_current_users_profile_data["display_name"]:users_data_dictionary})

# Print current users's playlists in console
print(json.dumps(users_dictionary, indent=4, sort_keys=False))