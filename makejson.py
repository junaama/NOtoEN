import json
import re
filename = 'nb-NOtoENdictionary.txt'

overalldict = {}
count = 0
overalldict["dictionary"] = []
with open(filename) as fh:
    for line in fh:
        tempdict = {}
        temparr = []
        word, definition = line.strip().split("	", 1)
        newdef = definition.strip().split("	")
        tempdict["id"] = count
        tempdict["word"] = word
        tempdict["definition"] = newdef
        overalldict["dictionary"].append(tempdict)
        count+= 1
out_file = open("final.json", "w")
json.dump(overalldict, out_file, indent  = 4, sort_keys = False, ensure_ascii=False)
out_file.close()
