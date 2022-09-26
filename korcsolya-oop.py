class Korcsolya:
    def __init__(self,sor):
        nev,orszag,technika,komponens,hiba = sor.strip().split(";")
        self.nev = nev
        self.orszag = orszag
        self.technika = float(technika)
        self.komponens = float(komponens)
        self.hiba = int(hiba)
        

class Korcsolya_donto:
    def __init__(self,sor):
        nev_d,orszag_d,technika_d,komponens_d,hiba_d = sor.strip().split(";")
        self.nev_d = nev_d
        self.orszag_d = orszag_d
        self.technika_d = float(technika_d)
        self.komponens_d = float(komponens_d)
        self.hiba_d = int(hiba_d)
        
with open("rovidprogram.csv","r",encoding="latin2") as f:
    fejlec = f.readline()
    lista = [Korcsolya(sor) for sor in f]
    
with open("donto.csv","r",encoding="latin2") as f2:
    fejlec2 = f2.readline()
    donto = [Korcsolya_donto(sor) for sor in f2]
    
print(f"""2. feladat
        A rövidprogramban {len(lista)} induló volt""")

print("3. feladat")

volt_e_magyar = [sor for sor in lista if sor.orszag == "HUN"]

if volt_e_magyar:
    print("        A magyar versenyző bejutott a kűrbe")
else:
    print("        A magyar versenyző nem jutott be a kűrbe")
    
def ÖsszPontszám():
    kereso = [sor for sor in lista if sor.nev == bekeres]
    if kereso:
        pontszamok = [(sor.technika,sor.komponens,sor.hiba) for sor in kereso]
        return (pontszamok[0][0] + pontszamok[0][1]) - pontszamok[0][2]
    else:
        return "        Ilyen nevű induló nem volt"
    
print("5.feladat")

bekeres = input("        Kérem a versenyző nevét: ")

kereso = [sor for sor in lista if sor.nev == bekeres]

meghivo = ÖsszPontszám()

if kereso:
    print(f"""6. feladat
        A versenyző Összpontszáma: {meghivo}""")
else:
    print(f"{meghivo}")
    
stat = dict()
for sor in donto:
    stat[sor.orszag_d] = stat.get(sor.orszag_d,0) + 1

print("7. feladat")
statisztika = [print(f"        {orszag}: {db} versenyző") for orszag,db in stat.items() if db > 1]
    
with open("vegeredmeny.csv","w",encoding="UTF-8") as f3:
    for sor in donto:
            jatekos = sor.nev_d
            pontszamok_d = [(sor.technika_d,sor.komponens_d,sor.hiba_d) for sor in donto if sor.nev_d == jatekos]
            jatekos_adatai = [sor for sor in donto if sor.nev_d == jatekos]
            pontszam_x_jatekosnak = (pontszamok_d[0][0] + pontszamok_d[0][1]) - pontszamok_d[0][2]
            pontszamok2 = [(sor.technika,sor.komponens,sor.hiba) for sor in lista if sor.nev == jatekos]
            pontszam_x_jatekosnak2 = (pontszamok2[0][0] + pontszamok2[0][1]) - pontszamok2[0][2]
            ossz11 = float(pontszam_x_jatekosnak2) + float(pontszam_x_jatekosnak)
            ossz11 = f"{ossz11:.2f}"
            f3.write(f"{jatekos};{jatekos_adatai[0].orszag_d};{ossz11}\n")

class Vegeredmeny:
    def __init__(self,sor):
        nev,orszag,pont = sor.strip().split(";")
        self.nev = nev
        self.orszag = orszag
        self.pont = float(pont)

with open("vegeredmeny.csv","r",encoding="UTF-8") as f2:
    lista = [Vegeredmeny(sor) for sor in f2]
    
with open("vegeredmeny.csv","w",encoding="UTF-8") as f4:
    lista.sort(key=lambda x:x.pont,reverse=True)
    for sor in lista:
        f4.write(f"{sor.nev}:{sor.orszag} {str(sor.pont)}\n")
        
        
with open("vegeredmeny.csv","w",encoding="UTF-8") as f5:
    szamlalo = 1
    for sor in lista:
        f5.write(f"{szamlalo};{sor.nev}:{sor.orszag} {str(sor.pont)}\n")
        szamlalo = szamlalo + 1
