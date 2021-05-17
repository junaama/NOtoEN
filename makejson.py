import json
import re
filename = 'nb-NOtoENdictionary.txt'

overalldict = {}
count = 0

with open(filename) as fh:
    for line in fh:
        tempdict = {}
        
        word, definition = line.strip().split("	", 1)
        newdef = definition.strip().split("	")
        tempdict[word] = newdef
        overalldict[count] = tempdict
        count+= 1
out_file = open("final.json", "w")
json.dump(overalldict, out_file, indent  = 4, sort_keys = False, ensure_ascii=False)
out_file.close()
