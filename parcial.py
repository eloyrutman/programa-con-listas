ls = []
kw = prom = 0
nombre = consumo = consumo2 = " "
archivo = open("Consumo.txt")
split = kilowats = " "
total = total2 = division = 0
mnon = mnom1 = " "
nprom = marc = 0
mismo = mismo1 = 0
masde = porc = porc2 = porc3 = 0
primer = " "
cons = 0

print("Nombre       Consumo        Total")
for kilowats in archivo:
    split = kilowats.split(",")
    nombre = split[0]
    consumo = int(split[1])
    consumo2 = int(split[2])
    total += consumo2
    total2 += consumo
    consumo3 = (consumo2 - consumo)
    division += 1
    prom = (total - total2) / division
    porc = consumo3
    cons = consumo3
    ls.append(consumo3)
    mismo1 = ls.count(consumo3)
    if porc <= 100:
        porc2 += 1
        porc3 = (porc2*100)/division
    if consumo3 >= 280:
        masde +=1
    if masde == 1:
        primer = nombre
    if consumo3 >= 800:
        kw = (100*0.51)+(200*0.50)+(250*0.45)+(300*0.40)+((consumo3-800)*0.35)
    if consumo3 <= 800 and consumo3 >= 550:
        kw = (100*0.51)+(200*0.50)+(250*0.45)+((consumo3-550)*0.40)
    if consumo3 <= 550 and consumo3 >= 301:
        kw = (100*0.51)+(200*0.50)+((consumo3-300)*0.45)
    if consumo3 <= 301 and consumo3 >= 101:
        kw = (100*0.51)+((consumo3-100)*0.45)
    if consumo3 <=101:
        kw = (consumo3)*.051
    print ("{0:10}       {1:2}         {1:2.1f}".format(nombre,consumo3,kw))
    if (marc == 0):
        nprom = consumo3
        mnom = nombre
        marc = 1
    elif nprom <= consumo3:
        nprom = consumo3
        mnom = nombre
        mnom1 = " "
    elif nprom == prom:
        mnom1 = nombre

    
print("Suscriptor que tuvo más consumo:",mnom)
print("Promedio de consumo:",f"{prom:.2f}")
print("Porcentaje de suscriptores con consumos hasta 100 Kw maximo:",f"{porc3:.2f}")
print("Se encontraron",mismo1, "con el mismo consumo")
print("Primer suscriptor que consumió 280 kw:",primer)

    
    
