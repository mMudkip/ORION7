from objet import Objet, Badge, Cable, Fusible, Bonbonne

class Salle:
  def __init__(self, nom: str):
    self.nom = nom
    self.acces_a: list[Salle] = []
    self.objets = []

  # Renvoie un bool pour si la Salle en paramètre est reliée à cette Salle
  def verifier_acces(self, salle: Salle):
    # return salle in self.acces_a
    return any(s[0] == salle for s in self.acces_a)

  def get_possibilite_acces(self):
    return self.acces_a

  def observation(self):
    print(f"\nOBSERVATION - {self.nom.upper()}")
    self.DEBUG_obtenir_objets()

  # DEBUG uniquement
  def DEBUG_nom(self):
    return f"{self.nom} {self}"

  def DEBUG_obtenir_acces(self):
    print("-" * 10, self.DEBUG_nom(), "liste accès", "-" * 10)
    for salle in self.acces_a:
      print(salle[0].DEBUG_nom(), salle[1])

  def DEBUG_obtenir_objets(self):
    print("-" * 10, self.DEBUG_nom(), "liste objets", "-" * 10)
    for objet in self.objets:
      print(objet.nom, objet)

class Sas(Salle):
  def __init__(self):
    super().__init__("Sas")

  def observation(self):
    super().observation()
    print("Il n'y a rien à faire dans cette salle.")

class Reserve(Salle):
  def __init__(self):
    super().__init__("Réserve")
    self.objets: list[Objet] = [Badge(), Cable()]

  def observation(self):
    super().observation()
    if len(self.objets) == 0:
      print("Il y a le Badge de maintenance et le Câble électrique.")
    else:
      # print("Il y a le Badge de maintenance.")
      # print("Il y a le Câble électrique.")
      print("Il n'y a rien à faire dans cette salle.")

class Laboratoire(Salle):
  def __init__(self):
    super().__init__("Laboratoire")
    self.objets: list[Objet] = [Fusible(), Bonbonne()]

  def observation(self):
    super().observation()
    if len(self.objets) == 0:
      print("Il y a le Fusible, la Bonbonne et le Journal qui permet de savoir le Code du réacteur.")
    else:
      # print("Il y a le Fusible et le Journal qui permet de savoir le code du réacteur.")
      # print("Il y a la Bonbonne et le Journal qui permet de savoir le code du réacteur.")
      print("Il y a le Journal qui permet de savoir le code du réacteur.")

class Machines(Salle):
  def __init__(self):
    super().__init__("Machines")

  def observation(self):
    super().observation()
    if len(self.objets) == 0:
      print("Dans cette salle, vous pouvez redémarrer le Réacteur si vous saisissez le Code, après avoir installer le Câble électrique ainsi que le Fusbile.")
    # else:
    #   print("Dans cette salle, vous pouvez redémarrer le Réacteur si vous saisissez le Code, après avoir installer le Fusbile.")
    #   print("Dans cette salle, vous pouvez redémarrer le Réacteur si vous saisissez le Code, après avoir installer le Câble électrique.")
    #   print("Dans cette salle, vous pouvez redémarrer le Réacteur si vous saisissez le Code.")

class Commande(Salle):
  def __init__(self):
    super().__init__("Commande")

  def observation(self):
    super().observation()
    print("D'ici, vous pouvez évacuer !")