# Spotify Playlist Multi-Level Sorting
Spotify playlist multi-level sorting.

## About This Repository
This is my repository for my project of creating a way to perform multi-level sorting on Spotify playlists with Python via the Spotify web API and [spotipy](https://github.com/spotipy-dev/spotipy) library.

Requirements were gathered via: `python3 -m pip freeze > requirements.txt`

### Additional Information
This cannot sort playlists that contain local files.

The python package `spotipy` is required for execution.

This will sort a Spotify playlist in the following multi-level order:
* album_artist
* release_date
* album
* disc_number
* track_number

The spotify credentials are stored in a file that is not configured to be uploaded to GitHub as it contains my Client ID and Client Secret.

### Execution
Prior to running this on your playlist, make a copy of it and test this on the copy.

This has been tested on the following playlist: [Spotify Playlist Multi-Level Sorting](https://open.spotify.com/playlist/47l4vufg3gAoVbOpSedwO5?si=852f7ce6eaa849c8)

1. Create a Spotify application in the Spotify Developer Dashboard.
    * Steps for creating an application can be found [here](https://developer.spotify.com/documentation/web-api/tutorials/getting-started#create-an-app).
    * Use `http://localhost:3000/` for the Redirect URI.
2. Clone the repository with `git clone https://github.com/Wolveraptor/Spotify-Playlist-Multi-Level-Sorting.git`
3. Navigate to the cloned repository via CLI and run `python3 -m pip install -r requirements.txt`
4. Rename the file `spotify_developer_application_template.py` to `spotify_developer_application.py` in the cloned repository.
5. Edit the following lines in `spotify_developer_application_template.py`:
    * `spotify_application_client_id = "Client ID from Spotify Developer Dashboard"`
        * Replace `Client ID from Spotify Developer Dashboard` with the client ID from the Spotify developer dashboard.
        * ![alttext](/Images/spotify_developer_dashboard_client_id.png)
    * `spotify_application_client_secret = "Client Secret from Spotify Developer Dashboard"`
        * Replace `Client Secret from Spotify Developer Dashboard"` with the client secret from the Spotify developer dashboard.
        * ![alttext](/Images/spotify_developer_dashboard_client_secret.png)
6. Execute the `spotify_playlist_multi-level_sorting.py` file and follow the on-screen prompts.