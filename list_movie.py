import movie
import fresh_tomatoes

# Rouge One Movie
rouge_one = movie.Movie("Rogue One",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/d/d4/Rogue_One%2C_A_Star_Wars_Story_poster.png/220px-Rogue_One%2C_A_Star_Wars_Story_poster.png",
                        "https://www.youtube.com/watch?v=frdj1zb9sMY")
# Minions Movie
minions = movie.Movie("Minions",
                      "https://upload.wikimedia.org/wikipedia/en/3/3d/Minions_poster.jpg",
                      "https://www.youtube.com/watch?v=P9-FCC6I7u0")

# La La Land Movie
la_la_land = movie.Movie("La La Land",
                           "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png",
                           "https://www.youtube.com/watch?v=0pdqf4P9MB8")

# Secret Life of Pets Movie
secret_life_of_pets = movie.Movie("The Secret Life Of Pets",
                                  "https://upload.wikimedia.org/wikipedia/en/thumb/6/64/The_Secret_Life_of_Pets_poster.jpg/220px-The_Secret_Life_of_Pets_poster.jpg",
                                  "https://www.youtube.com/watch?v=UZJVc_JTI_w")

# Conjuring 2 Movie
conjuring_2 = movie.Movie("The Conjuring 2",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/b/b9/Conjuring_2.jpg/220px-Conjuring_2.jpg",
                          "https://www.youtube.com/watch?v=KyA9AtUOqRM")

# Your name Movie
your_name = movie.Movie("Your name",
                        "https://upload.wikimedia.org/wikipedia/en/0/0b/Your_Name_poster.png",
                        "https://www.youtube.com/watch?v=hRfHcp2GjVI")

# create a list of movies
movies = [rouge_one,minions,la_la_land,secret_life_of_pets,conjuring_2,your_name]

# generate html file and open it in the web browser
fresh_tomatoes.open_movies_page(movies)
