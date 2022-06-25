a = int(input("Zadej první hodnotu:"))
b = int(input("Zadej druhou hodnotu:"))

def nasobeni (a, b):
   vysledek = a * b
   return (vysledek)

x1 = nasobeni(a, b)
print("Součin je:", x1)

def scitani (a, b):
   vysledek = a + b
   return (vysledek)

x2 = scitani(a, b)
print("Součet je:", x2)

def deleni (a, b):
   vysledek = a / b
   return (vysledek)

x3 = deleni(a, b)
print("Podíl je:", x3)

def odecitani (a, b):
   vysledek = a - b
   return (vysledek)

x4 = odecitani(a, b)
print("Rozdíl je:", x4)

def mocnina (a, b):
   vysledek = a ** b
   return (vysledek)

x5 = mocnina(a, b)
print("Výsledek je:", x5)