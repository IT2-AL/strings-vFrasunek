#1. úkol
print("ahoj".upper())

#2. úkol
print("AHOJ".lower())

#3. úkol
print("python".count("p"))
print("python".count("y"))
print("python".count("k"))
print("program".count("p"))
print("program".count("y"))
print("program".count("k"))

#4. úkol
print("python".index("t",0))

#5. úkol
print("program"[2:5])

#6. úkol
print("ahoj" + "slunce")

#7. úkol
jmeno = input("zadejte své jméno")
prijmeni = input("zadejte své příjmení")
print(jmeno[0].upper())
print(prijmeni[0].upper())

#2.--------------cvičení--------------------

#1. úkol
mesta = ["Praha","Berlín","Ostrava","Brno","Ústí nad labem"]

#2. úkol
print(mesta)

#3. úkol
print(mesta[3])

#4. úkol
for mesta in mesta:
  print(mesta)

  #5. úkol
for index, mesta1 in enumerate(mesta, start=1):
    print(f"{index}. {mesta1}")

#6. úkol
mesta.append("chomutov")
print(mesta)

#7. úkol
mesta.pop(1)
  
  #8. úkol
print(mesta)

#9. úkol 
mesta.sort()

#10. úkol
def mesto2(mesto3, mesto4):
    if mesto4 in mesto3:
        return True
    else:
        return False
mesto5 = "Brno"

if mesto2(mesta, mesto5):
    print(f"{mesto5} je v seznamu měst.")
else:
    print(f"{mesto5} není v seznamu měst.")

#11. úkol
mesta2_0 = ["litva,chrudim,ohio,amsterdam"]
mesta_a= [Mesta2_1 for Mesta2_1 in mesta2_0 if Mesta2_1.startswith('a')]
print(mesta_a)

#12. úkol
for mesta69 in mesta2_0:
    if len(mesta69) > 5:
        print(mesta69)