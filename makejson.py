import json
import re
filename = 'nb-NOtoENdictionary.txt'

dict1 = {}

with open(filename) as fh:
    for line in fh:
        word, definition = line.strip().split("	", 1)
        newdef = definition.strip().split("	")
        dict1[word] = newdef
out_file = open("final.json", "w")
json.dump(dict1, out_file, indent  = 4, sort_keys = False, ensure_ascii=False)
out_file.close()

