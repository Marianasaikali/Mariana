#mariana Saikali, Saimar09@ecolecatholique.ca
#2020-12-09

while True:
  print("Choisir une des option (1 ou 2) ou q pour quiter")
  print("1. Ecrire how are you?")
  print("2. Faire la somme de 0 jusqu'a une valeure")
  
  userInput = input()
  if userInput == "q":
    break 
  elif (userInput=="1"):
    print("how are you?")
  elif (userInput == "2"):
    print("Entrez une valeur pour trouver la somme de 0 a ce nombre")
    nombre = input()
    somme = 0
    for i in range(int(nombre)+1):
      somme=somme+i

    print("La somme est: "+str(somme))

  else:
    print("Erreure. Essayer encore")

