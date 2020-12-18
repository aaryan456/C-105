import csv 
with open("C:/Users/HOME/Downloads/height-weight.csv",newline="") as f:
    reader = csv.reader(f)
    filedata = list(reader)
filedata.pop(0)
newdata = []
for i in range(len(filedata)):
    infiniteno=filedata[i][1]
    newdata.append(float(infiniteno))
calclength=len(newdata)
total=0
for x in newdata:
    total=total+x
mean=total/calclength
print(str(mean))            
