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
        # If the playlist owner id equals the current user's profile id.
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
        # If the playlist owner id does not equal the current user's profile id.
        else:
            pass

    # Create variable to store chosen playlist's ID.
    while True:
        # Create loop to print playlists for selection
        for playlist in range(len(playlists_list)):
            playlist_name = playlists_list[playlist]["playlist_name"]
            print(f"{playlist} - {playlist_name}")
        try:
            # Request user input to paste playlist ID to be sorted.
            # playlist_to_be_sorted must be treated as an integer because this iterates through a list of dictionaries.
            playlist_to_be_sorted = int(input('Please enter the number to the left of the playlist to be sorted: '))
            playlist_id = playlists_list[playlist_to_be_sorted]["playlist_id"]
            # Print playlist id to console.
            # print(playlist_id)
            # Return the value of playlist_id
            return playlist_id
        # Create error handling if an integer is not entered.
        except ValueError:
            print("Enter an integer.")
        # Create error handling if an integer is entered but it does not correspond to a playlist.
        except IndexError:
            print("Invalid playlist number entered.")

# Create __name__ == "__main__" idiom.
if __name__ == "__main__":
    print('This file cannot be executed as a script.\n\nExecute "spotify_playlist_mulit-level_sorting.py" to sort playlist.')