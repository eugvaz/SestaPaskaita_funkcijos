

import time
def say_hi(): # nieko nepriima ir nieko negrazina
    print("hi")
say_hi()
say_hi()
say_hi()
def say_hi_to(name):#priima kintamaji, nieko negrazina
    print(f'hi {name}')

say_hi_to('Jonas')
say_hi_to('Naglis')
vardas = "Viktoras"
say_hi_to(vardas)

def sim_pi():# nieko nepriima, grazina reiksme
    return 3.1415

var = sim_pi()
print(var)


print(sim_pi())

def sumavimas(a, b):#priima du kintamuosius, grazina reiksme
    return a + b

print(sumavimas(4,48))
print( sum([4,48]) )

print(time.time())

def make_initials(name,surname):
    return (name[0] + surname[0]).upper()

initials = make_initials('Jonas', 'Jablonskis')
print(initials)

def make_initials_v2(text):
    pts = text.split()
    init = ""
    for pt in pts:
        init += pt[0]
    return init.upper()

res = make_initials_v2("Anzelmas Aluizas Mikalojus Konstantinas")

print(res)

def calc_age(birth_year = 2026):
    return 2026 - birth_year

print(calc_age(2002))
print(calc_age(1994))
print(calc_age())

def print_info(name = "", surname = "", birth_year = 0):
    print("mano vardas",name,"pavarde",surname,"gimimo metai",birth_year)

print_info('Naglis', 'Mockevicius',1998)
print_info('Naglis', 'Mockevicius')
print_info('Naglis', 1998)
print_info('Naglis', birth_year=1998)
print_info(name='Naglis', surname='Mockevicius',birth_year=1998)

print(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1, sep=" :) ", end=" ?")
print()

weirdo = "Anzelmas Aluizas Mikalojus Konstantinas"
print(weirdo.split())
print(weirdo.split("a"))
print(weirdo.split(sep="a"))
print(weirdo.split(sep="a", maxsplit=3))