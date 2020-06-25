a = []

with open("c:\\score\\score.txt","r") as f:
    for i in range(20):
        a.append(f.readline().split())

for i in range(20):
    a[i][2] = int(a[i][2])
    a[i][3] = int(a[i][3])
    a[i][4] = int(a[i][4])

    a[i].append(a[i][2] + a[i][3] + a[i][4]) #총점
    a[i].append(a[i][5] / 3) #평균

kor = 0; eng = 0; mat = 0;

for i in range(20):
    kor = kor + a[i][2] # 국어총점
    eng = eng + a[i][3] # 영어총점
    mat = mat + a[i][4] # 수학총점


#파일출력
with open("c:\\score\\report.txt","w") as f2:

    print("               *  성 적 표  *", file = f2)
    print("=============================", file = f2)
    print(" 번호  이름  국어  영어  수학  총점  평균 ", file = f2)
    print("=============================", file = f2)

    for i in range(20):
        print("  {}   {}   {}    {}    {}   {}   {:.1f} ".format(a[i][0],a[i][1],a[i][2],a[i][3],a[i][4],a[i][5],a[i][6]) , file = f2)

    print("==============================", file = f2)

    print("평균 :            {:.1f} {:.1f} {:.1f}         {:.1f}".format(kor/20, eng/20, mat/20, (kor+eng+mat)/30), file = f2)