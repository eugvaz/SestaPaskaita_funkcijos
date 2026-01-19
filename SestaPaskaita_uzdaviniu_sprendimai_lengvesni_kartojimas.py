import random

from SestaPaskaita_uzdaviniu_sprendimas import rnd_masyvas

print("_______________________1.________________________________")
# 1. Sukurkite Funkciją kuri priima du kintamuosius, skaičius. Juos susumuoja ir atspausdina.

def susumavimas(a,b):
    print(a+b)
susumavimas(4,5)

print("_______________________2.________________________________")
# 2. Sukurkite Funkciją kuri vadinasi PISq. Funkcija gražina reikšmę. Reikšmė yra : 9.8596; Gautą reikšmę atspausdinkite.

def PISq():
    return 9.8596

print(PISq())
print("_________")
def PISq():
    return 9.8596
print("_________")
x = PISq()
print(x)

print("_______________________3.________________________________")
# 3. Sukurkite Funkciją kuri priima du kintamuosius. Funkcija gražina skaičių sandaugą.; Gautą reikšmę atspausdinkite.

def sandauga(a,b):
    return a*b

print(sandauga(4,5))

print("_________")

y = sandauga(3,4)
print(y)

# 4. Sukurkite Funkciją kuri priima masyvą, prasuka ciklą ir atspausdina kiekvieną narį vienoje eilutėje.
print("_______________________4.________________________________")

masyvas= [1,2,3,3,3,3,5]
def atspausdink(masyvas):
    for sk in masyvas:
        print(sk)

atspausdink(masyvas)
print("_________")
def atspausdink(masyvas):
    for sk in masyvas:
        print(sk, end=" ")
print()
atspausdink([2,3,4,5,6])
print("_________")
def atspausdink(masyvas):
    for sk in masyvas:
        print(sk)
print()
atspausdink([2,3,4,5,6,7,8,9])
print("_________")
def atspausdink(masyvas):
    for i in range(len(masyvas)):
        print(masyvas[i])
print()
atspausdink([2,3,4,5,6,7,8,9])

print("_________")
atspausdink([2,3,4,5,6,7,8,9])
print("_________")
def atspausdink(masyvas):
    for i, sk in enumerate(masyvas):
        print(i,sk)
print()
atspausdink([0,0,2,3,4,5,6,7,8,9])
print("_________")
def atspausdink(masyvas):
    for i, sk in enumerate(masyvas):
        print(i,sk)
print()
atspausdink(['a','b','c','d','e'])

# 5. Sukurkite Funkciją kuri sugeneruotų random skaičių masyvą ir jį gražintų. Funkcija priima tris kintamuosius,
# min, max ir length reikšmėms nustatyti.
print("_______________________5.________________________________")

def sugeneruok_ir_grazink(min,max,length):
    return [random.randint (min, max) for _ in range(length)]
rnd_masyvas= sugeneruok_ir_grazink(2,5,5)
print(rnd_masyvas)

# 6. Sukurkite Funkciją kuri panaudotų 5toje užduotyje sugeneruotą masyvą (priimtų kaip kintamąjį), susumuotų ir gražintų reikšmę.
print("_______________________6.________________________________")

def susumuok_masyvo_reiksmes(rnd_masyvas):
    return sum(rnd_masyvas)

rnd_masyvas= sugeneruok_ir_grazink(3,5,6)
print(rnd_masyvas)

print(susumuok_masyvo_reiksmes(rnd_masyvas))

# 7. Sukurkite Funkciją kuri priimtų 5toje užduotyje sugeneruotą masyvą ir gražintų jos skaičių vidurkį.
print("_______________________7.________________________________")

def apskaiciuok_masyvo_skaiciu_vidurki(rnd_masyvas):
    if len(rnd_masyvas) == 0:
        return 0
    return (sum(rnd_masyvas)/len(rnd_masyvas))

rnd_masyvas= sugeneruok_ir_grazink(0,0,5)
print(rnd_masyvas)

print(apskaiciuok_masyvo_skaiciu_vidurki(rnd_masyvas))

# 8. Sukurkite Funkciją kuri priimtų du skaičius ir atspausdintų stačiakampį užpildytą žvaigždutėmis.
# Pirmas skaičius- išoriniam ciklui, antras vidiniam.
print("_______________________8.________________________________")

def atspausdink_staciakampi(a,b): # a eiluciu skaicius- isorinis ciklas
    for i in range(a):
        for y in range(b): # b stulpeliu skaicius- vidinis ciklas
            print(' * ', end= '')
        print()
atspausdink_staciakampi(5,4)
print("_________")
def staciakampis(a,b):
    for i in range(a):
        string = '' #cikle sukuriame tuscia String, kuriame klijuosime *
        for j in range(b):
            string += ' * '
        print(string)

staciakampis(2,3)
# 9. Sukurkite Funkciją kuri priimtų sakinį kaip kintamąjį ir atspausdintų kiek jame yra raidžių(simbolių) ir tarpų.
# Sakinys - “Šiandien labai graži diena”. (kodas turi veikti padavus bet kokį sakinį) (simboliu yra 23, tarpu yra 3)
print("_______________________9.________________________________")

def atspausdink_raides_ir_tarpus(tekstas):
    tarpai= tekstas.count(" ")
    raides= len(tekstas)-tarpai
    print('Raidziu:',raides, 'tarpu:',tarpai)
atspausdink_raides_ir_tarpus('Šiandien labai graži diena')
atspausdink_raides_ir_tarpus('Gyvenimas yra grazus')
print("_________")

def atspausdink_raides_ir_tarpus(tekstas):
    tarpai= tekstas.count(" ")
    raides= 0 #sukuriama raidziu skaitiklis
    for s in tekstas: #ciklas kur eina per kiekviena simboli tekste
        if s.isalpha(): # jei randa raide, tai ja sumuoja
         raides += 1
    print('Raidziu:',raides, 'tarpu:',tarpai)

atspausdink_raides_ir_tarpus('Vienas juokas!')
atspausdink_raides_ir_tarpus('Gyvenimas yra grazus...')

print("_______________________10.________________________________")
# 10.Sukurkite Funkciją kuri priimtų sakinį, jį užkoduotų ir grąžintų.
# Kodavimas - sakinį apsukame iš kitos pusės. Pvz “Naglis” turi gautis “silgaN”.

def uzkoduok_ir_grazink(tekstas):
    tekstas[::-1]
    return tekstas[::-1]

print(uzkoduok_ir_grazink('Eugenija'))
print(uzkoduok_ir_grazink('Gyvenimas yra grazus'))
print("_________")
def uzkoduok_ir_grazink(tekstas):
    uzkoduotas = tekstas[::-1]
    return uzkoduotas

print(uzkoduok_ir_grazink('Juokas'))
print(uzkoduok_ir_grazink('Gyvenimas yra'))

print("_______________________11.________________________________")
# 11.Sukurti funkciją, kuri apsuka tik žodžius. “Labas rytas” -> “sabaL satyr” ir atspausdina rezultatą

def atspausdink_apsuktus_zodzius(tekstas):
    rezultatas = "" #tuscias stringas
    for zodis in tekstas.split(): #sukam cikla su kiekvienu zodziu is sukarpyto teksto
        rezultatas += zodis[::-1]+" " # kiekviena zodi pasukame ir su tarpu suklijuojame i stringa
    print(rezultatas)
atspausdink_apsuktus_zodzius("Labas rytas")
atspausdink_apsuktus_zodzius("Juokas pro asaras")
print("_________")
def atspausdink_apsuktus_zodzius(tekstas):
    rezultatas = "" #tuscias stringas
    for zodis in tekstas.split(): #sukam cikla su kiekvienu zodziu is sukarpyto teksto
        rezultatas += zodis[::-1]+" " # kiekviena zodi pasukame ir su tarpu suklijuojame i stringa
    print(rezultatas.strip()) ## nuima nereikalingus tarpus is abieju zodzio pusiu

atspausdink_apsuktus_zodzius("Labas vakaras")
atspausdink_apsuktus_zodzius("Neviskas taip blogai")
print("_________")
def atspausdink_apsuktus_zodzius(tekstas):
    for zodis in tekstas.split():
        print(zodis[::-1], end=" ")
    print()
atspausdink_apsuktus_zodzius("jau spausdinu")

# 12.Sukurkite funkciją, kuri priimtų masyvą ir atspausdintų tik tuos elementus kurie yra skaičiai.
print("_______________________12.________________________________")

def atspausdink_tik_skaicius(masyvas):
    for elementas in masyvas:
        if isinstance(elementas,(int, float)) and not isinstance(elementas, bool): #instance tikrina ar elementas yra nurodyto tipo
            print(elementas)

atspausdink_tik_skaicius(['a',1,2,True,0,False])
print("_________")
def atspausdink_tik_skaicius(masyvas):
    for elementas in masyvas:
        if isinstance(elementas,(int, float)) and not isinstance(elementas, bool): #instance tikrina ar elementas yra nurodyto tipo
           print(elementas, end= ' ')
    print()
atspausdink_tik_skaicius(['a',1,2,True,0,False])

print("_________")
def atspausdink_tik_skaicius(masyvas):
    for elementas in masyvas:
        if type(elementas) in (int, float): # tikrina ar elementas yra nurodyto tipo
            print(elementas, end= ' ')
    print()
atspausdink_tik_skaicius(['a',1,2,True,0,False,3,4])

# 13.Sukurkite funkciją, kuri priima masyvą ir atspausdina tik sveikuosius skaičius.
# (jei pavyks, patobulinkite, kad funkcija priimtų antrą parametrą True/False kuris nuspręstų
# ar spausdins tik sveikuosius skaičius ar skaičius su kableliu.
print("_______________________13.________________________________")

def atspausdink_tik_sveikus_skaicius(masyvas):
    for elementas in masyvas:
        if type(elementas) == int:
            print(elementas) #atspausdina stulpeliu
    print()
atspausdink_tik_sveikus_skaicius([2,3,7,False,'a',True,1,5])

print("_________")
def atspausdink_tik_sveikus_skaicius(masyvas):
    for elementas in masyvas:
        if type(elementas) == int:
            print(elementas, end=' ') #atspausdina eilute
    print()
atspausdink_tik_sveikus_skaicius([2,3,7,False,'a',True,1,5])

print("_________")

def atspausdink_tik_sveikus_skaicius_pagal_pasirinkima(masyvas,tik_sveiki):
    for elementas in masyvas:
        if tik_sveiki == True:
            if type(elementas) == int:
                print(elementas, end=' ')
        else:
            if type(elementas) == float:
                print(elementas, end=' ')
    print()

atspausdink_tik_sveikus_skaicius_pagal_pasirinkima([1,2,3,1.2,5.6,True,"tu",8,9.1], tik_sveiki= True)
print("_________")
def atspausdink_tik_sveikus_skaicius_pagal_pasirinkima(masyvas,tik_sveiki):
    for elementas in masyvas:
        if tik_sveiki:
            if type(elementas) == int:
                print(elementas, end=' ')
        else:
            if type(elementas) == float:
                print(elementas, end=' ')
    print()

atspausdink_tik_sveikus_skaicius_pagal_pasirinkima([1,2,3,1.2,5.6,True,"tu",8,9.1], tik_sveiki= False)
print("_________")
def atspausdink_tik_sveikus_skaicius_pagal_pasirinkima(masyvas,tik_sveiki):
    for elementas in masyvas:
        if tik_sveiki:
            if type(elementas) == int:
                print(elementas, end=' ')
        else:
            if type(elementas) == float:
                print(elementas, end=' ')
    print()
atspausdink_tik_sveikus_skaicius_pagal_pasirinkima([1,2,3,1.2,5.6,True,"tu",8,9.1], tik_sveiki= False)

print("_________")
def atspausdink_tik_sveikus_skaicius_pagal_pasirinkima(masyvas,tik_sveiki):
    for elementas in masyvas:
        if tik_sveiki:
            if isinstance(elementas, int) and not isinstance(elementas, bool):
                print(elementas, end=' ')
        else:
            if isinstance(elementas, float) and not isinstance(elementas, bool):
                print(elementas, end=' ')
    print()
atspausdink_tik_sveikus_skaicius_pagal_pasirinkima([1.5,2,3,1.2,5.6,True,"tu",8,9.1], tik_sveiki= True)

# 14.Sukurkite funkciją word_count kuri priimtų textą ir gražintų kiek jame yra žodžių.
print("_______________________14.________________________________")

def grazink_kiek_zodziu_tekste(tekstas):
    return len(tekstas.split()) # isdalina teksta pagal tarpus ir grazina kiek zodziu tekste
kiek_zodziu = grazink_kiek_zodziu_tekste('Juokas pro visu asaras')
print(kiek_zodziu)
print("_________")
def word_count(tekstas):
    return len(tekstas.split())
kiek_zodziu = grazink_kiek_zodziu_tekste("Ar tikrai tai tiesa?")
print(kiek_zodziu)

# 15.Sukurkite funkciją kuri priima du parametrus. Skaičių masyvą ir boolean.
# Funkcija gražina prafiltruotą masyvą. Kai antras parametras True/tik poriniais skaičiais,
# False/tik neporiniais skaičiais.
print("_______________________15.________________________________")

def grazink_prafiltruota_masyva(masyvas, tik_poriniai):
    rezultatas = [] # sukuriamas tuscias masyvas rezultatams klijuoti
    for sk in masyvas:
        if tik_poriniai == True:
            if sk % 2 == 0:
                rezultatas.append(sk)
        else:
            if sk % 2 != 0:
                rezultatas.append(sk)
    return rezultatas
print()
# masyvas = [random.randint(1,5) for _ in range(5)]
# print(masyvas)
rezultatas = grazink_prafiltruota_masyva([random.randint(1,5) for _ in range(7)], tik_poriniai= False)
print(rezultatas)

# 16.Sukurkite funkciją number_is_prime. Funkcija priima skaičių, gražina True/False ar skaičius pirminis.
print("_______________________16.________________________________")

def numer_is_prime(n):
     if n<=1:
       return False
     for i in range(2,n):
         if n % i == 0:
             return False
     return True
print(numer_is_prime(1))
print(numer_is_prime(5))
print(numer_is_prime(7))
print(numer_is_prime(12))

# 17.Sukurkite funkciją kuri priima du argumentus. Gražina pirmąjį skaičių pakeltą laipsniu tokiu kaip antras skaičius.
print("_______________________17.________________________________")

def grazink_pakelta_laipsniu(a,b):
    return pow(a,b)
print(grazink_pakelta_laipsniu(2,0))
print(grazink_pakelta_laipsniu(5,3))
print("_________")

def grazink_pakelta_laipsniu(a,b):
    return a**b
print(grazink_pakelta_laipsniu(8,9))

# 18.Sukurkite funkciją kuri priima skaičių masyvą ir gražina tik skirtingus elementus.
# (panašiai kaip sql distinct)
print("_______________________18.________________________________")

def grazink_skirtingus_elementus(masyvas):
    rezultatas =[]
    for sk in masyvas:
        if sk not in rezultatas:
            rezultatas.append(sk)
    return rezultatas

print(grazink_skirtingus_elementus([random.randint(1,5) for _ in range(7)]))
