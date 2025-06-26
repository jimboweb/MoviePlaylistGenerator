from typing import List,Dict
from Movie import Movie
from Edge import Edge

def make_key(id1:int,id2:int)->str:
    first:str = str(min(id1,id2))
    second:str = str(max(id1,id2))
    return first + "x" + second

def update_probability(prior: int,new:int)->int:
    return prior + new

def update_edges_by_property(edges_dict:Dict[str,Edge], prop_name: str, movies:Dict[int,Movie],p:float)->Dict[str,Edge]:
    prop_dict: Dict[str, List[int]] = {}
    for k in movies.keys():
        movie = movies[k]
        l = None
        if prop_name == "genre":
            l = movie.genres
        elif prop_name == "keyword":
            l = movie.keywords
        else:
            l = movie.actors
        for prop in l:
            if prop in prop_dict:
                for other_id in prop_dict[prop]:
                    edge_key = make_key(k,other_id)
                    edge = edges_dict[edge_key]
                    edge.weight = update_probability(edge.weight,p)
                    edges_dict.update({edge_key:edge})
                prop_dict[prop].append(k)
            else:
                prop_dict[prop] = [k]
    return edges_dict

def make_graph(movies:Dict[id,Movie])-> Dict[str,Edge]:
    common_actor:float = 1
    common_genre:float = 1
    common_keyword:float = 2
    edges_dict:Dict[str,Edge] = {}
    genre_dict:Dict[str,List[int]] = {}
    keyword_dict:Dict[str,List[int]] = {}
    actor_dict:Dict[str,List[int]] = {}
    for id1 in movies.keys():
        for id2 in movies.keys():
            key = make_key(id1,id2)
            if key not in edges_dict:
                edges_dict[key]=Edge(movies[id1],movies[id2],0)
    edges_dict = update_edges_by_property(edges_dict,"genre",movies,common_genre)
    edges_dict = update_edges_by_property(edges_dict,"keyword",movies,common_keyword)
    edges_dict = update_edges_by_property(edges_dict,"actor",movies,common_actor)
    return edges_dict
