import random

from SestaPaskaita_uzdaviniu_sprendimas import rezultatas, masyvas

# 1.Parašykite funkciją, kurios argumentas būtų tekstas, kuris būtų atspausdinamas
# konsolėje pridedant “---” pradžioje ir gale. PVZ (---labas---)
print("_______________________1.S.________________________________")

def atspausdinti_maketuota_teksta(tekstas):
    print(f'---{tekstas}---')
atspausdinti_maketuota_teksta("gyvenimas")
print("_______________________________________________________")
# 2. Sugeneruokite atsitiktinį stringą iš raidžių ir skaičių (10 simbolių). Atspausdinkite simbolius stulpeliu.
# Jei tai skaičius apgaubkite “ [ 7 ]”. Jei skaičiai eina keli iš eilės, apgaubkite juos kartu. [75].
# (apačioje yra funkcija, ją nusikopijuokite ir paleiskite, ji sugeneruos stringą, su kuriuo dirbsite)
print("_______________________2.S.________________________________")

def generate_rnd_str(length):
  symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ12345678901234567890"
  text = ""
  for i in range(length):
    text += symbols[random.randint(0,len(symbols) -1)]
  return text

rezultatas = generate_rnd_str(10)
# apgaubia po viena skaiciu
for simbolis in rezultatas:
  if simbolis.isdigit():
    print(f'[{simbolis}]')
  else:
    print(f'{simbolis}')
print()

print("_______________________________________________________")
def generate_rnd_str(length):
  symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ12345678901234567890"
  text = ""
  for i in range(length):
    text += symbols[random.randint(0,len(symbols) -1)]
  return text

rezultatas = generate_rnd_str(10)
# darbas su sugeneruotu stringu
i = 0
while i < len(rezultatas)-1:  # ciklas vyksta kol egzistuoja dabartinis ir kitas simbolis
  if rezultatas[i].isdigit() and rezultatas[i+1].isdigit(): # tikrina ar eina du skaiciai is eiles
    print(f'[{rezultatas[i]}{rezultatas[i+1]}]') # abu skaiciai paskliaudziami
    i += 2 # zingsnis 2, nes du skaicius apgaube ir juos persoka
  else:
    if rezultatas[i].isdigit(): # kitu atveju tikrina tik viena simboli: ar jis skaicius ir tada ji apskliaudzia
        print(f'[{rezultatas[i]}]')
    else:
      print(f'{rezultatas[i]}') # jei ne skaicius, tai tiesiog atspausdina
    i += 1 # zingsnis 1
if i == len(rezultatas)-1:  # jei i paskutinis simbolis
  if rezultatas[i].isdigit(): # skaicius ir tada ji apskliaudzia
    print(f'[{rezultatas[i]}]')
  else:
    print(f'{rezultatas[i]}') # jei ne skaicius, tai tiesiog atspausdina
print()

# 13. Parašykite funkciją, kuri skaičiuotų, ir gražintų iš kiek sveikų skaičių jos argumentas
# dalijasi be liekanos (išskyrus vienetą ir patį save). Pvz padavus 10 turi grąžinti 2,  o padavus 20 gražintų 4.
print("_______________________3.S.________________________________")
def skaiciaus_dalikliai_kiekis(n):
    count = 0 # skaiciuoja kiek rasta dalikliu
    for i in range(2,n): # ciklas kaip daliklius tikrina visas reiksmes nuo 2 iki (n-1): 2,3,4,5,..., pagal salyga nereikia tikrinti 1 ir n
      if n % i == 0:
        count += 1 #jei skaicius dalinasi is daliklio, tai didina kieki
    return count
rezultatas = skaiciaus_dalikliai_kiekis(16)
print(rezultatas)
print("_______________________________________________________")

# detalus sprendimas supratimui
def skaiciaus_dalikliai_kiekis(n):
  count = 0  # skaiciuoja kiek rasta dalikliu
  for i in range(2,n):  # ciklas kaip daliklius tikrina visas reiksmes nuo 2 iki (n-1): 2,3,4,5,..., pagal salyga nereikia tikrinti 1 ir n
    print(f'tikrina skaiciu:{i}')
    if n % i == 0:
      print(f'dalinasi be liekanos')
      count += 1  # jei skaicius dalinasi is daliklio, tai didina kieki
      print(f'dalikliu yra {count}')
    else:
      print(f'nesidalina')
    print()
  return count


rezultatas = skaiciaus_dalikliai_kiekis(17)
print(rezultatas)

# 4.Sugeneruokite masyvą iš 100 elementų, kurio reikšmės atsitiktiniai skaičiai nuo 33 iki 77.
# Išrūšiuokite masyvą pagal daliklių be liekanos kiekį mažėjimo tvarka, panaudodami trečio uždavinio funkciją.

print("_______________________4.S.________________________________")


# def skaiciaus_dalikliai_kiekis(n):
#     count = 0  # skaiciuoja kiek rasta dalikliu
#     for i in range(2, n):  # ciklas kaip daliklius tikrina visas reiksmes nuo 2 iki (n-1): 2,3,4,5,..., pagal salyga nereikia tikrinti 1 ir n
#       print(f'tikrina skaiciu:{i}')
#       if n % i == 0:
#         print(f'dalinasi be liekanos')
#         count += 1  # jei skaicius dalinasi is daliklio, tai didina kieki
#         print(f'dalikliu yra {count}')
#       else:
#         print(f'nesidalina')
#       print()
#     return count
#
# masyvas = [random.randint(33,77) for _ in range(100)]
# print(masyvas)
#
# for elementas in masyvas:
#   print(f'{elementas} ir jo dalikliai {skaiciaus_dalikliai_kiekis(elementas)}')


def skaiciaus_dalikliai_kiekis(n):
    count = 0  # skaiciuoja kiek rasta dalikliu
    for i in range(2, n):  # ciklas kaip daliklius tikrina visas reiksmes nuo 2 iki (n-1): 2,3,4,5,..., pagal salyga nereikia tikrinti 1 ir n
      if n % i == 0:
        count += 1  # jei skaicius dalinasi is daliklio, tai didina kieki
    return count #grazina dalikliu skaiciu
masyvas = [random.randint(33,77) for _ in range(100)] #sukuria masyva
print(masyvas)

for elementas in masyvas: # ciklas eina per kiekviena elementa is masyvo
  print(f'{elementas} ir jo dalikliai {skaiciaus_dalikliai_kiekis(elementas)}') # skaiciuoja kiek dalikliu jis turi be 1 ir saves pacio

for i in range(len(masyvas)): # isorinis ciklas tikrina tiek kartu, kiek masyve skaiciu
  for j in range(len(masyvas)-1): # vidinis ciklas eina per masyva ir lygina elementus viena salia kito
      left = masyvas[j] # paima kaimynus arba viena salia kito
      right = masyvas[j+1] # paima kaimynus arba viena salia kito
      if skaiciaus_dalikliai_kiekis(left)< skaiciaus_dalikliai_kiekis(right): # tikrina salyga liel dalikliu kuris skaicius turi ir juos sukeicia vietomis, jei reikia
            masyvas[j],masyvas[j+1] = masyvas[j+1],masyvas[j]
print(f'\nSurusiuotas masyvas')
for sk in masyvas:
  print(sk,"dalikliu:", skaiciaus_dalikliai_kiekis(sk))

print("_______________________________________________________")
def skaiciaus_dalikliai_kiekis(n):
    count = 0  # skaiciuoja kiek rasta dalikliu
    for i in range(2, n):  # ciklas kaip daliklius tikrina visas reiksmes nuo 2 iki (n-1): 2,3,4,5,..., pagal salyga nereikia tikrinti 1 ir n
      if n % i == 0:
        count += 1  # jei skaicius dalinasi is daliklio, tai didina kieki
    return count  # grazina dalikliu skaiciu
masyvas = [random.randint(33, 77) for _ in range(100)]  # sukuria masyva
print(masyvas)

for elementas in masyvas:  # ciklas eina per kiekviena elementa is masyvo
  print( f'{elementas} ir jo dalikliai {skaiciaus_dalikliai_kiekis(elementas)}')  # skaiciuoja kiek dalikliu jis turi be 1 ir saves pacio
surusiuotas = sorted(masyvas, # rusiuojamas sarasas
                     key=skaiciaus_dalikliai_kiekis, # pagal ka vyksta rusiavimas
                     reverse= True ) # nuo didziausio iki maziausio

print(f'\nSurusiuotas masyvas pagal dalikliu kieki') # atspausdina surusiuota masyva
for sk in surusiuotas:
  print(sk, "dalikliu:", skaiciaus_dalikliai_kiekis(sk))