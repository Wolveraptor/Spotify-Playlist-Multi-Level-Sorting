# Import required modules.
# json module is used for printing returned data.
import json
# spotipy is used for interacting with the Spotify API.
import spotipy

# Create function to get current user's playlists information.
def get_current_users_playlists(spotify_authorization, current_users_profile_id):
    # Create variable to store data from current_user_playlist method of spotipy
    get_current_users_playlists_data = spotify_authorization.current_user_playlists(limit=50)

    # Create empty list to store dictionaries.
    playlists_list = []

    # Create loop to iterate through playlists.
    for playlists in range(len(get_current_users_playlists_data["items"])):
        if get_current_users_playlists_data["items"][playlists]["owner"]["id"] == current_users_profile_id:
            # Create empty dictionary to store data about each playlist.
            # This dictionary will be the value of the key which is the playlist.
            playlists_data_dictionary = {}
            # Update playlists_data_dictionary with key:value pair.
            playlists_data_dictionary.update({"playlist_name":get_current_users_playlists_data["items"][playlists]["name"]})
            # Update playlists_data_dictionary with key:value pair.
            playlists_data_dictionary.update({"playlist_id":get_current_users_playlists_data["items"][playlists]["id"]})
            # Update playlists_data_dictionary with key:value pair.
            playlists_data_dictionary.update({"playlist_tracks_total":get_current_users_playlists_data["items"][playlists]["tracks"]["total"]})
            # Update playlists_data_dictionary with key:value pair.
            playlists_data_dictionary.update({"playlist_owner":get_current_users_playlists_data["items"][playlists]["owner"]["display_name"]})
            # Update playlists_data_dictionary with key:value pair.
            playlists_data_dictionary.update({"playlist_owner_id":get_current_users_playlists_data["items"][playlists]["owner"]["id"]})
            # Append playlists_data_dictionary to playlists_list
            playlists_list.append(playlists_data_dictionary)
        else:
            pass

    # Print current users's playlists in console
    print(json.dumps(playlists_list, indent=4, sort_keys=False))

    # Request user input to paste playlist ID to be sorted.
    playlist_id = input('Please copy and paste the "playlist_id" to be sorted: ')

    # Return the value of playlist_id
    return playlist_id