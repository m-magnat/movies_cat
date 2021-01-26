from flask import Flask, render_template
import tmdb_client
from flask import request

app = Flask(__name__)

@app.route('/')
def homepage():
    buttons = ["Top rated", "Upcoming", "Popular", "Now Playing"]
    types = [button.lower().replace(" ", "_") for button in buttons]
    selected_list = request.args.get('list_type', "popular")
    print(selected_list)
    if selected_list not in types:
        selected_list="popular"
    movies = tmdb_client.get_movies(how_many=8, list_type = selected_list)
    return render_template("homepage.html", movies = movies, current_list = selected_list, buttons = buttons)
    

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
   details = tmdb_client.get_single_movie(movie_id)
   cast = tmdb_client.get_single_movie_cast(movie_id)
   return render_template("movie_details.html", movie=details, cast=cast[:4])

@app.route("/index")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)