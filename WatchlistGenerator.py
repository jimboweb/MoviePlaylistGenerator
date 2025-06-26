from typing import List, Dict, Tuple
from Movie import Movie
from Edge import Edge
from GraphBuilder import make_key
from random import choice, randint

def make_watchlist(movie_dict:Dict[int, Movie], edges:Dict[str, Edge], watchlist_count:int, seed_count:int, steps:int):
    names:List[str] = []
    with open("names.txt","r") as namefile:
        names = namefile.read().split(",")
    for i in range(watchlist_count):
        name = choice(names)
        watched_movie_ids:List[int] = []
        for j in range(seed_count):
            watched_movie_ids.append(choice(List[int](movie_dict.keys())))
        for j in range(steps):
            prob_dict: Dict[int:int] = {}
            for seed_id in watched_movie_ids:
                for movie_id in movie_dict.keys():
                    if movie_id == seed_id:
                        continue
                    key = make_key(seed_id,movie_id)
                    edge = edges[key]
                    if edge.weight == 0:
                        continue
                    if movie_id in prob_dict:
                        prob_dict.update({movie_id: prob_dict[movie_id] + edge.weight})
                    else:
                        prob_dict[movie_id]=edge.weight
            dartboard: List[Tuple[int,int]] = []
            max_prob:int = 0
            for movie_id in prob_dict.values():
                weight:int = prob_dict[movie_id]
                dartboard.append((max_prob+weight,movie_id))
                max_prob += weight
            dart:int = randint(0,max_prob)
            watched_movie_id:int = -1
            for tpl in dartboard:
                if tpl[0]<dart:
                    watched_movie_id = tpl[1]
            if watched_movie_id == -1:
                watched_movie_id = dartboard[len(dartboard)-1][1]
            watched_movie_ids.append(watched_movie_id)
        with open("watchlist.txt","w") as watchlist_file:
            watchlist_file.write(name + ":")
            for c,watched_movie_id in enumerate(watched_movie_ids):
                watchlist_file.write(movie_dict[watched_movie_id].title)
                if c<len(watched_movie_ids)-1:
                    watchlist_file.write(",")
            watchlist_file.write("\n")
