
from re import M
from unicodedata import name


def read():
    test = open(r"C:\Users\gabri\OneDrive\Dokument\GitHub\NetworkProgramming\Project\LaborationTwo\score2.txt", "r")
    d = dict()
    for x in test:
        values = x.split() 
        name = values[2] + " " + values [3]
        points = int(values[4])
        if name in d.keys():
            #if name 
            d[name] += points
        else:
            d[name] = points
    maxPoints = 0
    for name in d.keys():
        points = d[name]
        if maxPoints < points:
            maxPoints = points    
    print(maxPoints)
    for name in d.keys():
        if d[name] == maxPoints:
            print(name) 
        
    test.close()
    
read()