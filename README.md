# Mini-Project: Playlist Management API

This project implements a dynamic playlist management system using Flask. Users can create, manage, and explore playlists with functionalities like adding/removing songs, searching playlists, and basic CRUD operations.


### Getting Started

This API utilizes the Python library Flask.

This will run the API on http://127.0.0.1:5000 by default


### API Endpoints

The API provides functionalities for managing playlists and songs through various endpoints:

**Playlist Endpoints:**

* **Create Playlist (POST /playlist/create):**
    * Request Body (JSON):
        * name: (required) Name of the playlist.
        * description: (required) Description of the playlist.
    * Response:
        * On success (status code 201): JSON object containing the newly created playlist's ID.
        * On error (status code 400): JSON object with an error message (e.g., missing required fields).
* **Get Playlist (GET /playlist/&lt;id>):**
    * Path Parameter: &lt;playlist_id> (Unique identifier of the playlist)
    * Response:
        * On success (status code 200): JSON object containing the playlist details (name, description, songs).
        * On error (status code 404): JSON object with an error message (playlist not found).
* **Update Playlist (PUT /playlist/update/&lt;id>):**
    * Path Parameter: &lt;id> (Unique identifier of the playlist)
    * Request Body (JSON):
        * name (optional): Updated name of the playlist.
        * description (optional): Updated description of the playlist.
    * Response:
        * On success (status code 200): JSON object with a success message ("Playlist updated successfully").
        * On error (status code 404): JSON object with an error message ("Playlist not found").
* **Delete Playlist (DELETE /playlist/delete/&lt;id>):**
    * Path Parameter: &lt;playlist_id> (Unique identifier of the playlist)
    * Response:
        * On success (status code 200): JSON object with a success message ("Playlist deleted successfully").
        * On error (status code 404): JSON object with an error message ("Playlist not found").

**Song Endpoints**

* **Add Song to Playlist (POST /playlist/&lt;id>/add_song):**
    * Adds a song to a specific playlist.
    * Path Parameter: &lt;id> (Unique identifier of the playlist)
    * Request Body (JSON):
        * title: Title of the song.
        * artist: Artist of the song.
    * Response:
        * On success (status code 201): JSON object with a success message ("Song added to playlist successfully").
* **Remove Song from Playlist (DELETE /playlist/&lt;id>/remove_song/&lt;song_id>):**
    * Removes a song from a specific playlist.
    * Path Parameters:
        * &lt;id>: Unique identifier of the playlist
        * &lt;song_id>: Unique identifier of the song within the playlist
    * Response:
        * On success (status code 200): JSON object with a success message ("Song removed from playlist successfully").

**Search Song Endpoint**

* **Search Song (GET /playlist/songsearch/&lt;query>):**
    * Searches for songs in playlists based on title or artist name (case-insensitive).
    * Path Parameter: &lt;query> (Search query string)
    * Response:
        * On success: JSON array containing the results of the seacch