import json

# API--?

dict1 = r'{"Name": "Ramesh","Age": 20,"Profession": "Rat", }'
with open("JsonfileDemo.json", "r") as f:
    a = f.read()
    print(a)

# --> Data (1000 rows)
# --> Age == Ramesh ?
# --> Req ("Name"="Ramesh") --> backend
# --> keys() and values()  "Name", "Ramesh"
# SQL Query --> SELECT Age from Student Where Key = Value; --> opetimization of SQL -- data security
# Output Res --> {"Age":20} --> Res.(200) -->net travel
# client machine --> HTML, React, --> javascript --> decode (parse) -->
# Output = 20

val = json.dump(dict1, separators=",")

print(val)

## TO-DO : --> What and When?
