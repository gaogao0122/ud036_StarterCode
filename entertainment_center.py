import media
import fresh_tomatoes

# Toy story movie: movie title, storyline, poster image and movie trailer
toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # NOQA
    "https://www.youtube.com/watch?v=KYz2wyBy3kc"
    )

# Avatar movie: movie title, storyline, poster image and movie trailer
avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=5PSNL1qE6VY"
     )

# School of rock movie: movie title, storyline, poster image and movie trailer
school_of_rock = media.Movie(
    "School of Rock",
    "Using rock music to learn",
    "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=3PsUJFEBC74"
    )

# Ratatouille movie: movie title, storyline, poster image and movie trailer
ratatouille = media.Movie(
    "Ratatouille",
    "Storyline",
    "http://www.pixartalk.com/wp-content/uploads/2009/06/ratrussian1.jpg",  # NOQA
    "https://www.youtube.com/watch?v=c3sBBRxDAqk"
    )

# Midnight in paris movie: movie title, storyline,
# poster image and movie trailer
midnight_in_paris = media.Movie(
    "Midnight in Paris",
    "Storyline",
    "https://upload.wikimedia.org/wikipedia/zh/9/9f/Midnight_in_Paris_Poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=FAfR8omt-CY"
    )

# The hunger games movie: movie title,
# storyline, poster image and movie trailer
the_hunger_games = media.Movie(
    "The Hunger Games",
    "Storyline",
    "https://upload.wikimedia.org/wikipedia/en/4/4b/Hunger_Games_Film_Poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=4S9a5V9ODuY"
    )

# An array with all movies which will be used
# to fresh_tomatoes.py file to create the movie website
movies = [
    toy_story, avatar, school_of_rock,
    ratatouille, midnight_in_paris, the_hunger_games
    ]

# open the HTML file in a webbrowser via fresh_tomatoes.py file
fresh_tomatoes.open_movies_page(movies)
