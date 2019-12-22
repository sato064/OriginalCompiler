#Reading source code
path1 = "samplesource.txt"
file1 = open(path1,'r',encoding='utf-8')
f1 = file1.readlines()
file1.close()

#Analysis
P_Len = len(f1)
print(P_Len)
PG = 0
n = 0

while(PG < P_Len):
    print(f1[PG])
    if(f1[PG] == "START\n"):
        print("RETURN 10000")
    if(f1[PG] == "END"):
        print("RETURN 10001")
    #print(len(f1[PG]))
    n = 0
    while(len(f1[PG]) > n):
        #print(f1[PG][n])
        n += 1
    
    PG += 1






print(f1)