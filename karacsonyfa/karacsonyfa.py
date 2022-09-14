x = ""
def karacsony(num):
    szamlalo = 0
    szam = num - 1
    for i in range(num):
        print((szam * " ")+(szamlalo * "*") + "*" + (szamlalo * "*"))
        szamlalo += 1
        szam -= 1
    return x
print(karacsony(7))
