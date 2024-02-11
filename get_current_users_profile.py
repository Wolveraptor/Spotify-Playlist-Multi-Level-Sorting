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

# Authorization Code Flow to obtain user details.
user_details = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotify_client_id,
                                               client_secret=spotify_client_secret,
                                               redirect_uri=spotify_redirect_uri,
                                               scope="user-read-private user-read-email"))

# Print user details in console.
print(json.dumps(user_details.me(), indent=4, sort_keys=True))