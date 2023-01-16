bq={"sq":{1:1,2:4,3:9,4:16,5:25},"cu":{1:1,2:8,3:27,4:64,5:125}}
print(bq)
bqq=pd.DataFrame(bq,index=[1,2,3,4,5])
print(bqq)

for i in bq:
    print("keys are:",i)
    for j in bq[i]:
        print("vaules are of",j,"is",bq[i][j])
