from json import loads
from typing import List

def get_json(json_string:str):
    json_string = json_string.replace('""','"')
    json_string = json_string.replace('"[','[')
    json_string = json_string.replace(']"',']')
    return loads(json_string)

def getvalsfromjsn(json_string:str,val_name:str)->List[str]:
    json_string = json_string.replace('""','"')
    json_string = json_string.replace('"[','[')
    json_string = json_string.replace(']"',']')
    rtrn = []
    try:
        jsn_list = loads(json_string)
        for item in jsn_list:
            rtrn.append(item[val_name])
    except ValueError as e:
        print("JSON error"+str(e))
    return rtrn
