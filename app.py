from pymongo import MongoClient

client = MongoClient()
db = client.Playlister
playlists = db.playlists

from flask import Flask, render_template

app = Flask(__name__)

# OUR MOCK ARRAY OF PROJECTS
# playlists = [
#   { 'title': 'Great Playlist' },
#   { 'title': 'Next Playlist' }
# ]

@app.route('/')
def playlists_index():
    """Show all playlists."""
    return render_template('playlists_index.html', playlists=playlists.find())

if __name__ == '__main__':
    app.run(debug=True) 