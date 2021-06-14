def unique(list1):
    unique_list = []

    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list
def stat(id,k,stan):
    tab = []
    with open("games.txt") as file_in:
        lines = []
        for line in file_in:
            lines.append(line.rstrip('\n'))
    for i in range(len(lines)):
        if(lines[i]==id):
            if (lines[i + 1] == k):
                a = 0
                b = i+3
                while(len(stan) > a and stan[a]==lines[b]):
                    if (a == len(stan)-1):
                        tab.append(lines[b + 1])
                        tab.append(lines[i + 2])

                    a = a + 1
                    b = b + 1
    return tab
def wyszukaj(imie,nazwisko):
    plik = open('players.txt', 'r+').readlines()
    L = []
    H = []
    x = 0
    for linia in plik:
        if x % 2 == 0:
            L.append(linia.rstrip())
        else:
            H.append(linia.rstrip())
        x = x + 1
    if imie in L:
        for i in range(len(L)):
            if (L[i] == imie and H[i] == nazwisko):
                return int(x/2)
    else:
        print("Taki zawodnik nie istnieje")
        return
o=0
#im=input('imie')
#na=input('nazwisko')
#indeks=wyszukaj(im,na)
#po podpięciu bazy danych z graczami przed partią wyszukiwanie przeciwnika
indeks=1
k=input('podaj kolor, 0=biały -1=czarny')
tablica=[]
while(o!=1):
    staty = []
    winrate = []
    move = []
    times = []
    wins = []
    k2=k
    int(o)
    if(o!=1):

        if(k2==-1):
            s = input('podaj ruch')
            str(s)
            tablica.append(s)
            staty = stat(str(indeks), str(k), tablica)
            for x in range(len(staty)):
                if x % 2 == 0:
                    move.append(staty[x])
                else:
                    winrate.append(staty[x])
            uni = unique(move)
            for x in range(len(uni)):
                times.append(move.count(uni[x]))

            for x in range(len(uni)):
                wins.append(0)

            for x in range(len(staty)):
                if x % 2 != 0:
                    if (staty[x] == 'w'):
                        wins[uni.index(staty[x - 1])] += 1
            print('ruchy')
            print(uni)
            print('liczba gier')
            print(times)
            print('liczba zwycięstw')
            print(wins)
            k2 = 0
        else:
            s = input('podaj ruch przeciwnika')
            str(s)
            tablica.append(s)
            s = input('podaj ruch')
            str(s)
            tablica.append(s)

            staty = stat(str(indeks), str(k), tablica)
            for x in range(len(staty)):
                if x % 2 == 0:
                    move.append(staty[x])
                else:
                    winrate.append(staty[x])
            uni = unique(move)
            for x in range(len(uni)):
                times.append(move.count(uni[x]))
            for x in range(len(uni)):
                wins.append(0)
            for x in range(len(staty)):
                if x % 2 != 0:
                    if (staty[x] == 'w'):
                        wins[uni.index(staty[x - 1])] += 1
            print('ruchy')
            print(uni)
            print('liczba gier')
            print(times)
            print('liczba zwycięstw')
            print(wins)
