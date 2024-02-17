# Import required modules.
# spotify_developer_application is used for passing the spotify_client_id, spotify_client_secret, and spotify_redirect_uri variables.
from spotify_developer_application import (spotify_application_client_id,
                                           spotify_application_client_secret,
                                           spotify_application_redirect_uri)

# Import connect_to_spotify_api function.
from Modules.function_connect_to_spotify_api import connect_to_spotify_api
# Import get_current_users_profile function.
from Modules.function_get_current_users_profile import get_current_users_profile
# Import get_current_users_playlists function.
from Modules.function_get_current_users_playlists import get_current_users_playlists
# Import sort_current_users_playlist function.
from Modules.function_sort_current_users_playlist import sort_current_users_playlist

# Assign connect_to_spotify function with arguments to variable function_connect_to_spotify_api
function_connect_to_spotify_api = connect_to_spotify_api(spotify_application_client_id, spotify_application_client_secret, spotify_application_redirect_uri)
# Assign get_current_users-profile function with argument to variable function_get_current_users_profile
function_get_current_users_profile = get_current_users_profile(function_connect_to_spotify_api)
# Assign get_current_users_playlists function with arguments to variable function_get_current_users_playlists
function_get_current_users_playlists = get_current_users_playlists(function_connect_to_spotify_api, function_get_current_users_profile)

# Execute sort_current_users_playlist
sort_current_users_playlist(function_connect_to_spotify_api, function_get_current_users_playlists)