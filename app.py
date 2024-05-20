from flask import Flask, request
app = Flask(__name__)

playlists = {}

@app.route("/")
def home(): return "<h1>Mini Project: Playlist Management API</h1>"

@app.route('/playlist/create', methods=['POST'])
def create_playlist():
    data = request.json
    name = data.get('name')
    descr = data.get('description')
    if not name or not descr: return {'error': 'name and description are required'}, 400
    id = len(playlists)+1
    playlists[id] = {'name': name, 'description': descr, 'songs': []}
    return {'playlist id': id}, 201

@app.route('/playlist/<int:id>', methods=['GET'])
def get_playlist(id):
    if id in playlists: return playlists[id]
    return {'error': 'Playlist not found'}, 404

@app.route('/playlist/update/<int:id>', methods=['PUT'])
def update_playlist(id):
    if id not in playlists: return  {'error': 'Playlist not found'}, 404
    data = request.json
    name = data.get('name')
    if name: playlists[id]['name'] = name
    descr = data.get('description')
    if descr: playlists[id]['description'] = descr
    return {'message': 'Playlist updated successfully'}, 200

@app. route('/playlist/delete/<int:id>', methods=['DELETE'])
def delete_playlist(id):
    if id not in playlists: return  {'error': 'Playlist not found'}, 404
    del playlists[id]
    return {'message': 'Playlist deleted successfully'}, 200

@app.route('/playlist/<int:id>/add_song', methods=['POST'])
def add_song_to_playlist(id):
    data = request.json
    song_id = len(playlists[id]['songs']) + 1
    song = {"song_id": song_id, "title": data.get('title'), "artist": data.get('artist')}
    playlists[id]['songs'].append(song)
    return {'message': 'Song added to playlist successfully'}, 201

@app.route('/playlist/<int:id>/remove_song/<int:song_id>', methods=['DELETE'])
def remove_song_from_playlist(id, song_id):
    playlists[id]['songs'] = [song for song in playlists[id]["songs"] if song["song_id"] != song_id]
    return {'message': 'Song removed from playlist successfully'}

@app.route('/playlist/songsearch/<string:query>', methods=['GET'])
def search_song(query):
    results = []
    query = query.lower()
    for id in playlists:
        for song in playlists[id]['songs']:
            if query in song['title'].lower() or query in song['artist'].lower():
                results.append(("Playlist: "+str(id)+" ("+playlists[id]['name'] + ")", song))
    return results

if __name__ == '__main__': app.run(debug=True)