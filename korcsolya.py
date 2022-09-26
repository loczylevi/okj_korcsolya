#Név;   Ország;    Technikai;     Komponens;    Levonás

# 0         1          2               3            4

with open("rovidprogram.csv","r",encoding="latin2") as f:
    fejlec = f.readline()
    lista = [sor.strip().split(";") for sor in f]

#Név;   Ország;    Technikai;     Komponens;    Levonás

# 0         1          2               3            4
    
with open("donto.csv","r",encoding="latin2") as f2:
    fejlec2 = f2.readline()
    donto = [sor.strip().split(";") for sor in f2]
    
print(f"""2. feladat
        A rövidprogramban {len(lista)} induló volt""")

print("3. feladat")

volt_e_magyar = [sor for sor in lista if sor[1] == "HUN"]

if volt_e_magyar:
    print("        A magyar versenyző bejutott a kűrbe")
else:
    print("        A magyar versenyző nem jutott be a kűrbe")
    
def ÖsszPontszám():
    kereso = [sor for sor in lista if sor[0] == bekeres]
    if kereso:
        pontszamok = [(sor[2],sor[3],sor[4]) for sor in kereso]
        return (float(pontszamok[0][0]) + float(pontszamok[0][1])) - float(pontszamok[0][2])
    else:
        return "        Ilyen nevű induló nem volt"
    
print("5.feladat")

bekeres = input("        Kérem a versenyző nevét: ")

kereso = [sor for sor in lista if sor[0] == bekeres]

meghivo = ÖsszPontszám()

if kereso:
    print(f"""6. feladat
        A versenyző Összpontszáma: {meghivo}""")
else:
    print(f"{meghivo}")

stat = dict()
for sor in donto:
    stat[sor[1]] = stat.get(sor[1],0) + 1

print("7. feladat")
statisztika = [print(f"        {orszag}: {db} versenyző") for orszag,db in stat.items() if db > 1]
    

#Név;   Ország;    Technikai;     Komponens;    Levonás

# 0         1          2               3            4

with open("vegeredmeny.csv","w",encoding="UTF-8") as f3:
    for sor in donto:
            jatekos = sor[0]
            pontszamok_d = [(float(sor[2]),float(sor[3]),float(sor[4])) for sor in donto if sor[0] == jatekos]
            jatekos_adatai = [sor for sor in donto if sor[0] == jatekos]
            pontszam_x_jatekosnak = (pontszamok_d[0][0] + pontszamok_d[0][1]) - pontszamok_d[0][2]
            pontszamok2 = [(float(sor[2]),float(sor[3]),float(sor[4])) for sor in lista if sor[0] == jatekos]
            pontszam_x_jatekosnak2 = (pontszamok2[0][0] + pontszamok2[0][1]) - pontszamok2[0][2]
            ossz11 = float(pontszam_x_jatekosnak2) + float(pontszam_x_jatekosnak)
            ossz11 = f"{ossz11:.2f}"
            f3.write(f"{jatekos};{jatekos_adatai[0][1]};{ossz11}\n")

with open("vegeredmeny.csv","r",encoding="UTF-8") as f2:
    lista = [sor.strip().split(";") for sor in f2]
    
with open("vegeredmeny.csv","w",encoding="UTF-8") as f4:
    lista.sort(key=lambda x:x[2],reverse=True)
    for sor in lista:
        f4.write(f"{sor[0]}:{sor[1]} {str(sor[2])}\n")
        
        
with open("vegeredmeny.csv","w",encoding="UTF-8") as f5:
    szamlalo = 1
    for sor in lista:
        f5.write(f"{szamlalo};{sor[0]}:{sor[1]} {str(sor[2])}\n")
        szamlalo = szamlalo + 1