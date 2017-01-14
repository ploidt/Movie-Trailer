import webbrowser
class Movie():
    def __init__(self,movie_title,movie_poster,movie_trailer_url):
        self.title = movie_title
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer_url
    
    def show_trailer(self):
        webbrowser.open(trailer_youtube_url)
