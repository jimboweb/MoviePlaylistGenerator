from typing import List

def read_csv(filename:str)->List[List[str]]:
    path = "tmdb5000movies/"+filename
    rtrn = []
    try:
        with open(path,'r') as f:
            lines = f.readlines()
            for line in lines:
                rtrn.append(line.strip().split(","))
        return rtrn
    except IOError as e:
        print("exception reading file:" + e)
