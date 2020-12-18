import csv
from collections import Counter
with open ("C:/Users/HOME/Downloads/height-weight.csv",newline="") as filepath:
    read = csv.reader(filepath)
    data = list(read)
data.pop(0)
calculateddata=[]
for i in range (len(data)):
    line=data[i][1]
    calculateddata.append(line)
#caclutating the mode
datamode=Counter(calculateddata)
modedataforrange = {"50-60":0,"60-70":0,"70-80":0}
for height,occurence in datamode.items():
    if 50<float(height)<60:
        modedataforrange["50-60"]+=occurence
    elif 60<float(height)<70:
        modedataforrange["60-70"]+=occurence
    elif 70<float(height)<80:
        modedataforrange["70-80"]+=occurence
moderange,modeoccurence=0,0
for range,occurence in modedataforrange.items():
    if occurence>modeoccurence:
        moderange,modeoccurence=[int(range.split("-")[0]),int(range.split("-")[1])],occurence
mode=float((moderange[0]+moderange[1])/2)
print(f"mode is->{mode:2f}")              
    



    
   

