# Import required modules.
# spotipy is used for interacting with the Spotify API.
import spotipy
# Import SpotifyOAuth for Client Authorization Code Flow.
from spotipy.oauth2 import SpotifyOAuth

# Create function to connect to the Spotify API.
def connect_to_spotify_api(application_client_id, application_client_secret, application_redirect_uri):
    # Authorization Code Flow to obtain current user's profile.
    spotify_authorization = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=application_client_id,
                                                                      client_secret=application_client_secret,
                                                                      redirect_uri=application_redirect_uri,
                                                                      # Scopes required for getting current user's profile can be found here: https://developer.spotify.com/documentation/web-api/reference/get-current-users-profile
                                                                      # Scopes required for obtaining current user's playlists can be found here: https://developer.spotify.com/documentation/web-api/reference/get-a-list-of-current-users-playlists
                                                                      # Scopes required for modifying current user's playlists can be found here: https://developer.spotify.com/documentation/web-api/reference/reorder-or-replace-playlists-tracks
                                                                      scope="user-read-private user-read-email playlist-read-private playlist-modify-public playlist-modify-private"))

    # Return the value of spotify_authorization
    return spotify_authorization

# Create __name__ == "__main__" idiom.
if __name__ == "__main__":
    print('This file cannot be executed as a script.\n\nExecute "spotify_playlist_mulit-level_sorting.py" to sort playlist.')