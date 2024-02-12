# Spotify Playlist Multi-Level Sorting
Spotify playlist multi-level sorting.

## About This Repository
This is my repository for my project of creating a way to perform multi-level sorting on Spotify playlists with Python via the Spotify web API.

### Execution
THIS IS NOT READY FOR PRODUCTION!

The spotify credentials are stored in a file that is not configured to be uploaded to GitHub as it contains my Client ID and Client Secret.

If you wish to use this, upon cloning this repository you will need to create a file called `spotify_developer_application.py` that contains four variables:
* `spotify_client_id`
* `spotify_client_secret`
* `spotify_redirect_uri`
* `spotify_playlist_id`

The values for `spotify_client_id`, `spotify_client_secret`, and `spotify_redirect_uri` can be gathered from the Spotify developer dashboard after you create an application.

To create an application follow the steps outlined under "Create an app" [here](https://developer.spotify.com/documentation/web-api/tutorials/getting-started#create-an-app).

The value for `spotify_playlist_id` can be gathered from running the `get_current_users_playlists.py` module and copying and pasting the desired playlist id to be sorted.