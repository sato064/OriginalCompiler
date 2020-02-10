# Reading source code
path1 = "samplesource4.txt"
file1 = open(path1, 'r', encoding='utf-8')
f1 = file1.readlines()
file1.close()


fileobj = open("Source.C", "w")


# print_SourceCode
# print(f1)


# Analysis
P_Len = len(f1)
# print(P_Len)
PG = 0
n = 0
PG_e = 0


pflg = False
sflg = False

fflg = True

e_flg = False
pe_flg = False
ge_flg = False
de_flg = False
ee_flg = False
cr_flg = False

str_flg = True
end_flg = True


while(PG < P_Len):
    n = 0
    isCoron = True
    isisCoron = False
    if(f1[0] == "START\n" and str_flg == True):
        # print("START:RETURN 10000")
        fileobj.write("#include <stdio.h>\nint main(){\n")
        str_flg = False

    if (f1[PG] == "END\n" and end_flg == True):
        if(PG == P_Len - 1):
            # print("END:RETURN 10001")
            fileobj.write("\nreturn 0;\n}")
            end_flg = False
        else:
            print("ERROR_ENDがソースコードの途中に含まれています")
            ee_flg = True
    # if(f1[PG] == )
    # print(len(f1[PG]))

    while(len(f1[PG]) > n):

        if(f1[PG][n] == "i"):
            if(f1[PG][n+1] == "f"):
                # print("IF:RETURN 30")
                fileobj.write("if")

        if(f1[PG][n] == "e"):
            if (f1[PG][n + 1] == "l"):
                if(f1[PG][n+2] == "s"):
                    if(f1[PG][n+3] == "e"):
                        # print("IF:RETURN 30")
                        fileobj.write("else ")

        if(f1[PG][n] == "w"):
            if(f1[PG][n+1] == "h"):
                if(f1[PG][n+2] == "i"):
                    if(f1[PG][n+3] == "l"):
                        if(f1[PG][n+4] == "e"):
                            # print("WHILE:RETURN 31")
                            fileobj.write("while")

        if(f1[PG][n] == "g"):
            if(f1[PG][n+1] == "e"):
                if(f1[PG][n+2] == "t"):
                    # print("GET:RETURN 10")
                    fileobj.write('scanf("%d",&')
                    pflg = True
                    isisCoron = True
                    if (f1[PG][n + 4] != "$"):
                        ge_flg = True
                        e_flg = True

        if(f1[PG][n] == "p"):
            if(f1[PG][n+1] == "r"):
                if(f1[PG][n+2] == "i"):
                    if(f1[PG][n+3] == "n"):
                        if (f1[PG][n + 4] == "t"):
                            if(f1[PG][n + 6] == "$"):
                                # print("#print:RETURN 11")
                                fileobj.write('printf("%d",')
                                pflg = True
                                pflg = True
                                if (f1[PG][n + 6] != "$"):
                                    pe_flg = True
                                    e_flg = True
                            else:
                                fileobj.write('printf')

        if(f1[PG][n] == "d"):
            if(f1[PG][n+1] == "e"):
                if(f1[PG][n+2] == "f"):
                    # print("DEF 10")
                    pflg = True
                    fileobj.write("int ")
                    if (f1[PG][n + 4] != "$"):
                        de_flg = True
                        e_flg = True
                    # i = 4
                    # while(f1[PG][n+i] != "$"):
                    # fileobj.write(f1[PG][n+i])

        if(f1[PG][n] == "$"):
            # print("ID:RETURN 1000")
            if(pflg):
                i = 1
                while(f1[PG][n+i] != "~"):
                    fileobj.write(f1[PG][n+i])
                    i += 1

                fileobj.write(")")
                n += i
                slfg = False
                pflg = False

            else:
                i = 1
                while(f1[PG][n+i] != "~"):
                    # print("-------------" + f1[PG][n+i])
                    fileobj.write(f1[PG][n+i])
                    i += 1
                n += i

        if (f1[PG][n] == "_"):
            fileobj.write('"')
            i = 1
            while (f1[PG][n + i] != "_" and f1[PG][n + i] != ")"):
                #print(f1[PG][n + i])
                fileobj.write(f1[PG][n + i])

                # print(f1[PG][n+i])

                i += 1

        if(f1[PG][n] == "+"):
            # print("+:RETURN 100"
            fileobj.write("+")

        if(f1[PG][n] == "-"):
            # print("-:RETURN 101")
            fileobj.write("-")

        if(f1[PG][n] == "*"):
            # print("*:RETURN 102")
            fileobj.write("*")

        if(f1[PG][n] == "/"):
            # print("/:RETURN 103")
            fileobj.write("/")

        if(f1[PG][n] == "%"):
            # print("%:RETURN 104")
            fileobj.write("%")

        if(f1[PG][n] == "=" and f1[PG][n-1] != "="):
            if(f1[PG][n+1] == "="):
                # print("==:RETURN 110")
                fileobj.write("==")
            else:
                # print("=:RETURN 105")
                fileobj.write("=")

        if(f1[PG][n] == "<"):
            # print("<:RETURN 111")
            fileobj.write("<")

        if(f1[PG][n] == ">"):
            # print(">:RETURN 112")
            fileobj.write(">")

        if(f1[PG][n] == "!"):
            # print(">:RETURN 115")
            fileobj.write("!")

        if(f1[PG][n] == "="):
            if(f1[PG][n+1] == "<"):
                # print("IF:RETURN 113")
                fileobj.write("=<")

        if(f1[PG][n] == "="):
            if(f1[PG][n+1] == ">"):
                # print("IF:RETURN 114")
                fileobj.write("=>")

        if(f1[PG][n] == "("):
            # print("(:RETURN 40")
            fileobj.write("(")

        if(f1[PG][n] == ")"):
            # print("):RETURN 42")
            fileobj.write(")")

        if(f1[PG][n] == "{"):
            # print("{:RETURN 41")
            fileobj.write("{")

        if(f1[PG][n] == "}"):
            # print("}:RETURN 43")
            fileobj.write("}")

        if(f1[PG][n] == "&"):
            # print("}:RETURN 43")
            fileobj.write("&")

        if(f1[PG][n] == "|"):
            # print("}:RETURN 43")
            fileobj.write("|")

        if(f1[PG][n] == "1"):
            # print("}:RETURN 43")
            fileobj.write("1")

        if(f1[PG][n] == "2"):
            # print("}:RETURN 43")
            fileobj.write("2")

        if(f1[PG][n] == "3"):
            # print("}:RETURN 43")
            fileobj.write("3")

        if(f1[PG][n] == "4"):
            # print("}:RETURN 43")
            fileobj.write("4")

        if(f1[PG][n] == "5"):
            # print("}:RETURN 43")
            fileobj.write("5")

        if(f1[PG][n] == "6"):
            # print("}:RETURN 43")
            fileobj.write("6")

        if(f1[PG][n] == "7"):
            # print("}:RETURN 43")
            fileobj.write("7")

        if(f1[PG][n] == "8"):
            # print("}:RETURN 43")
            fileobj.write("8")

        if(f1[PG][n] == "9"):
            # print("}:RETURN 43")
            fileobj.write("9")

        if(f1[PG][n] == "0"):
            # print("}:RETURN 43")
            fileobj.write("0")

        if(f1[PG][n] == ";"):
            # print("}:RETURN 43")
            fileobj.write(";")
            isCoron = False

        n += 1

    PG += 1
    if(e_flg == False):
        PG_e += 1
    fileobj.write("\n")

    if (isCoron and isisCoron):
        cr_flg = True
        e_flg = True


if(str_flg):
    print("ERROR-STARTがありません(1)行目")
    fflg = False
if(end_flg):
    print("ERROR-ENDがありません(" + str(PG) + "行目)")
    fflg = False
if(ee_flg):
    fflg = False
if (pe_flg):
    print("ERROR_Printの引数が無いか，変数の前に＄がありません(" + str(PG_e+1) + "行目)")
    fflg = False
if (ge_flg):
    print("ERROR_Getの引数が無いか，変数の前に＄がありません(" + str(PG_e+1) + "行目)")
    fflg = False
if (de_flg):
    print("ERROR_Defの引数が無いか，変数の前に＄がありません(" + str(PG_e+1) + "行目)")
    fflg = False
if (cr_flg):
    print("文末に;が無い行があります")
    fflg = False

if(fflg):
    print("Compile finished")


fileobj.close
