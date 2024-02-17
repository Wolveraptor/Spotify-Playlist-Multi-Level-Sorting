# Create __name__ == "__main__" idiom.
if __name__ == "__main__":
    print('This file cannot be executed as a script.\n\nExecute "spotify_playlist_mulit-level_sorting.py" to sort playlist.')
else:
    # The values for the variables "spotify_client_id" and "spotify_client_secret" are gathered from the Spotify Developer Dashboard.
    spotify_application_client_id = "Client ID from Spotify Developer Dashboard"
    spotify_application_client_secret = "Client Secret from Spotify Developer Dashboard"
    spotify_application_redirect_uri = "http://localhost:3000/"