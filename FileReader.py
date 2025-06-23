from typing import List

def read_csv(filename:str)->List[List[str]]:
    path = "tmdb5000movies/"+filename
    rtrn = []
    try:
        with open(path,'r') as f:
            lines = f.readlines()
            for line in lines:
                buffer = ""
                l = []
                is_json = False
                prev_is_qt = False
                for i in range(len(line)-1):
                    c = line[i]
                    if not is_json:
                        if c == ',':
                            if line[i+1] == '"' and line[i+2] == '[':
                                is_json = True
                            l.append(buffer)
                            buffer = ""
                        else:
                            buffer += c
                    else:
                        if c == ']':
                            is_json = False
                        if c == '"':
                            if prev_is_qt:
                                prev_is_qt = False
                                continue
                            else:
                                prev_is_qt = True
                        buffer += c
                rtrn.append(l)
        return rtrn
    except IOError as e:
        print("exception reading file:" + e)
