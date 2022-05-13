#Funkcja generujaca wejsciowy ciag

def generujciag(m,n):
    ciag=""
    for i in range(0,m,1):
        ciag+='0'
    ciag+='1'
    for j in range(0,n,1):
        ciag+='0'
    return ciag

#Funkcja, ktora oblicza roznice wlasciwa matematycznie
def roznicawlasciwa(m,n):
    if(m>=n):
        return m-n
    else:
        return 0

#Funkcja, ktora wypisuje informacje o maszynie Turinga

def informacje():
    print("Emualtor maszyny Turinga obliczajacy roznice wlasciowa\n")
    print("Definicja roznicy wlasciwej:")
    print("     | m-n dla m >= n")
    print(" m-n=|")
    print("     | 0 dla m < n\n")
    print("Postac maszyny Turinga:")
    print(" M=({q0, q1, q2, q3, q4, q5, q6}, {0,1}, {0,1,B}, d, q0, B, 0) \n")
    print("Tablica przejsc maszyny Turinga:")
    print("  -----------------------------------------------")
    print("  |  d   |      0     |      1     |      B     |")
    print("  -----------------------------------------------")
    print("  -----------------------------------------------")
    print("  |  q0  |  (q1,B,P)  |  (q5,B,P)  |      -     |")
    print("  -----------------------------------------------")
    print("  -----------------------------------------------")
    print("  |  q1  |  (q1,0,P)  |  (q2,1,P)  |      -     |")
    print("  -----------------------------------------------")
    print("  -----------------------------------------------")
    print("  |  q2  |  (q3,1,L)  |  (q2,1,P)  |  (q4,B,L)  |")
    print("  -----------------------------------------------")
    print("  -----------------------------------------------")
    print("  |  q3  |  (q3,0,L)  |  (q3,1,L)  |  (q0,B,P)  |")
    print("  -----------------------------------------------")
    print("  -----------------------------------------------")
    print("  |  q4  |  (q4,0,L)  |  (q4,B,L)  |  (q6,0,P)  |")
    print("  -----------------------------------------------")
    print("  -----------------------------------------------")
    print("  |  q5  |  (q5,B,P)  |  (q5,B,P)  |  (q6,B,P)  |")
    print("  -----------------------------------------------")
    print("  -----------------------------------------------")
    print("  |  q6  |      -     |      -     |      -     |")
    print("  -----------------------------------------------")

#Emulator dzialania maszyny Turinga
def przejscie(list,przejdz):
    pom1=list[2]
    pom2=list[3]
    if(pom1==0 and przejdz=='L'):
        list[0]='B'+list[0]
        return 0
    if(pom1==pom2 and przejdz=='P'):
        list[0]+='B'
        list[3]=pom2+1
        return pom2+1
    if(przejdz=='P'): 
        return pom1+1
    else:
        return pom1-1

def zamien(s, p, r): 
    return s[:p]+r+s[p+1:]

def piszopis(list):
    opis=""
    if(list[2]==0):
        return " "+"q"+str(list[1])+" "+list[0]
    for i in range(list[2]):
        opis+=list[0][i]
    opis+=(" "+"q"+str(list[1])+" ")
    for j in range(list[2],len(list[0]),1):
        if(list[0][j]!='B'):
            opis+=list[0][j]
        else:
            break
    return opis

def emulator(list):
    while(1):
        if(list[4]==1):
            print(' '+'|-'+' ',end='')
        print(piszopis(list),end='')
        list[4]=1
        if(list[1]==6):
            list[2]=-1
            break
        if(list[1]==0):
            if(list[0][list[2]]=='0'):
                list[1]=1
                list[0]=zamien(list[0],list[2],'B')
                list[2]=przejscie(list,'P')
            elif(list[0][list[2]]=='1'):
                list[1]=5
                list[0]=zamien(list[0],list[2],'B')
                list[2]=przejscie(list,'P')
        elif(list[1]==1):
            if(list[0][list[2]]=='0'):
                list[1]=1
                list[0]=zamien(list[0],list[2],'0')
                list[2]=przejscie(list,'P')
            elif(list[0][list[2]]=='1'):
                list[1]=2
                list[0]=zamien(list[0],list[2],'1')
                list[2]=przejscie(list,'P')
        elif(list[1]==2):
            if(list[0][list[2]]=='0'):
                list[1]=3
                list[0]=zamien(list[0],list[2],'1')
                list[2]=przejscie(list,'L')
            elif(list[0][list[2]]=='1'):
                list[1]=2
                list[0]=zamien(list[0],list[2],'1')
                list[2]=przejscie(list,'P')
            elif(list[0][list[2]]=='B'):
                list[1]=4
                list[0]=zamien(list[0],list[2],'B')
                list[2]=przejscie(list,'L')
        elif(list[1]==3):
            if(list[0][list[2]]=='0'):
                list[1]=3
                list[0]=zamien(list[0],list[2],'0')
                list[2]=przejscie(list,'L')
            elif(list[0][list[2]]=='1'):
                list[1]=3
                list[0]=zamien(list[0],list[2],'1')
                list[2]=przejscie(list,'L')
            elif(list[0][list[2]]=='B'):
                list[1]=0
                list[0]=zamien(list[0],list[2],'B')
                list[2]=przejscie(list,'P')
        elif(list[1]==4):
            if(list[0][list[2]]=='0'):
                list[1]=4
                list[0]=zamien(list[0],list[2],'0')
                list[2]=przejscie(list,'L')
            elif(list[0][list[2]]=='1'):
                list[1]=4
                list[0]=zamien(list[0],list[2],'B')
                list[2]=przejscie(list,'L')
            elif(list[0][list[2]]=='B'):
                list[1]=6
                list[0]=zamien(list[0],list[2],'0')
                list[2]=przejscie(list,'P')
        elif(list[1]==5):
            if(list[0][list[2]]=='0'):
                list[1]=5
                list[0]=zamien(list[0],list[2],'B')
                list[2]=przejscie(list,'P')
            elif(list[0][list[2]]=='1'):
                list[1]=5
                list[0]=zamien(list[0],list[2],'B')
                list[2]=przejscie(list,'P')
            elif(list[0][list[2]]=='B'):
                list[1]=6
                list[0]=zamien(list[0],list[2],'B')
                list[2]=przejscie(list,'P') 

def licznik(list):
    ans=0
    for i in range(len(list[0])):
        if(list[0][i]!='B'):
            ans+=1
    return ans

informacje()
pom=[]
wykonanie=1
m=int(input("Podaj liczbe m:"))

n=int(input("Podaj liczbe n:"))
if(m<0 or n<0):
    print("Prosze podac nieujemne liczby!")
    wykonanie=0

if(wykonanie==1):
    Turing=[generujciag(m,n),0,0,m+n,0]
    print()
    print("Wygenrowana tasma wejsciowa:"+generujciag(m,n)+'\n')
    print('Ciag opisow chwilowych:')
    ans=emulator(Turing)
    roznica=licznik(Turing)
    print('\n'+'---------------------------------------------'+'\n')
    print("Wynik roznicy wlasciwej wynosi:"+str(roznica)+"\n")
    if(roznicawlasciwa(m,n)==roznica):
        print("Obliczona wartosc jest zgodna z wartoscia roznicy wlasciwej dla liczb m="+str(m)+" i n="+str(n)+"\n")
    print("Wyjscie zostalo zaakceptowane")
else:
    print("Wyjscie nie zostalo zaakceptowane!")