from typing import List

class Movie:
    def __init__(self, name:str, id:str, genres:List[str], keywords:List[str], popularity:int):
        self.name = name
        self.id = id
        self.genres = genres
        self.keywords = keywords
        self.popularity = popularity
        self.actors = []
        self.director = None
