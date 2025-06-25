from typing import Dict
from Movie import Movie
from JsonHandler import dump_movie_to_file

def write_movies(movies:Dict[int,Movie])->None:
    with open("movies_processed.txt","w") as f:
        for key in movies.keys():
            f.write(str(key)+ ":")
            dump_movie_to_file(movies[key],f)
