

#--------------- Jeu de mots ------------------

phrases = []
consignes = []

# changer seulement les lignes dans mon_mad_lib ci-dessous
# --> supprimer les phrases.append et consignes.append
# --> ajouter vos propres phrases et consignes
#
# NE CHANGER RIEN D'AUTRE DANS LE PROGRAMME
#
# Si tout le monde fais ça, je vais pouvoir intégrer le
# travail dans un "livre" de mad libs que vous pourrez
# jouer avec votre famille pendant le temps des fêtes
#

def mon_mad_lib():
    """Préparer les phrases à trou""" 

    # le trou dans la phrase est indiqué par les {}
    phrases.append("Apres que je me suis {} pour la journée")
    consignes.append("verbe")
    phrases.append("J'ai {} le sapin de Noel avec ma famille.")
    consignes.append("nom commun")
    phrases.append("Ensuite on est {} faire des biscuits de noel")
    consignes.append("verbe aller au passé parfait")
    phrases.append("On a aussi regarder un {} de noel!")
    consignes.append("nom masculin")
    phrases.append("J'ai enfin passé une belle {} avec ma famille")
    consignes.append("nom féminin")

mon_mad_lib()

# Obtenir les réponses de l'utilisateur
mots = []
# on demande un mot pour chaque consigne, utilisant la boucle 'for each'
for c in consignes:
    # ici le print utilise la méthode .format() qui remplace chaque {}
    # dans le texte avec la valeur dans le .format()
    print("Taper un mot qui est un(e) {}".format(c))
    mots.append(input())


# Afficher le résultat
print("Quand tu est prêt(e) pour le résultat, tape Enter")
input() # attend

for i in range(len(phrases)):
    # les trous {} dans les phrases sont remplacés par les mots.
    print(phrases[i].format(mots[i]))

print("\nMerci d'avoir joué!")