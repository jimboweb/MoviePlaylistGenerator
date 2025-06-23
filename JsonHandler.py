from json import loads
from typing import List

def getvalsfromjsn(json_string:str,val_name:str)->List[str]:
    rtrn = []
    try:
        json_string = json_string[1:len(json_string)-1]
        jsn_list = loads(json_string)
        for item in jsn_list:
            rtrn.append(item[val_name])
    except ValueError as e:
        print("JSON error"+str(e))
    return rtrn
