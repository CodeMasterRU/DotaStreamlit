from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.eval_db

joueur_durand_belina = db.joueurs.find_one({"nom_joueur": "Durand", "prenom_joueur": "Belina"})
joueur_caron_camilia = db.joueurs.find_one({"nom_joueur": "Caron", "prenom_joueur": "Camilia"})

if joueur_durand_belina and joueur_caron_camilia:
    match = db.matchs.find_one({
        "$or": [
            {"$and": [{"id_joueur1": joueur_durand_belina["id_joueur"]}, {"id_joueur2": joueur_caron_camilia["id_joueur"]}]},
            {"$and": [{"id_joueur1": joueur_caron_camilia["id_joueur"]}, {"id_joueur2": joueur_durand_belina["id_joueur"]}]}
        ]
    })

    if match:
        creneau = db.creneaux.find_one({"id_creneau": match["id_creneau"]})
        print(f"Le match entre Durand Belina et Caron Camilia a eu lieu le {match['date_match']} à la plage horaire {creneau['plage_horaire']}")
    else:
        print("Aucun match trouvé entre Durand Belina et Caron Camilia.")
else:
    print("Joueurs Durand Belina et/ou Caron Camilia non trouvés.")
