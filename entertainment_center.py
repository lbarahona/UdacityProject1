import fresh_tomatoes
import media


john_wick = media.Movie("John Wick",
						"Legendary assassin John Wick (Keanu Reeves) retired from his violent career after marrying the love of his life. Her sudden death leaves John in deep mourning. When sadistic mobster Iosef Tarasov (Alfie Allen) and his thugs steal John's prized car and kill the puppy that was a last gift from his wife, John unleashes the remorseless killing machine within and seeks vengeance. Meanwhile, Iosef's father (Michael Nyqvist) -- John's former colleague -- puts a huge bounty on John's head.",
						"http://upload.wikimedia.org/wikipedia/en/9/98/John_Wick_TeaserPoster.jpg",
						"https://www.youtube.com/watch?v=C0BMx-qxsP4")

the_equalizer = media.Movie("The Equalizer",
						"Robert McCall (Denzel Washington), a man of mysterious origin who believes he has put the past behind him, dedicates himself to creating a quiet new life. However, when he meets Teri (Chloe Grace Moretz), a teenager who has been manhandled by violent Russian mobsters, he simply cannot walk away. With his set of formidable skills, McCall comes out of self-imposed retirement and emerges as an avenging angel, ready to take down anyone who brutalizes the helpless.",
						"http://upload.wikimedia.org/wikipedia/en/8/81/The_Equalizer_poster.jpg",
						"https://www.youtube.com/watch?v=jAI7rF0eQyQ")

die_hard = media.Movie("Die Hard",
						"New York City cop John McClane (Bruce Willis) arrives in Moscow to track down his estranged son, Jack (Jai Courtney). McClane thinks his son is a criminal, so it comes as a shock when he learns that Jack is actually working undercover to protect Komarov (Sebastian Koch), a Russian government whistleblower. With their own lives on the line, McClane and Jack must overcome their differences in order to get Komarov to safety and thwart a potentially disastrous crime in the Chernobyl region.",
						"http://ia.media-imdb.com/images/M/MV5BMTcwNzgyNzUzOV5BMl5BanBnXkFtZTcwMzAwOTA5OA@@._V1_SX640_SY720_.jpg",
						"https://www.youtube.com/watch?v=C0BMx-qxsP4")


movies = [john_wick, the_equalizer, die_hard]

fresh_tomatoes.open_movies_page(movies)



	