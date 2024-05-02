from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.eval_db

joueurs_dans_hangar = db.matchs.distinct("id_joueur1", {"id_terrain": 3}) + db.matchs.distinct("id_joueur2", {"id_terrain": 3})

occurrences = {}
for joueur in joueurs_dans_hangar:
    occurrences[joueur] = occurrences.get(joueur, 0) + 1

joueurs_uniques = [joueur for joueur, occ in occurrences.items() if occ == 1]

noms_joueurs_uniques = []
for joueur_id in joueurs_uniques:
    joueur = db.joueurs.find_one({"id_joueur": joueur_id})
    if joueur:
        noms_joueurs_uniques.append(f"{joueur['prenom_joueur']} {joueur['nom_joueur']}")

if len(noms_joueurs_uniques) == 2:
    print("Les deux joueurs uniques qui ont joué dans le hangar sont :", ", ".join(noms_joueurs_uniques))
elif len(noms_joueurs_uniques) > 2:
    print("Il y a plus de deux joueurs uniques qui ont joué dans le hangar.")
else:
    print("Il n'y a pas assez de joueurs uniques qui ont joué dans le hangar.")
