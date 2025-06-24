from FileReader import read_csv, read_tab_delim
from MoviesBuilder import make_movies
from JsonHandler import getvalsfromjsn
def main():
    movie_list = read_csv("movies.csv")
    credit_list = read_csv("credits.csv")
    movies = make_movies(movie_list,credit_list)
    print(movies[0].__str__())
    # for val in movies[1]:
    #     print(val)
    # for val in credits[1]:
    #     print(val)
    # avatar_genres = getvalsfromjsn(movies[1][1],"name")
    # for genre in avatar_genres:
    #     print(genre)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
