from typing import List

class Movie:
    def __init__(self, title:str, genres:List[str], keywords:List[str], popularity:int):
        self.title = title
        self.genres = genres
        self.keywords = keywords
        self.popularity = popularity
        self.actors = []
        self.director = None

    def __str__(self):
        return "title: {}, genres: {}, keywords: {}, popularity: {}, actors:{}, director{}".format(
            self.title,self.genres,self.keywords,self.popularity, self.actors, self.director)
