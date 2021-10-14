# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from builtins import enumerate
import operator

text=str(input("Idatzi hemen desenkriptatu nahi duzun testua: ")) # pedir un texto cifrado


alfabetoa={"A": 0, "B":0, "C":0, "D":0,
            "E":0, "F":0, "G":0, "H":0,
            "I":0, "J":0 ,"K":0, "L":0,
            "M":0, "N":0, "Ñ":0, "O":0,
            "P":0, "Q":0, "R":0, "T":0,
            "U":0, "v":0, "Y":0, "W":0, "Z":0}  # crear el diccionario


for i in text:         # contar cuantas veces se repiten las letras
    for e in alfabetoa:
        if(i==e):
            alfabetoa[e] += 1


for f in enumerate(alfabetoa):      # mostrar las letras del diccionario y cuantas veces se han repertido
    print(f[1], ":",alfabetoa[f[1]])

input("Sacatu enter erabili diren letrak ordenatzeko gehienetik gutxienera")
print("")

alfa_or=sorted(alfabetoa.items(),key=operator.itemgetter(1),reverse=True)    # ordenar las letras mas usadas y las respectivas cantidades
print(alfa_or)

input("gehien erabiltzen diren lehenengo bi letrak maiztasun analisi baten ondorioz e eta a letren ordez aldatuko ditugu:")
print("")

lista_ord=[]
for i in enumerate(alfa_or):         #crear una lista ordenada de las letras mas usadas
    lista_ord.append(i[1][0])


text2=str(text.replace(lista_ord[0], "e"))    # sustituir las letras q se encuentran en las dos primeras posiciones de la lista ordenada
text=str(text2.replace(lista_ord[1], "a"))
print(text)       #devolver el nuevo texto

cont=1
while(text.islower()==False):
    if(cont==1 or cont==2):
        a=str(input("Bi eta hiru letrez osatutako hitzak begiratuz jakin ahal dugu beste letraren bat? zein da aldatuko zenuke letra?(maiuskulaz) "))
        b=str(input("Zein letrarekin aldatuko zenuke? "))


    elif(cont!=3 and cont!=1 and cont!=2):
        a = input(" Lortu dugunarekin, beste letra bat jakin ahal dugu? Zein?")
        b = input("Zein letrarekin aldatuko zenuke?")


    if(cont==3):
        print("Frekuentzia analisia jarraituz normalean gehien erabiltzen den hurrengoa 'o' letra da, beraz gure letren lista ordenatua jarraituz zein letrarekin aldatu beharko genuke? ")
        a = input("(Goian duzun listan begiratu erabili ez dugun letren artean zein den gehien erabiltzen dena): ")
        b= "o"

    text2 = str(text.replace(a, b))  # sustituir las letras q hemos recibido
    print(text2)
    text = text2
    cont=cont+1



















