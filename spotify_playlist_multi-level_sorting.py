# Import required modules.
# argparse is used for taking command-line options, arguments, and sub-commands.
import argparse
# Import connect_to_spotify_api function.
from Modules.function_connect_to_spotify_api import connect_to_spotify_api
# Import get_current_users_profile function.
from Modules.function_get_current_users_profile import get_current_users_profile
# Import get_current_users_playlists function.
from Modules.function_get_current_users_playlists import get_current_users_playlists
# Import sort_current_users_playlist function.
from Modules.function_sort_current_users_playlist import sort_current_users_playlist

# Additional information can be found here: https://machinelearningmastery.com/command-line-arguments-for-your-python-script/
argument_parser = argparse.ArgumentParser(description="Spotify Playlist Multi-Level Sorting positional and optional arguments:",
                                 usage="With default Redirect URI: python3 spotify_playlist_multi-level_sorting.py 0123456789 9876543210\n\n\
       With custom Redirect URI: python3 spotify_playlist_multi-level_sorting.py 0123456789 9876543210 http://localhost:9000/",
                                 # formatter_class=argparse.ArgumentDefaultsHelpFormatter)
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
# Create required positional argument client_id
argument_parser.add_argument("client_id", help="Client ID from Spotify Developer Dashboard.")
# Create required positional argument client_secret
argument_parser.add_argument("client_secret", help="Client Secret from Spotify Developer Dashboard.")
# Create optional argument -ruri/--redirect_uri
argument_parser.add_argument("-ruri", "--redirect_uri", default="http://localhost:3000/", help="Redirect URI from Spotify Developer Dashboard. (Default = http://localhost:3000/)")
# Assign arguments as namespace object to variable arguments_namespace_object
arguments_namespace_object = argument_parser.parse_args()
# Assign arguments as a dictionary to variable arguments_dictionary
arguments_dictionary = vars(arguments_namespace_object)
# Assign value of client_id key value to variable spotify_application_client_id
spotify_application_client_id = arguments_dictionary["client_id"]
# Assign value of client_secret key value to variable spotify_application_client_secret
spotify_application_client_secret= arguments_dictionary["client_secret"]
# Assign value of redirect_uri key value to variable spotify_application_redirect_uri
spotify_application_redirect_uri= arguments_dictionary["redirect_uri"]
# Print arguments_dictionary to console.
# print(arguments_dictionary)

# Create __name__ == "__main__" idiom.
if __name__ == "__main__":
    # Assign connect_to_spotify function with arguments to variable function_connect_to_spotify_api
    function_connect_to_spotify_api = connect_to_spotify_api(spotify_application_client_id, spotify_application_client_secret, spotify_application_redirect_uri)
    # Assign get_current_users-profile function with argument to variable function_get_current_users_profile
    function_get_current_users_profile = get_current_users_profile(function_connect_to_spotify_api)
    # Assign get_current_users_playlists function with arguments to variable function_get_current_users_playlists
    function_get_current_users_playlists = get_current_users_playlists(function_connect_to_spotify_api, function_get_current_users_profile)

    # Execute sort_current_users_playlist
    sort_current_users_playlist(function_connect_to_spotify_api, function_get_current_users_playlists)