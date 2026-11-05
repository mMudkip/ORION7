from salle import Salle
from joueur import Joueur

class StationOrbitale:
  def __init__(self, nom: str):
    self.nom = nom
    self.salles: list[Salle] = []

  def ajouter_salle(self, *salles: Salle):
    for salle in salles:
      if not self.verifier_salle(salle):
        self.salles.append(salle)

  # Renvoie un bool pour si la Salle en paramètre est présente dans la StationOrbitale
  def verifier_salle(self, salle: Salle):
    return salle in self.acces_a

  # Permet d'ajouter un lien entre une Salle et une autre (dans les 2 sens)
  def ajouter_acces(self, salle_1: Salle, salle_2: Salle, objet = None):
    if not salle_1.verifier_acces(salle_2):
      salle_1.acces_a.append([salle_2, objet])
      if not salle_2.verifier_acces(salle_1):
        self.ajouter_acces(salle_2, salle_1, objet)
    # else:
    #   print(f"ERREUR : La salle \"{salle.nom}\" est déjà reliée à {self.nom}.")

  def afficher_map(self, joueur: Joueur):
    sas = " sas "
    reserve = " réserve "
    laboratoire = " laboratoire "
    machines = " machines "
    commande = " commande "

    if joueur.emplacement.nom.lower() == sas.strip():
      sas = "-SAS-"
    elif joueur.emplacement.nom.lower() == reserve.strip():
      reserve = "-RÉSERVE-"
    elif joueur.emplacement.nom.lower() == laboratoire.strip():
      laboratoire = "-LABORATOIRE-"
    elif joueur.emplacement.nom.lower() == machines.strip():
      machines = "-MACHINES-"
    elif joueur.emplacement.nom.lower() == commande.strip():
      commande = "-COMMANDE-"

    print(f"""\n{"=" * 40} {self.nom} {"=" * 40}
Vous êtes dans {joueur.emplacement.nom}
                ┌───────────┐
                │ {reserve} │
                └─────┬─────┘
    ┌───────┬─────────┘
    │ {sas} │
    └───────┴─────────┐
              ┌───────┴───────┐               ┌────────────┐                  ┌────────────┐
              │ {laboratoire} ├── badge (X) ──┤ {machines} ├── réacteur (X) ──┤ {commande} │
              └───────────────┘               └────────────┘                  └────────────┘
    """)