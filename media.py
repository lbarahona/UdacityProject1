import webbrowser

# base class for Fresh Tomatoes movie website project
class Movie() :

	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube,
				release_date, director, running_time, mpaa_rating):

		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.release_date = release_date
		self.director = director
		self.running_time = running_time
		self.mpaa_rating = mpaa_rating


	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)