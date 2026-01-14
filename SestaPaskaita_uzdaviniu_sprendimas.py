import random

print("_______________________1.________________________________")
# 1. Sukurkite Funkciją kuri priima du kintamuosius, skaičius. Juos susumuoja ir atspausdina.

def sumavimas(a,b): #
    print(a+b)
sumavimas(6,8)

print("_______________________2.________________________________")
# 2. Sukurkite Funkciją kuri vadinasi PISq. Funkcija gražina reikšmę. Reikšmė yra : 9.8596; Gautą reikšmę atspausdinkite.

def PISq():
    return 9.8596
kintamasis = PISq()
print(kintamasis)

print("_______________________3.________________________________")
# 3. Sukurkite Funkciją kuri priima du kintamuosius. Funkcija gražina skaičių sandaugą.; Gautą reikšmę atspausdinkite.
def sandauga(a,b): #
    return (a*b)
print(sandauga(5,3))
print(sandauga(1.5,2))

# 4. Sukurkite Funkciją kuri priima masyvą, prasuka ciklą ir atspausdina kiekvieną narį vienoje eilutėje.
print("_______________________4.________________________________")

masyvas = [1,2,3,4]

def rodyk(masyvas):
    for i, sk in enumerate(masyvas):
        print(i,sk)

rodyk(masyvas)
print("_______________________________________________________")
masyvas = [1,2,3,4]

def rodyk(masyvas):
    for i, sk in enumerate(masyvas):
        print(i,sk, end="")
        print()
rodyk(masyvas)

print("_______________________________________________________")

def rodyk(masyvas):
    for sk in masyvas:
        print(sk,end=" ")
    print()

masyvas = [1,2,3,4]
rodyk(masyvas)
print("_______________________________________________________")
masyvas = ['varle','gyvate','ziogas']
rodyk(masyvas)
print("_______________________________________________________")
masyvas = [random.randint(100,999) for _ in range(100)]
rodyk(masyvas)
# 5. Sukurkite Funkciją kuri sugeneruotų random skaičių masyvą ir jį gražintų. Funkcija priima tris kintamuosius,
# min, max ir length reikšmėms nustatyti.
print("_______________________5.________________________________")

def rodyk_masyva(min, max, length):
        return ([random.randint(min,max) for _ in range(length)])
masyvas = rodyk_masyva(0,15,10)
rnd_masyvas = rodyk_masyva(0,3,5) #masyvas 6 uzduociai atlikti
print(masyvas)
print(rnd_masyvas)


# 6. Sukurkite Funkciją kuri panaudotų 5toje užduotyje sugeneruotą masyvą (priimtų kaip kintamąjį), susumuotų ir gražintų reikšmę.
print("_______________________6.________________________________")
print(rnd_masyvas) #masyvas is 5 tos uzduoties
def Suma_masyvo(rnd_masyvas):
    return sum(rnd_masyvas)

print(Suma_masyvo(rnd_masyvas))

# 7. Sukurkite Funkciją kuri priimtų 5toje užduotyje sugeneruotą masyvą ir gražintų jos skaičių vidurkį.
print("_______________________7.________________________________")
rnd_masyvas = rodyk_masyva(1,3,5)
print(rnd_masyvas)

def Vidurkis_masyvo(rnd_masyvas):
    return sum(rnd_masyvas)/ len(rnd_masyvas)

print(Vidurkis_masyvo(rnd_masyvas))
print(round(Vidurkis_masyvo(rnd_masyvas),2))

# 8. Sukurkite Funkciją kuri priimtų du skaičius ir atspausdintų stačiakampį užpildytą žvaigždutėmis.
# Pirmas skaičius- išoriniam ciklui, antras vidiniam.
print("_______________________8.________________________________")

def staciakampis( a, b):
    for i in range(a): # prasuka eilutes
        for k in range(b): # prasuka stulpelius
            print("* ", end="")
        print()

staciakampis(3,4)
print("_______________________________________________________")

# def staciakampis( a, b):
#     String = ""  # pasiimame tuscia string
#     for i in range(a): # prasuka eilutes
#         for k in range(b): # prasuka stulpelius
#             String += "* "
#         String += "\n"
#
# staciakampis(3,4)
# print(String)

# 9. Sukurkite Funkciją kuri priimtų sakinį kaip kintamąjį ir atspausdintų kiek jame yra raidžių(simbolių) ir tarpų.
# Sakinys - “Šiandien labai graži diena”. (kodas turi veikti padavus bet kokį sakinį) (simboliu yra 23, tarpu yra 3)
print("_______________________9.________________________________")

tekst = "Šiandien labai graži diena"

def Text( tekst):
    print(len(tekst))
Text(tekst)
print("_______________________________________________________")
tekst = "Šiandien labai graži diena"
def Raides_ir_tarpai( tekst):
    tarpai = tekst.count(" ")
    raides = len(tekst) - tarpai
    return raides, tarpai

rezultatas = Raides_ir_tarpai(tekst)
print( "Raides:", rezultatas[0])
print( "Tarpai:", rezultatas[1])

print("_______________________________________________________")
tekst = "Geras oras"
def Raides_ir_tarpai( tekst):
    tarpai = tekst.count(" ")
    raides = len(tekst) - tarpai
    return raides, tarpai

rezultatas = Raides_ir_tarpai(tekst)
print( "Raides:", rezultatas[0])
print( "Tarpai:", rezultatas[1])
print("_______________________________________________________")
tekst = "Gyvenimas yra grazus"
def Raides_ir_tarpai( tekst):
    tarpai = tekst.count(" ")
    raides = len(tekst) - tarpai
    return raides, tarpai

rezultatas = Raides_ir_tarpai(tekst)
print( "Raides:", rezultatas[0])
print( "Tarpai:", rezultatas[1])
print("_______________________________________________________")

print("_______________________10.________________________________")
# 10.Sukurkite Funkciją kuri priimtų sakinį, jį užkoduotų ir grąžintų.
# Kodavimas - sakinį apsukame iš kitos pusės. Pvz “Naglis” turi gautis “silgaN”.

tekst = "Gyvenimas yra grazus"

def Uzkoduoti( tekst): #tekstas su kuriuo dirbama
    tekst[::-1] # apsukamas tekstas, pradedamas skaityti nuo pabaigos
    return tekst[::-1]
print(Uzkoduoti("Eugenija"))
print(Uzkoduoti("Vaznyte"))
print(Uzkoduoti("Gyvenimas yra grazus"))
print(Uzkoduoti("Šiandien labai graži diena"))

print("_______________________11.________________________________")
# 11.Sukurti funkciją, kuri apsuka tik žodžius. “Labas rytas” -> “sabaL satyr” ir atspausdina rezultatą

def Apsukti( tekst): #tekstas su kuriuo dirba funkcija
    rezultatas = ""
    for zodis in tekst.split(): # paleidziamas ciklas, kuris ima po zodi is padalinto teksto zodziu
        rezultatas += zodis[::-1]+" "# kaupiame informacija kol sukasi zodziu ciklas+ pridedame " "
    #print(rezultatas)
    print(rezultatas.strip())# nuima nereikalingus tarpus is abieju zodzio pusiu
Apsukti(" Gyvenimas grazus ")
print("_______________________________________________________")

def Apsukti( tekst): #tekstas su kuriuo dirba funkcija
    rezultatas = ""
    for zodis in tekst.split(): # paleidziamas ciklas, kuris ima po zodi is padalinto teksto zodziu
        rezultatas += zodis[::-1]+" "# kaupiame informacija kol sukasi zodziu ciklas+ pridedame " "
    print(rezultatas)
    #print(rezultatas.strip())# nuima nereikalingus tarpus is abieju zodzio pusiu
Apsukti(" Gyvenimas grazus ")
print("_______________________________________________________")

def Apsukti( tekst): #tekstas su kuriuo dirba funkcija
    rezultatas = ""
    for zodis in tekst.split(): # paleidziamas ciklas, kuris ima po zodi is padalinto teksto zodziu
        rezultatas += zodis[::-1]+" "# kaupiame informacija kol sukasi zodziu ciklas+ pridedame " "
    print(rezultatas)
    #print(rezultatas.strip())# nuima nereikalingus tarpus is abieju zodzio pusiu
Apsukti("Ko cia nori ?")


# 12.Sukurkite funkciją, kuri priimtų masyvą ir atspausdintų tik tuos elementus kurie yra skaičiai.
print("_______________________12.________________________________")

def Atspausdink_tik_skaicius( masyvas ):
    for elementas in masyvas:
        if isinstance(elementas,(int, float)) and not isinstance(elementas, bool): # tikrina salyga ar sveikas skaicius, ar su kableliu ir ar ne booleans(true/ false)
            print(elementas)

masyvas= [1,5,"tu",True,6,False]
Atspausdink_tik_skaicius( masyvas )
print("_______________________________________________________")
masyvas= [8.2,2,5,"you",True,6.5,False,"Gyvenimas"]
Atspausdink_tik_skaicius( masyvas )
print("_______________________________________________________")

def Atspausdink_tik_skaicius( masyvas ):
    for elementas in masyvas:
        if type(elementas) in (int, float): # tikrina salyga elemento tipo is masyvo: sveikas skaicius, ar su kableliu
            print( elementas, end=" ")
    print()
masyvas= [8.2,2,5,"you",True,6.5,False,"Gyvenimas",1,5,"tu",True,6,False]
Atspausdink_tik_skaicius(masyvas)

# 13.Sukurkite funkciją, kuri priima masyvą ir atspausdina tik sveikuosius skaičius.
# (jei pavyks, patobulinkite, kad funkcija priimtų antrą parametrą True/False kuris nuspręstų
# ar spausdins tik sveikuosius skaičius ar skaičius su kableliu.
print("_______________________13.________________________________")
def Atspausdink_tik_sveikus_skaicius(masyvas):
    for elementas in masyvas:
        if type(elementas) == int: # tikrina salyga elemento tipo is masyvo: ar jis sveikas skaicius
            print( elementas) #atspausdina stulpeliu
    print()
masyvas= [8.2,2,5,"you",True,6.5,False,"Gyvenimas",1,5,"tu",True,6,False]
Atspausdink_tik_sveikus_skaicius(masyvas)


print("_______________________________________________________")

def Atspausdink_tik_sveikus_skaicius(masyvas):
    for elementas in masyvas:
        if type(elementas) == int: # tikrina salyga elemento tipo is masyvo: ar jis sveikas skaicius
            print( elementas, end= " ") #atspausdina eilute
    print()
masyvas= [8.2,2,5,"you",True,6.5,False,"Gyvenimas",1,5,"tu",True,6,False]
Atspausdink_tik_sveikus_skaicius(masyvas)

print("_______________________________________________________")
def Atspausdink_skaicius_pagal_pasirinkima(masyvas, tik_sveiki):
    for elementas in masyvas:
        if tik_sveiki == True:
            if type(elementas) == int: # tikrina salyga elemento tipo is masyvo: ar jis sveikas skaicius
                print( elementas)
        else:
            if type(elementas) == float:
                print(elementas)
    print()
masyvas= [8.2,2,5,"you",True,6.5,False,"Gyvenimas",1,5,"tu",True,6,False]
Atspausdink_skaicius_pagal_pasirinkima(masyvas,tik_sveiki= True)

print("_______________________________________________________")
def Atspausdink_skaicius_pagal_pasirinkima(masyvas, tik_sveiki):
    tipas = int if tik_sveiki else float #( rasome true, jei sveiki ir false, jei su kableliu
    for elementas in masyvas:
        if type(elementas) == tipas: # tikrina salyga elemento tipo is masyvo: ar jis sveikas skaicius
                print( elementas)
    print()
masyvas= [2.8,2.5,5,"you",True,5.5,False,"Gyvenimas",3,5,"tu",True,6.2,False]
Atspausdink_skaicius_pagal_pasirinkima(masyvas,tik_sveiki=True)

# 14.Sukurkite funkciją word_count kuri priimtų textą ir gražintų kiek jame yra žodžių.
print("_______________________14.________________________________")

def Suskaiciuoti_zodzius( tekst ): #tekstas su kuriuo dirba funkcija
     return len(tekst.split()) # isdalina teksta pagal tarpus ir grazina kiek zodziu tekste
zodziai = Suskaiciuoti_zodzius("Grazus gyvenimas") # rezultatas
print(zodziai)

print("_______________________________________________________")
def word_count(tekst):  # tekstas su kuriuo dirba funkcija
    return len(tekst.split())  # isdalina teksta pagal tarpus ir grazina kiek zodziu tekste

zodziai = word_count("Šiandien labai graži diena")  # rezultatas
print(zodziai)

# 15.Sukurkite funkciją kuri priima du parametrus. Skaičių masyvą ir boolean.
# Funkcija gražina prafiltruotą masyvą. Kai antras parametras True/tik poriniais skaičiais,
# False/tik neporiniais skaičiais.
print("_______________________15.________________________________")
def Grazink_skaicius_poriniai_neporiniai(masyvas, tik_poriniai):
    rezultatas = [] # sukuriamas tuscias masyvas tinkamiems skaiciams
    for skaicius in masyvas:
        if tik_poriniai == True:
            if skaicius % 2 == 0: # tikrina salyga skaiciaus; ar jis porinis
                rezultatas.append(skaicius)
        else:
            if skaicius % 2 != 0: # tikrina salyga skaiciaus; ar jis neporinis
                rezultatas.append(skaicius)
    return rezultatas

masyvas = [random.randint(1,5) for _ in range(5)]
print(masyvas)
rezultatas = Grazink_skaicius_poriniai_neporiniai(masyvas, tik_poriniai= False)
print(rezultatas)

# 16.Sukurkite funkciją number_is_prime. Funkcija priima skaičių, gražina True/False ar skaičius pirminis.
print("_______________________16.________________________________")
# def Grazink_skaicius_pirminiai_nepirminiai(masyvas, tik_pirminiai):
#     rezultatas = [] # sukuriamas tuscias masyvas tinkamiems skaiciams
#     for skaicius in masyvas:
#         if tik_pirminiai == True:
#             if skaicius % skaicius == 1 and skaicius % 1 == skaicius and skaicius > 1: # tikrina salyga skaiciaus; ar jis pirminiais
#                 rezultatas.append(skaicius)
#         else:
#                 rezultatas.append(skaicius)
#     return rezultatas
#
# masyvas = [random.randint(7,11) for _ in range(5)]
# print(masyvas)
# rezultatas = Grazink_skaicius_pirminiai_nepirminiai(masyvas, tik_pirminiai= True)
# print(rezultatas)

def numer_is_prime(n):
    if n<=1: # patikrina ar ne 0 ir 1, nes jie nepirminiai
        return False # jei 0 ar 1, tai iskart grazina atsakyma
    for i in range( 2, n): # tikrina visus galimus daugiklius nuo 2 iki n-2
        if n % i == 0:
            return False
    return True
print(numer_is_prime(13))

# 17.Sukurkite funkciją kuri priima du argumentus. Gražina pirmąjį skaičių pakeltą laipsniu tokiu kaip antras skaičius.
print("_______________________17.________________________________")
def pakelti_laipsniu(a,b):
    return pow(a,b) #laipsnio kelimo funkcija
rezultatas = pakelti_laipsniu(10,15)
print(rezultatas)
print("_______________________________________________________")
def pakelti_laipsniu(a,b):
    return a**b # kelia laipsniu vietoj pow()
rezultatas = pakelti_laipsniu(4,1)
print(rezultatas)
print("_______________________________________________________")
# 18.Sukurkite funkciją kuri priima skaičių masyvą ir gražina tik skirtingus elementus.
# (panašiai kaip sql distinct)
print("_______________________18.________________________________")

def Grazina_unikalius_skaicius(masyvas):
    rezultatas = [] #sukuria tuscia masyva
    for skaicius in masyvas:  # suka cikla
        if skaicius not in rezultatas: # tikrina skaicius ar ju nera sukurtame masyve
            rezultatas.append(skaicius) # jeigu nera, tai prideda
    return rezultatas

masyvas = [random.randint(0,3) for _ in range(7)]
print(masyvas)
rezultatas = Grazina_unikalius_skaicius(masyvas)
print(rezultatas)
print("_______________________________________________________")

def Grazina_skirtingus_skaicius(masyvas):
    return list(set(masyvas)) # pasalina pasikartojancius skaicius is masyvo, grazina sarasa, bet neislaiko pradinio masyvo eiliskumo

masyvas = [random.randint(0,2) for _ in range(7)]
print(masyvas)
rezultatas = Grazina_skirtingus_skaicius(masyvas)
print(rezultatas)


# 19.Sukurkite funkciją kuri priima tekstą ir atspausdina tekste daugiausiai pasikartojantį simbolį.
print("_______________________19.________________________________")
def Atspausdinti_dazniausia_simboli( tekstas):
    skaicius = {} # sukuriamas tuscias zodynas simboliams skaiciuoti
    for simbolis in tekstas: # ciklas eina per kiekviena simboli tekste
        if simbolis in skaicius: # tikrina ar simbolis yra zodyne
            skaicius[simbolis]+= 1 # jeidu taip, tai prideda +1 prie jau esancio skaiciaus
        else:
            skaicius[simbolis] = 1 #jeigu ne, tai irasoma i zodyna ir pradeda skaiciuoti
    dazniausia = max( skaicius, key= skaicius.get) # skaicius- simboliu pasikartojimai, esantys zodyne,
    # key lygina pagal skaiciu reiksmes, iesko didziausios
    print(dazniausia,"-",skaicius[dazniausia]) # atspausdina raide ir jos pasikartojimu skaiciu

Atspausdinti_dazniausia_simboli("labai geras oras")
print("_______________________________________________________")
def Atspausdinti_dazniausius_simbolius( tekstas):
    #tekstas = tekstas.replace(" ","") #panaikiname is teksto tarpus
    didziausias = 0 # susikuriame skaitikli simboliu pasikartojimams skaiciuoti
    for simbolis in tekstas: # ciklas eina per kiekviena simboli tekste
        kiekis = tekstas.count(simbolis) # skaicius, kuris gaunamas
        if kiekis > didziausias: # tikrina salyga ar kiekis didziausias
            didziausias = kiekis # jei taip, tai padaro nauju didziausiu
    rezultatas = [] #sukuriamas tuscias masyvas
    for simbolis in tekstas:  # ciklas eina per kiekviena simboli tekste
        if tekstas.count(simbolis) == didziausias and simbolis not in rezultatas:
            rezultatas.append(simbolis)
    print(rezultatas,"-",didziausias )

Atspausdinti_dazniausius_simbolius("  visas geras oras ")
print("_______________________________________________________")
def Atspausdinti_dazniausius_simbolius( tekstas):
    # tekstas = tekstas.replace(" ","") #panaikiname is teksto tarpus
    rezultatas = []  # sukuriamas tuscias masyvas
    didziausias = 0  # susikuriame skaitikli simboliu pasikartojimams skaiciuoti
    for simbolis in tekstas: # ciklas eina per kiekviena simboli tekste
        skaicius = tekstas.lower().count(simbolis)
        if skaicius > didziausias:
            didziausias = skaicius
    for simbolis in tekstas:
        if tekstas.lower().count(simbolis) == didziausias and simbolis not in rezultatas:
            rezultatas.append(simbolis)
    print(rezultatas,"-",didziausias )

Atspausdinti_dazniausius_simbolius(" Ar visas geras oras")


# 20.Sukurkite funkciją kuri priima tekstą ir atspausdina jame esantį ilgiausią žodį.
print("_______________________20.________________________________")
def Atspausdinti_ilgiausia_zodzi(tekst):  # tekstas su kuriuo dirba funkcija
        ilgiausias = " " # sukuriamas kintamasis
        for zodis in tekst.split():# isdalina teksta pagal tarpus ir grazina kiek zodziu tekste
                if len( zodis) > len(ilgiausias):
                    ilgiausias = zodis
        print(ilgiausias)

Atspausdinti_ilgiausia_zodzi("Gyvenimas yra nesamones")

print("_______________________________________________________")


def Atspausdinti_ilgiausius_zodzius(tekst):  # tekstas su kuriuo dirba funkcija
    zodziai = tekst.split()  # isdalina teksta pagal tarpus ir grazina zodzius
    max_ilgis = 0
    for z in zodziai: # eina per kiek viena zodi, suskaiciuoja jo ilgi ir randa ilgiausia zodi tarp zodziu
        if len(z) > max_ilgis:
            max_ilgis = len(z)
    rezultatas = []
    for z in zodziai:
        if len(z) == max_ilgis:
            rezultatas.append(z)
    print(rezultatas, "zodzio/zodziu ilgis:",max_ilgis)

Atspausdinti_ilgiausius_zodzius("Gyvenimas yra nesamones")