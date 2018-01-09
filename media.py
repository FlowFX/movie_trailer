import webbrowser


class Movie():
    """Class that provides a way to store movie related information.

    Args:
        movie_title (str): Movie's title.
        movie_storyline (str): Movie's summary.
        poster_image (str): URL of Movie poster.
        trailer_youtube (str): URL of Movie's trailer on YouTube.

    Attributes:
        movie_title (str): Movie's title.
        movie_storyline (str): Movie's summary.
        poster_image (str): URL of Movie's poster.
        trailer_youtube (str): URL of Movie's trailer on YouTube.

    Methods:
        show_trailer (): Open YouTube link in webbrowser.
    """
    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Opens up a webbrowser and shows the Movie's trailer on YouTube.

        Args:
            None

        Returns:
            None
        """
        webbrowser.open(self.trailer_youtube_url)
