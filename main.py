from FileReader import read_csv
from JsonHandler import getvalsfromjsn
def main():
    movies = read_csv("movies.csv")
    credits = read_csv("credits.csv")
    # print(movies[1][1])
    avatar_genres = getvalsfromjsn(movies[1][1],"name")
    for genre in avatar_genres:
        print(genre)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
