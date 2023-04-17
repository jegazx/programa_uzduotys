nuoma = int(input("Ar jus nuomojates gyvenama busta: Taip (1) Ne (2)"))
if nuoma == 1:
    busto_nuoma = float(input("Iveskite kiek mokate uz busto nuoma: "))
else:
    busto_mokesciai = float(input("Kiek isleidziate busto mokesciam: "))
    zurnalas -= busto_nuoma + busto_mokesciai

