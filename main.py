from FileReader import read_csv
from MoviesBuilder import make_movies
from GraphBuilder import make_graph
from FileWriter import write_movies
def main():
    movie_list = read_csv("movies.csv")
    credit_list = read_csv("credits.csv")
    movies = make_movies(movie_list,credit_list)
    # write_movies(movies)
    edges_dict = make_graph(movies)
    print("")

    # TODO: make probabilistic graph object for movies
    # TODO: use graph object to make watch list

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
