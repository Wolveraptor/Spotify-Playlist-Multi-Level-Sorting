<!-- omit from toc -->
# Spotify Playlist Multi-Level Sorting
* Spotify Playlist Multi-Level Sorting.

<!-- omit from toc -->
## Spotify Playlist Multi-Level Sorting | About This Repository
* This is my repository for my project of creating a way to perform multi-level sorting on Spotify playlists with Python via the Spotify web API and [spotipy](https://github.com/spotipy-dev/spotipy) library.

<!-- omit from toc -->
### Spotify Playlist Multi-Level Sorting | Table of Contents
* [Spotify Playlist Multi-Level Sorting | Additional Information](#spotify-playlist-multi-level-sorting--additional-information)
* [Spotify Playlist Multi-Level Sorting | Execution](#spotify-playlist-multi-level-sorting--execution)
* [Spotify Playlist Multi-Level Sorting | Notes](#spotify-playlist-multi-level-sorting--notes)

#### Spotify Playlist Multi-Level Sorting | Additional Information
* This cannot sort playlists that contain local files.
* This will sort a Spotify playlist in the following multi-level order:
    * artist
    * release_date
    * album
    * disc_number
    * track_number

#### Spotify Playlist Multi-Level Sorting | Execution
* Prior to running this on your playlist, make a copy of it and test this on the copy.
* This has been tested on the following playlist: [Spotify Playlist Multi-Level Sorting](https://open.spotify.com/playlist/47l4vufg3gAoVbOpSedwO5?si=852f7ce6eaa849c8)
1. Create a Spotify application in the Spotify Developer Dashboard.
    * Steps for creating an application can be found [here](https://developer.spotify.com/documentation/web-api/tutorials/getting-started#create-an-app).
    * Use `http://localhost:3000/` for the Redirect URI.
2. Clone the repository with `git clone https://gitlab.cybersanctuary.xyz/wolveraptor/spotify-playlist-multi-level-sorting.git`
3. Navigate to the cloned repository via CLI.
    * For Windows use `PowerShell` or `Command Prompt`.
    * For Linux and MacOS use `Terminal`.
4. Create a virtual environment.
    * For Windows `Command Prompt` use `python.exe -m venv spmls`.
    * For Windows `PowerShell` use `python.exe -m venv spmls`.
    * For Linux and MacOS use `python3 -m venv spmls`.
        * On Debian/Ubuntu systems, you may need to install the `python3-venv` package.
            * Example: `sudo apt install python3-venv`
5. Activate the virtual environment.
    * For Windows `Command Prompt` use `spmls\Scripts\activate.bat`.
    * For Windows `PowerShell` use `.\spmls\Scripts\Activate.ps1`.
    * For Linux and MacOS use `source spmls/bin/activate`.
6. Install required dependencies.
    * For Windows `Command Prompt` use `python.exe -m pip install -r requirements.txt`.
    * For Windows `PowerShell` use `python.exe -m pip install -r .\requirements.txt`.
    * For Linux and MacOS use `python3 -m pip install -r requirements.txt`.
7. Execute `spotify_playlist_multi-level_sorting.py` and supply the `Client ID` from the Spotify Developer Dashboard and the `Client Secret` from the Spotify Developer Dashboard.
    * Client ID:
    * ![alttext](/Images/spotify_developer_dashboard_client_id.png)
    * Client Secret:
    * ![alttext](/Images/spotify_developer_dashboard_client_secret.png)
    * For Windows `Command Prompt` use `python.exe spotify_playlist_multi-level_sorting.py 0123456789 9876543210`.
    * For Windows `PowerShell` use `python.exe .\spotify_playlist_multi-level_sorting.py 0123456789 9876543210`.
    * For Linux and MacOS use `python3 spotify_playlist_multi-level_sorting.py 0123456789 9876543210`.
8. Follow the on-screen prompts.
9. Deactivate the virtual environment.
    * For Windows `Command Prompt` use `spmls\Scripts\deactivate.bat`.
    * For Windows `PowerShell` use `deactivate`.
    * For Linux and MacOS use `deactivate`.

#### Spotify Playlist Multi-Level Sorting | Notes
* To view example usage and the optional argument execute:
    * Windows: `py spotify_playlist_multi-level_sorting.py -h` or `py spotify_playlist_multi-level_sorting.py --help`
    * MacOS and Ubuntu: `python3 spotify_playlist_multi-level_sorting.py -h` or `python3 spotify_playlist_multi-level_sorting.py --help`
* `0123456789` and `9876543210` are examples of `Client ID` and `Client Secret` respectively. Do not use these values as they will not work. You must enter the `Client ID` and `Client Secret` as they appear in the Spotify Developer Dashboard.
* If the optional argument -ruri or --redirect_uri is supplied, the `Redirect URI` from the Spotify Developer Dashboard must be entered as well. This optional argument only needs to be supplied if a `Redirect URI` other than `http://localhost:3000` was configured in the Spotify Developer Dashboard.