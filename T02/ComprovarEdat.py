# Programa que demana l'edat i diu si ets major d'edat.

edat=int(input("¿Moz@ que años tiens tu?"))

if edat>=18 and edat<=99:
    print("Lla eresh maiorzito AB")
elif edat==17:
    print("Eshtash Jodydou")
elif edat<17 and edat>=1 :
    print("Pitufo")
elif edat<=0 or edat>=100:
    print("T'ah ekivocau")
else:
    print("¿¿Que ash pueshto shabal??")


print("Shabal q za cabao")