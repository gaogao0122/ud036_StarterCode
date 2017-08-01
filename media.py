import webbrowser


class Movie():
    """ This class provides a way to store movie related information"""

    # This array contains all the movie's degree
    VALID_RATING = ["G", "PG", "PG-13", "R"]

    '''the constructor of class movie
    input: movie title, storyline, poster image and movie trailer '''
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # This function is used to open the movie's trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
