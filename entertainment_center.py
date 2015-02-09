import fresh_tomatoes
import media


john_wick = media.Movie("John Wick",
						"Legendary assassin John Wick (Keanu Reeves) retired from his violent career after marrying the love of his life. Her sudden death leaves John in deep mourning. When sadistic mobster Iosef Tarasov (Alfie Allen) and his thugs steal John's prized car and kill the puppy that was a last gift from his wife, John unleashes the remorseless killing machine within and seeks vengeance. Meanwhile, Iosef's father (Michael Nyqvist) -- John's former colleague -- puts a huge bounty on John's head.",
						"http://upload.wikimedia.org/wikipedia/en/9/98/John_Wick_TeaserPoster.jpg",
						"https://www.youtube.com/watch?v=C0BMx-qxsP4",
						"October 24, 2014",
						"David Leitch, Chad Stahelski",
						"101 minutes",
						"R")

the_equalizer = media.Movie("The Equalizer",
						"Robert McCall (Denzel Washington), a man of mysterious origin who believes he has put the past behind him, dedicates himself to creating a quiet new life. However, when he meets Teri (Chloe Grace Moretz), a teenager who has been manhandled by violent Russian mobsters, he simply cannot walk away. With his set of formidable skills, McCall comes out of self-imposed retirement and emerges as an avenging angel, ready to take down anyone who brutalizes the helpless.",
						"http://upload.wikimedia.org/wikipedia/en/8/81/The_Equalizer_poster.jpg",
						"https://www.youtube.com/watch?v=jAI7rF0eQyQ",
						"September 26, 2014",
						"Antoine Fuqua",
						"131 minutes",
						"R")

die_hard = media.Movie("Die Hard",
						"New York City cop John McClane (Bruce Willis) arrives in Moscow to track down his estranged son, Jack (Jai Courtney). McClane thinks his son is a criminal, so it comes as a shock when he learns that Jack is actually working undercover to protect Komarov (Sebastian Koch), a Russian government whistleblower. With their own lives on the line, McClane and Jack must overcome their differences in order to get Komarov to safety and thwart a potentially disastrous crime in the Chernobyl region.",
						"http://ia.media-imdb.com/images/M/MV5BMTcwNzgyNzUzOV5BMl5BanBnXkFtZTcwMzAwOTA5OA@@._V1_SX640_SY720_.jpg",
						"https://www.youtube.com/watch?v=C0BMx-qxsP4",
						"February 14, 2013",
						"John Moore",
						"98 minutes",
						"R")

the_avengers = media.Movie("The Avengers",
							"When Thor's evil brother, Loki (Tom Hiddleston), gains access to the unlimited power of the energy cube called the Tesseract, Nick Fury (Samuel L. Jackson), director of S.H.I.E.L.D., initiates a superhero recruitment effort to defeat the unprecedented threat to Earth. Joining Fury's dream team are Iron Man (Robert Downey Jr.), Captain America (Chris Evans), the Hulk (Mark Ruffalo), Thor (Chris Hemsworth), the Black Widow (Scarlett Johansson) and Hawkeye (Jeremy Renner).",
							"http://x.annihil.us/u/prod/marvel/i/mg/6/50/521f70b81f7d3/portrait_incredible.jpg",
							"https://www.youtube.com/watch?v=hIR8Ar-Z4hw",
							"May 4, 2012",
							"Joss Whedon",
							"143 minutes",
							"PG-13")

fury = media.Movie("Fury",
					"In April 1945, the Allies are making their final push in the European theater. A battle-hardened Army sergeant named Don Wardaddy Collier (Brad Pitt), leading a Sherman tank and a five-man crew, undertakes a deadly mission behind enemy lines. Hopelessly outnumbered, outgunned and saddled with an inexperienced soldier (Logan Lerman) in their midst, Wardaddy and his men face overwhelming odds as they move to strike at the heart of Nazi Germany.",
					"http://ia.media-imdb.com/images/M/MV5BMjA4MDU0NTUyN15BMl5BanBnXkFtZTgwMzQxMzY4MjE@._V1_SX640_SY720_.jpg",
					"https://www.youtube.com/watch?v=-OGvZoIrXpg",
					"October 17, 2014",
					"David Ayer",
					"135 minutes",
					"R")

interstellar = media.Movie("Interstellar",
							"In Earth's future, a global crop blight and second Dust Bowl are slowly rendering the planet uninhabitable. Professor Brand (Michael Caine), a brilliant NASA physicist, is working on plans to save mankind by transporting Earth's population to a new home via a wormhole. But first, Brand must send former NASA pilot Cooper (Matthew McConaughey) and a team of researchers through the wormhole and across the galaxy to find out which of three planets could be mankind's new home.",
							"http://www.hollywoodreporter.com/sites/default/files/custom/Blog_Images/interstellar3.jpg",
							"https://www.youtube.com/watch?v=ePbKGoIGAXY",
							"November 5, 2014",
							"Christopher Nolan",
							"169 minutes",
							"PG-13")


movies = [john_wick, the_equalizer, die_hard, the_avengers, fury, interstellar]

fresh_tomatoes.open_movies_page(movies)



	