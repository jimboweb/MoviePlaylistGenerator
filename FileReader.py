from typing import List

def read_csv(filename:str)->List[List[str]]:
    path = "tmdb5000movies\\"+filename
    rtrn = []
    with open(path,'r') as f:
        lines = f.readlines()
        for line in lines:
            rtrn+=line.strip().split(",")
    return rtrn
