import random
kleur = ['oranje', 'blauw', 'groen','bruin']
zak = {
    "oranje": 0,
    "blauw": 0,
    "groen": 0,
    "bruin": 0
}
def smarties():
    vraag1 = int(input("Hoeveel MnM's wil je toevoegen? "))
    for x in range(0, vraag1):
        nummer = random.randint(0, 3)
        smart = (kleur[nummer])
        zak[smart] = zak[smart] +1
        
    return

smarties()
result ={k: m for k, m in sorted(zak.items(), key= lambda m: m[1], reverse=True)}
print(result)