from station import StationOrbitale
from salle import Sas, Reserve, Laboratoire, Machines, Commande
from joueur import Joueur
from objet import Badge, Cable, Fusible

# Setup
orion = StationOrbitale("ORION-7")
joueur = Joueur()

s_sas = Sas()
s_reserve = Reserve()
s_laboratoire = Laboratoire()
s_machines = Machines()
s_commandes = Commande()

orion.ajouter_acces(s_sas, s_reserve)
orion.ajouter_acces(s_sas, s_laboratoire)
orion.ajouter_acces(s_laboratoire, s_machines, "Badge de maintenance requis")
orion.ajouter_acces(s_machines, s_commandes, "Réacteur à activer")

# s_sas.DEBUG_obtenir_acces()
# s_reserve.DEBUG_obtenir_acces()
# s_laboratoire.DEBUG_obtenir_acces()
# s_machines.DEBUG_obtenir_acces()
# s_commandes.DEBUG_obtenir_acces()

# Setup du départ
joueur.emplacement = s_sas
#DEBUG
# joueur.objets = [Badge(), Cable(), Fusible()]

while True:
  if joueur.oxygene > 0:
    orion.afficher_map(joueur)
    quitter = orion.action(joueur)
    if quitter:
      break
  else:
    print("\nVous n'avez plus d'oxygène...")
    break