import csv
with open ("C:/Users/HOME/Downloads/height-weight.csv",newline="") as medianfile:
    reader=csv.reader(medianfile)
    filedata = list(reader)
    filedata.pop(0)
    newdata = []
    for i in range (len(filedata)):
        lines=filedata[i][1]
        newdata.append(lines)
    n = len(newdata)
    newdata.sort()
    if n%2==0:
        median1=float(newdata[n//2])
        median2=float(newdata[n//2-1])
        median=(median2+median1)/2
    else:
         median=newdata[n//2]
    print("median is= "+str(median) )        
            
