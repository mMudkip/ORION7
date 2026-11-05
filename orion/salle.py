class Salle:
  def __init__(self, nom: str):
    self.nom = nom
    self.acces_a: list[Salle] = []

  # Renvoie un bool pour si la Salle en paramètre est reliée à cette Salle
  def verifier_acces(self, salle: Salle):
    # return salle in self.acces_a
    return any(s[0] == salle for s in self.acces_a)

  # DEBUG uniquement
  def DEBUG_nom(self):
    return f"{self.nom} {self}"

  def DEBUG_obtenir_acces(self):
    print("-" * 10, self.DEBUG_nom(), "liste accès", "-" * 10)
    for salle in self.acces_a:
      print(salle[0].DEBUG_nom(), salle[1])