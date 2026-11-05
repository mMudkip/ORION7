from salle import Salle

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
    return salle in self._acces_a

  # Permet d'ajouter un lien entre une Salle et une autre (dans les 2 sens)
  def ajouter_acces(self, salle_1: Salle, salle_2: Salle, objet = None):
    if not salle_1.verifier_acces(salle_2):
      salle_1.acces_a.append([salle_2, objet])
      if not salle_2.verifier_acces(salle_1):
        self.ajouter_acces(salle_2, salle_1, objet)
    # else:
    #   print(f"ERREUR : La salle \"{salle.nom}\" est déjà reliée à {self.nom}.")

  def __str__(self):
    return f"""\n{"=" * 40} {self.nom} {"=" * 40}
Vous êtes dans Sas
                ┌───────────┐
                │  réserve  │
                └─────┬─────┘
    ┌───────┐         │
    │ -SAS- ├─────────┤
    └───────┘         │
              ┌───────┴───────┐               ┌────────────┐                  ┌────────────┐
              │  laboratoire  ├── badge (X) ──┤  machines  ├── réacteur (X) ──┤  commande  │
              └───────────────┘               └────────────┘                  └────────────┘
    """