# Import required modules.
# json module is used for printing returned data.
import json
# spotipy is used for interacting with the Spotify API.
import spotipy

# Create function to get current user's profile information.
def get_current_users_profile(spotify_authorization):
    # Create variable to store data from current_user() method of spotipy
    get_current_users_profile_data = spotify_authorization.current_user()

    # Create empty dictionary to store current user's profile information.
    current_users_profile_information_dictionary = {}

    # Update current_users_profile_information with key:value pair.
    current_users_profile_information_dictionary.update({"display_name":get_current_users_profile_data["display_name"]})
    # Update current_users_profile_information with key:value pair.
    current_users_profile_information_dictionary.update({"email":get_current_users_profile_data["email"]})
    # Update current_users_profile_information with key:value pair.
    current_users_profile_information_dictionary.update({"id":get_current_users_profile_data["id"]})
    # Update current_users_profile_information with key:value pair.
    current_users_profile_information_dictionary.update({"country":get_current_users_profile_data["country"]})
    # Update current_users_profile_information with key:value pair.
    current_users_profile_information_dictionary.update({"type":get_current_users_profile_data["type"]})
    # Update current_users_profile_information with key:value pair.
    current_users_profile_information_dictionary.update({"product":get_current_users_profile_data["product"]})

    # Print current user's profile information in console.
    # print(json.dumps(current_users_profile_information_dictionary, indent=4, sort_keys=False))

    # Return the value of id
    return current_users_profile_information_dictionary["id"]

# Create __name__ == "__main__" idiom.
if __name__ == "__main__":
    print('This file cannot be executed as a script.\n\nExecute "spotify_playlist_mulit-level_sorting.py" to sort playlist.')