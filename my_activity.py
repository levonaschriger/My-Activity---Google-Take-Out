import numpy as np
import json
from matplotlib import pyplot as plt
data = open('myactivity.json', 'r')
variable_name = json.load(data)

list_value = []
for key in variable_name:
    value = key.get("title", None)
    list_value.append(value)
    seen = {}
    dupes = []
for x in list_value:
    if x not in seen:
           seen[x] = 1
    else:
        
        if seen[x] == 1:
            dupes.append(x)
        seen[x] += 1
  
sorted_seen = {k: v for k, v in sorted(seen.items(), key=lambda item: item[1],reverse = True )
x_axises = []
y_axises = []
    for key, value in sorted_seen.items():
        x_axises.append(key)
        y_axises.append(value)
x = np.linspace(0,10, num = len(x_axises))
y = y_axises
plt.loglog(x,y)
plt.title('log-log graph: querys issued on my google takeout')
plt.xlabel('rank of the query in a descending order')
plt.ylabel('number of times the query was issued')
  

    time_value = []
    for key in variable_name:
        value = key.get(\"time\", None)
        time_value.append(value)
   
    years = []
    for i in range(0,len(time_value)):
         years.append(time_value[i][:4])  
    seen = {}
    dupes = []
    for x in years:
        if x not in seen:
            seen[x] = 1
        else:
           if seen[x] == 1:
                dupes.append(x)
           seen[x] += 1

    sorted_time_value = {k: v for k, v in sorted(seen.items(), key=lambda item: item[1],reverse = True )}
    x = []
    y = []
    for key, value in sorted_time_value.items():
        x.append(key)
        y.append(value)

pos = np.arange(len(x))
width = 1.0   
ax = plt.axes()
ax.set_xticks(pos + (width / 2))
ax.set_xticklabels(x)
plt.bar(pos, y, width, color='r')
plt.title('histogram of number of querys issued each year')
plt.xlabel('years')
plt.ylabel('number of querys issued')
plt.show()
