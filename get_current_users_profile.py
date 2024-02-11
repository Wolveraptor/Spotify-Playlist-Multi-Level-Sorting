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

# Print current's user profile in console.
print(json.dumps(get_current_users_profile.me(), indent=4, sort_keys=True))