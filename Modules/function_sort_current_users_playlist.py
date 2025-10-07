# Import required modules.
# spotipy is used for interacting with the Spotify API.
import spotipy

# Create function to sort current user's selected playlist.
def sort_current_users_playlist(spotify_authorization, playlist_id):
    # Create variable to store data from playlist_items method of spotipy
    get_playlist_items_data = spotify_authorization.playlist_items(playlist_id=playlist_id,
                                                                   limit=100,
                                                                   offset=0,
                                                                   additional_types=['track'])

    # Create empty list to store dictionaries.
    tracks_list = []

    # Create loop to iterate through playlist tracks.
    for tracks in range(len(get_playlist_items_data["items"])):
        # Create empty dictionary to store data about each track.
        tracks_data_dictionary = {}
        # Check if "Various Artists" is the album_artis.
        # If it is, track artist will be used for sorting.
        if get_playlist_items_data["items"][tracks]["track"]["album"]["artists"][0]["name"] == "Various Artists":
            # Update tracks_data_dictionary with key:value pair.
            tracks_data_dictionary.update({"artist":get_playlist_items_data["items"][tracks]["track"]["artists"][0]["name"]})
            # Update tracks_data_dictionary with key:value pair.
            tracks_data_dictionary.update({"album":get_playlist_items_data["items"][tracks]["track"]["album"]["name"]})
            # Update tracks_data_dictionary with key:value pair.
            tracks_data_dictionary.update({"release_date":get_playlist_items_data["items"][tracks]["track"]["album"]["release_date"]})
            # Update tracks_data_dictionary with key:value pair.
            tracks_data_dictionary.update({"track":get_playlist_items_data["items"][tracks]["track"]["name"]})
            # Update tracks_data_dictionary with key:value pair.
            tracks_data_dictionary.update({"track_number":get_playlist_items_data["items"][tracks]["track"]["track_number"]})
            # Update tracks_data_dictionary with key:value pair.
            tracks_data_dictionary.update({"disc_number":get_playlist_items_data["items"][tracks]["track"]["disc_number"]})
            # Update tracks_data__dictionary with key:value pair.
            tracks_data_dictionary.update({"id":get_playlist_items_data["items"][tracks]["track"]["id"]})
            # Append playlists_data_dictionary to tracks_list
            tracks_list.append(tracks_data_dictionary)
        elif get_playlist_items_data["items"][tracks]["track"]["album"]["artists"][0]["name"] != "Various Artists":
            # Update tracks_data_dictionary with key:value pair.
            tracks_data_dictionary.update({"artist":get_playlist_items_data["items"][tracks]["track"]["album"]["artists"][0]["name"]})
            # Update tracks_data_dictionary with key:value pair.
            tracks_data_dictionary.update({"album":get_playlist_items_data["items"][tracks]["track"]["album"]["name"]})
            # Update tracks_data_dictionary with key:value pair.
            tracks_data_dictionary.update({"release_date":get_playlist_items_data["items"][tracks]["track"]["album"]["release_date"]})
            # Update tracks_data_dictionary with key:value pair.
            tracks_data_dictionary.update({"track":get_playlist_items_data["items"][tracks]["track"]["name"]})
            # Update tracks_data_dictionary with key:value pair.
            tracks_data_dictionary.update({"track_number":get_playlist_items_data["items"][tracks]["track"]["track_number"]})
            # Update tracks_data_dictionary with key:value pair.
            tracks_data_dictionary.update({"disc_number":get_playlist_items_data["items"][tracks]["track"]["disc_number"]})
            # Update tracks_data__dictionary with key:value pair.
            tracks_data_dictionary.update({"id":get_playlist_items_data["items"][tracks]["track"]["id"]})
            # Append playlists_data_dictionary to tracks_list
            tracks_list.append(tracks_data_dictionary)

    # Create while loop to look for next set of paginated results.
    while get_playlist_items_data["next"]:
        # Set variable get_playlist_items_data value to the next set of paginated results.
        get_playlist_items_data = spotify_authorization.next(get_playlist_items_data)
        # Create loop to iterate through playlist tracks.
        for tracks in range(len(get_playlist_items_data["items"])):
            # Create empty dictionary to store data about each track.
            tracks_data_dictionary = {}
            # Check if "Various Artists" is the album_artis.
            # If it is, track artist will be used for sorting.
            if get_playlist_items_data["items"][tracks]["track"]["album"]["artists"][0]["name"] == "Various Artists":
                # Update tracks_data_dictionary with key:value pair.
                tracks_data_dictionary.update({"artist":get_playlist_items_data["items"][tracks]["track"]["artists"][0]["name"]})
                # Update tracks_data_dictionary with key:value pair.
                tracks_data_dictionary.update({"album":get_playlist_items_data["items"][tracks]["track"]["album"]["name"]})
                # Update tracks_data_dictionary with key:value pair.
                tracks_data_dictionary.update({"release_date":get_playlist_items_data["items"][tracks]["track"]["album"]["release_date"]})
                # Update tracks_data_dictionary with key:value pair.
                tracks_data_dictionary.update({"track":get_playlist_items_data["items"][tracks]["track"]["name"]})
                # Update tracks_data_dictionary with key:value pair.
                tracks_data_dictionary.update({"track_number":get_playlist_items_data["items"][tracks]["track"]["track_number"]})
                # Update tracks_data_dictionary with key:value pair.
                tracks_data_dictionary.update({"disc_number":get_playlist_items_data["items"][tracks]["track"]["disc_number"]})
                # Update tracks_data__dictionary with key:value pair.
                tracks_data_dictionary.update({"id":get_playlist_items_data["items"][tracks]["track"]["id"]})
                # Append playlists_data_dictionary to tracks_list
                tracks_list.append(tracks_data_dictionary)
            elif get_playlist_items_data["items"][tracks]["track"]["album"]["artists"][0]["name"] != "Various Artists":
                # Update tracks_data_dictionary with key:value pair.
                tracks_data_dictionary.update({"artist":get_playlist_items_data["items"][tracks]["track"]["album"]["artists"][0]["name"]})
                # Update tracks_data_dictionary with key:value pair.
                tracks_data_dictionary.update({"album":get_playlist_items_data["items"][tracks]["track"]["album"]["name"]})
                # Update tracks_data_dictionary with key:value pair.
                tracks_data_dictionary.update({"release_date":get_playlist_items_data["items"][tracks]["track"]["album"]["release_date"]})
                # Update tracks_data_dictionary with key:value pair.
                tracks_data_dictionary.update({"track":get_playlist_items_data["items"][tracks]["track"]["name"]})
                # Update tracks_data_dictionary with key:value pair.
                tracks_data_dictionary.update({"track_number":get_playlist_items_data["items"][tracks]["track"]["track_number"]})
                # Update tracks_data_dictionary with key:value pair.
                tracks_data_dictionary.update({"disc_number":get_playlist_items_data["items"][tracks]["track"]["disc_number"]})
                # Update tracks_data__dictionary with key:value pair.
                tracks_data_dictionary.update({"id":get_playlist_items_data["items"][tracks]["track"]["id"]})
                # Append playlists_data_dictionary to tracks_list
                tracks_list.append(tracks_data_dictionary)

    # Sort list of dictionaries by multiple keys.
    # Sorting is performed by album_artist, release_date, album, disc_number, and then track_number
    # The casefold() method returns all characters as lowercase.
    # If this is not performed, uppercase and lowercase characters will be sorted separately even if they are the same character.
    # By default, sorting is performed in ASCIIbetical order which puts uppercase letters before lowercase letters.
    tracks_list = sorted(tracks_list,
                         key=lambda track:(track["artist"].casefold(),
                                           track["release_date"].casefold(),
                                           track["album"].casefold(),
                                           track["disc_number"],
                                           track["track_number"]))

    # Create empty list to store track ids.
    ids_list = []

    # Create loop to iterate through tracks.
    for ids in range(len(tracks_list)):
        # Append track id to ids_list
        ids_list.append(tracks_list[ids]["id"])

    # Create empty list to store ids in nested lists.
    # This is required as there is a maximum of 100 items in one request.
    ids_list_of_lists = []

    # Slice the ids_list into smaller 100 item lists and add them to ids_list_of_lists
    # Additional information can be found here: https://www.geeksforgeeks.org/break-list-chunks-size-n-python/
    # Additional information can be found here: https://www.geeksforgeeks.org/python-list-slicing/
    # Starting item in list. 0 is the first item. We start at 0 because this is eventually passed to the range() function.
    start = 0
    # Ending item in list. Gathered from the len() function.
    end = len(ids_list)
    # Increments to take. Will gather 100 track ids at a time.
    step = 100
    # Create loop to iterate through tracks and append lists of 100 track ids to ids_list_of_lists
    for track_ids in range(start, end, step):
        sliced_track_ids = track_ids
        ids_list_of_lists.append((ids_list[sliced_track_ids:sliced_track_ids+step]))

    # Create loop to iterate through ids lists to delete all tracks in the playlist.
    for ids_list in range(len(ids_list_of_lists)):
        spotify_authorization.playlist_remove_all_occurrences_of_items(playlist_id=playlist_id,
                                                                       items=ids_list_of_lists[ids_list])

    # Create loop to iterate through ids lists to add tracks to the playlist.
    for ids_list in range(len(ids_list_of_lists)):
            spotify_authorization.playlist_add_items(playlist_id=playlist_id,
                                                     items=ids_list_of_lists[ids_list])

    # Print update to console.
    print(f"Playlist has been sorted.")

# Create __name__ == "__main__" idiom.
if __name__ == "__main__":
    print('This file cannot be executed as a script.\n\nExecute "spotify_playlist_mulit-level_sorting.py" to sort playlist.')