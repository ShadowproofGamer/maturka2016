import math
plik = open("punkty.txt")
odczyt = plik.read().split()
kolo_dla_1000 = 0
kolo_dla_5000 = 0
kolo_dla_wszystkich = 0
indeks = 0
wspolrzedne = []
for i in odczyt[::2]:
    war = (int(i)-200)**2 + (int(odczyt[indeks+1])-200)**2
    if war < 200**2 and indeks <2000:
        kolo_dla_1000+=1
        kolo_dla_5000 += 1
        kolo_dla_wszystkich += 1
    elif war < 200**2 and indeks <10000:
        kolo_dla_5000 += 1
        kolo_dla_wszystkich += 1

    elif war < 200**2:
        kolo_dla_wszystkich += 1
    elif war == 200**2:
        wspolrzedne.append([int(i), int(odczyt[indeks + 1])])
    indeks+=2

print(wspolrzedne)
print(kolo_dla_wszystkich)
print("pi dla 1000 punktow: ", (kolo_dla_1000/1000)*4)
print("pi dla 5000 punktow: ", (kolo_dla_5000/5000)*4)
print("pi dla wszystkich punktow: ", (kolo_dla_wszystkich/10000)*4)


def pii(n):
    kolo = 0
    indeks = 0
    for i in odczyt[:n*2:2]:
        war = (int(i) - 200) ** 2 + (int(odczyt[indeks + 1]) - 200) ** 2
        if war < 200 ** 2:
            kolo += 1
        indeks += 2
    return (kolo/n)*4

blad_tab = []


def blad(n):
    return abs(round((math.pi-pii(n))*10000))/10000


for j in range(1,1700):
    ess = blad(j)
#    print(ess)
    blad_tab.append(ess)
#print(blad_tab[1000:1700:])
print(blad(1000))
print(blad(1700))
