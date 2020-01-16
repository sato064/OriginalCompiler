#Reading source code
path1 = "samplesource.txt"
file1 = open(path1,'r',encoding='utf-8')
f1 = file1.readlines()
file1.close()


fileobj = open("Source.C", "w")



#Print_SourceCode
print(f1)



#Analysis
P_Len = len(f1)
print(P_Len)
PG = 0
n = 0


while(PG < P_Len):
    print(f1[PG])
    n = 0
    if(f1[PG] == "START\n"):
        print("START:RETURN 10000")
        fileobj.write("#include <stdio.h>\nvoid main void(){\n")

    if(f1[PG] == "END\n"):
        print("END:RETURN 10001")
        fileobj.write("\n}")
    
    #if(f1[PG] == )
    #print(len(f1[PG]))
    
    while(len(f1[PG]) > n):

        if(f1[PG][n] == "i"):
            if(f1[PG][n+1] == "f"):
                print("IF:RETURN 30")
        
        if(f1[PG][n] == "w"):
            if(f1[PG][n+1] == "h"):
                if(f1[PG][n+2] == "i"):
                    if(f1[PG][n+3] == "l"):
                        if(f1[PG][n+4] == "e"):
                            print("WHILE:RETURN 31")

        if(f1[PG][n] == "g"):
            if(f1[PG][n+1] == "e"):
                if(f1[PG][n+2] == "t"):
                    print("GET:RETURN 10")
        
        if(f1[PG][n] == "p"):
            if(f1[PG][n+1] == "r"):
                if(f1[PG][n+2] == "i"):
                    if(f1[PG][n+3] == "n"):
                        if(f1[PG][n+4] == "t"):
                            print("PRINT:RETURN 11")
        
        if(f1[PG][n] == "d"):
            if(f1[PG][n+1] == "e"):
                if(f1[PG][n+2] == "f"):
                    print("DEF 10")
                    fileobj.write("int " + f1[PG][n+5] + f1[PG][n+6]+ f1[PG][n+7] + f1[PG][n+8])


        
        
        if(f1[PG][n] == "$"):
            print("ID:RETURN 1000")
            #fileobj.write("int " + f1[PG][n+1])

        
        if(f1[PG][n] == "+"):
            print("+:RETURN 100")

        if(f1[PG][n] == "-"):
            print("-:RETURN 101")

        if(f1[PG][n] == "*"):
            print("*:RETURN 102")

        if(f1[PG][n] == "/"):
            print("/:RETURN 103")

        if(f1[PG][n] == "%"):
            print("%:RETURN 104")
                            
        if(f1[PG][n] == "=" and f1[PG][n-1] != "="):
            if(f1[PG][n+1] == "="):
                print("==:RETURN 110")
            else:
                print("=:RETURN 105")

        if(f1[PG][n] == "<"):
            print("<:RETURN 111")
        
        if(f1[PG][n] == ">"):
            print(">:RETURN 112")
        
        if(f1[PG][n] == "="):
            if(f1[PG][n+1] == "<"):
                print("IF:RETURN 113")

        if(f1[PG][n] == "="):
            if(f1[PG][n+1] == ">"):
                print("IF:RETURN 114")

        if(f1[PG][n] == "("):
            print("(:RETURN 40")
        
        if(f1[PG][n] == ")"):
            print("):RETURN 42")
        
        if(f1[PG][n] == "{"):
            print("{:RETURN 41")
        
        if(f1[PG][n] == "}"):
            print("}:RETURN 43")
        

        
        n += 1
    
    PG += 1

fileobj.close



