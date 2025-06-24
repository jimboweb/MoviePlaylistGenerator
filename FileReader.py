from typing import List

def read_tab_delim(filename:str)->List[List[str]]:
    path = "tmdb5000movies/"+filename
    rtrn = []
    try:
        with open(path,'r') as f:
            lines = f.readlines()
            for line in lines:
                if len(line)>0:
                    rtrn.append(line.strip().split("\t"))
            return rtrn
    except IOError as e:
        print("exception reading file:" + e)


def read_csv(filename:str)->List[List[str]]:
    path = "tmdb5000movies/"+filename
    rtrn = []
    try:
        with open(path,'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                buffer = ""
                l = []
                is_json = False
                is_str = False
                for i in range(len(line)):
                    c = line[i]
                    if is_json:
                        if c == ']':
                            is_json = False
                        buffer += c
                    elif is_str:
                        if c == '"':
                            is_str = False
                        buffer += c
                    else:
                        if buffer == "" and c == '"':
                            if line[i+1] == '[':
                                is_json = True
                            else:
                                is_str = True
                        if c == ',':
                            l.append(buffer)
                            buffer = ""
                        else:
                            buffer += c
                l.append(buffer)
                rtrn.append(l)
        return rtrn
    except IOError as e:
        print("exception reading file:" + e)
