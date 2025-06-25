from Movie import Movie

class Edge:
    def __init__(self, movie1:Movie, movie2:Movie, weight:float):
        self.movie1 = movie1
        self.movie2 = movie2
        self.weight = weight
