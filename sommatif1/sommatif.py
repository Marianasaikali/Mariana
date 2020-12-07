#mariana saikali, saimar09@ecolecatholique.ca
#2020-12-04

#mit un syteme pour les points(le score)
score=0
#Demande l'année
print("Qu'elle année la premiere guerre a-t'elle commencer?")
#donner les choix multiple de la question
print("mettre 1, 2 ou 3")
print("1 1914")
print("2 1925")
print("3 1919")
reponse=int(input())
#1 point si la reponse est bon
if reponse==1:
  print("Bonne reponse! Passe a la prochaine question")
  score+=1
else:
  print("Mauvaise réponse, réessayez.")

#Pose une autre question
print("Qu'elle est la plus haute montagne du Canada?")
#donner les choix multiple de la question
print("mettre 1, 2, 3 ou 4")
print("1 Mont-Tremblant")
print("2 Montagne Pyramide")
print("3 Mont Logan")
print("4 Montagne Cascade")
reponse=int(input())
if reponse==3:
  print("Bonne reponse! Passe a la prochaine question")
  #1 point si la reponse est bon
  score+=1
else:
  print("Mauvaise réponse, réessayez.")

#pose une autre question
print("Quel est l'animal terrestre le plus rapide au monde?")
#donner les choix multiple de la question
print("mettre 1, 2, 3 ou 4")
print("1 Lion")
print("2 Guépard")
print("3 Kangaroo")
print("4 Gazelle de Thompson")
reponse=int(input())
if reponse==2:
  print("Bonne reponse! Passe a la prochaine question")
  #1 point si la reponse est bon
  score+=1
else:
  print("Mauvaise réponse, réessayez.")

print(score+" /3")
print(score)