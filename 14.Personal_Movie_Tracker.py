import os
import json

FILENAME = "movies.json"

def load_movies():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as f:
        return json.load(f)
    
def save_movies(movies):
    with open(FILENAME,"w") as f:
        json.dump(movies, f, indent=2)

def add_movie(movies):
    name = input("Enter the name of movie: ")
    if any(movie["name"] == name for movie in movies):
        print("Movie already exists.")
        return 
    genre = input("Enter the genre of the movie: ")
    try:
        rating = float(input("Enter your rating for the movie (0-10): "))
        if rating < 0 or rating > 10:
            print("Rating must be between 0 and 10.")
            return  
    except ValueError:
        print("Invalid rating. Please enter a number between 0 and 10.")
        return
    movies.append({"name": name, "genre": genre, "rating": rating})
    save_movies(movies)
    print("Movie added successfully.")

def search_movies(movies):
    inp = input("Enter the name or genre to search: ").lower()
    results = [movie for movie in movies
               if inp in movie["name"].lower() or inp in movie["genre"].lower()]
    if not results:
        print("No movies found.")
        return
    print(f"Found {len(results)} movies:")
    for movie in results:
        print(f"Name: {movie['name']}, Genre: {movie['genre']}, Rating: {movie['rating']}")

def view_movies(movies):
    if not movies:
        print("No movies to display.")
        return
    print("All movies:")
    for movie in movies:
        print(f"Name: {movie['name']}, Genre: {movie['genre']}, Rating: {movie['rating']}")

def run():
    movies = load_movies()
    while True:
        print("\nPersonal Movie Tracker")
        print("1. Add a movie")
        print("2. View all movies")
        print("3. Search movies")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_movie(movies)
        elif choice == "2":
            view_movies(movies)
        elif choice == "3":
            search_movies(movies)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run()