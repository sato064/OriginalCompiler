#Reading source code
path1 = "samplesource.txt"
file1 = open(path1,'r',encoding='utf-8')
f1 = file1.readlines()
file1.close()

#Analysis
PG = 0
n = 0

while(PG <= 1):
    print(f1[PG])
    print(len(f1[PG]))
    n = 0
    while(len(f1[PG]) > n):
        print(f1[PG][n])
        n += 1
    
    PG += 1






print(f1)