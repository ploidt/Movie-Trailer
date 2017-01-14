import webbrowser

class Movie():
    #crete an init of Movie class
    def __init__(self,movie_title,movie_poster,movie_trailer_url):
        self.title = movie_title
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer_url

    #create a method that will open the trailer in the web browser
    def show_trailer(self):
        webbrowser.open(trailer_youtube_url)
