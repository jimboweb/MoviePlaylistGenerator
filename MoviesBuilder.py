from typing import List, Dict
from Movie import Movie
from JsonHandler import getvalsfromjsn, get_json

def get_headers(header_line:List[str])->Dict[str,int]:
    headers = {}
    for j, h in enumerate(header_line):
        headers[h] = j
    return headers


def make_movies(movie_list:List[str],credits_list:List[str])->List[Movie]:
    movie_dict = {}
    headers = None
    for i,mline in enumerate(movie_list):
        if i == 0:
            h = get_headers(mline)
        elif len(mline) < len(h):
            continue
        else:
            id = mline[h["id"]]
            title = mline[h["title"]]
            genres = getvalsfromjsn(mline[h["genres"]], "name")
            keywords = getvalsfromjsn(mline[h["keywords"]],"name")
            popularity = mline[h["popularity"]]
            movie_dict[id] = Movie(title,genres,keywords,popularity)

    headers = {}
    for i,cline in enumerate(credits_list):
        if i == 0:
            h = get_headers(cline)
        elif len(mline) < len(h):
            continue
        else:
            id = cline[h["movie_id"]]
            if id in movie_dict:
                movie = movie_dict[id]
            else:
                continue
            cast = cline[h["cast"]]
            actors = getvalsfromjsn(cast,"name")
            movie.actors = actors
            # for crewmember in get_json(cline[h["crew"]]):
            #     if(crewmember["job"]=="director"):
            #         movie.director = crewmember["name"]
            movie_dict.update({id:movie})
    return list(movie_dict.values())
