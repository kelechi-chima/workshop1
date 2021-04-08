from flask import Flask
from flask import render_template
from flask import request
from optparse import OptionParser

parser = OptionParser()
parser.add_option("--film-name", dest="film_name")
parser.add_option("--stars", dest="rating")

app = Flask(__name__)

if __name__ == "__main__":
    (options, args) = parser.parse_args()
    with open("/Users/kchima/Documents/Corndel/code/workshop1/film_ratings_app/ratings.txt", "a") as ratings_file:
        ratings_file.write(f"{options.film_name}, {options.rating}\n")

def read_ratings_file():
    data = []
    with open("/Users/kchima/Documents/Corndel/code/workshop1/film_ratings_app/ratings.txt") as ratings_file:
        for film in ratings_file:
            film_name, rating = film.split(", ")
            data.append({"name": film_name, "rating": int(rating)})
    return data

@app.route("/films/list")
def films_list():
    return render_template("films_list.html")

@app.route("/films/table")
def films_table():
    data = read_ratings_file()
    requested_stars = request.args.get("stars")
    if requested_stars is not None:
        try:
            requested_stars = int(requested_stars)
        except ValueError:
            print(f"{requested_stars} is not a valid int")
        else:
            data = [film for film in data if film["rating"] == requested_stars]
    return render_template("films_table.html", films=data)

@app.route("/films/submit", methods=["GET", "POST"])
def submit_film():
    if request.method == "GET":
        data = read_ratings_file()
        return render_template("submit_film.html", films=data)
    elif request.method == "POST":
        film_name = request.form["filmname"]
        rating = request.form["rating"]
        with open("/Users/kchima/Documents/Corndel/code/workshop1/film_ratings_app/ratings.txt", "a") as ratings_file:
            ratings_file.write(f"{film_name}, {rating}\n")
        data = read_ratings_file()
        return render_template("films_table.html", films=data)
