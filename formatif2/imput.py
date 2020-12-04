

#demander le nom
print("c'est quoi ton nom?")
nom=input()
print("je comprend", nom)
#verifier le nom
print("est ce que cest bon? oui ou non")
bon=input().lower()

if bon == "oui":
  print("parfait")
elif bon =="non":
  #demander le nom encore
  print("entre ton nom en nouveau")
  nom=input()
  print("je comprend", nom)
else:
  print("je nest pas compris. on va juste continuer")

print("fin")