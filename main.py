from FileReader import read_csv
def main():
    movies = read_csv("movies.csv")
    credits = read_csv("credits.csv")
    print(movies[0])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
