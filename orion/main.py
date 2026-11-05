from station import StationOrbitale
from salle import Salle
from joueur import Joueur

# Setup
orion = StationOrbitale("ORION-7")
joueur = Joueur()

s_sas = Salle("Sas")
s_reserve = Salle("Réserve")
s_laboratoire = Salle("Laboratoire")
s_machines = Salle("Machines")
s_commandes = Salle("Commande")

orion.ajouter_acces(s_sas, s_reserve)
orion.ajouter_acces(s_sas, s_laboratoire)
orion.ajouter_acces(s_laboratoire, s_machines, "badge")
orion.ajouter_acces(s_machines, s_commandes, "réacteur")

s_sas.DEBUG_obtenir_acces()
s_reserve.DEBUG_obtenir_acces()
s_laboratoire.DEBUG_obtenir_acces()
s_machines.DEBUG_obtenir_acces()
s_commandes.DEBUG_obtenir_acces()

# Setup du départ
joueur.emplacement = s_sas

while True:
  orion.afficher_map(joueur)
  quitter = joueur.choix_deplacement()
  if quitter:
    break