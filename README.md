# Spotify Playlist Multi-Level Sorting
Spotify playlist multi-level sorting.

## About This Repository
This is my repository for my project of creating a way to perform multi-level sorting on Spotify playlists with Python via the Spotify web API and [spotipy](https://github.com/spotipy-dev/spotipy) library.

### Additional Information
This cannot sort playlists that contain local files.

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
4. Execute `spotify_playlist_multi-level_sorting.py` and supply the `Client ID` from the Spotify Developer Dashboard and the `Client Secret` from the Spotify Developer Dashboard.
    * Client ID:
    * ![alttext](/Images/spotify_developer_dashboard_client_id.png)
    * Client Secret:
    * ![alttext](/Images/spotify_developer_dashboard_client_secret.png)
    * `python3 spotify_playlist_multi-level_sorting.py 0123456789 9876543210`
        * To view example usage and the optional argument execute: `python3 spotify_playlist_multi-level_sorting.py -h` or `python3 spotify_playlist_multi-level_sorting.py --help`
5. Follow the on-screen prompts.