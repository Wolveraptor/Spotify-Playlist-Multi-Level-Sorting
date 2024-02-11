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
                                               # Scopes required for obtaining current user's profile can be found here: https://developer.spotify.com/documentation/web-api/reference/get-a-list-of-current-users-playlists
                                               scope="playlist-read-private"))

# Print current user's playlists in console.
print(json.dumps(get_current_users_playlists.current_user_playlists(), indent=4, sort_keys=True))
print(f"Playlist Name: {get_current_users_playlists.current_user_playlists()["items"][0]["name"]}")
print(f"Playlist Owner: {get_current_users_playlists.current_user_playlists()["items"][0]["owner"]["display_name"]}")
print(f"Playlist ID: {get_current_users_playlists.current_user_playlists()["items"][0]["owner"]["id"]}")
print(f"Playlist Tracks: {get_current_users_playlists.current_user_playlists()["items"][0]["tracks"]["total"]}")