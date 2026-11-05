class Objet:
  def __init__(self, nom: str, utilisation: str):
    self.nom = nom
    self.utilisation = utilisation

class Badge(Objet):
  def __init__(self):
    super().__init__("Badge de maintenance", "Permet d'ouvrir l'accès vers Machines depuis Laboratoire")

class Cable(Objet):
  def __init__(self):
    super().__init__("Câble électrique", "S'installe dans Machines")

class Fusible(Objet):
  def __init__(self):
    super().__init__("Fusible", "S'installe dans Machines")

class Bonbonne(Objet):
  def __init__(self):
    super().__init__("Bonbonne", "Redonne 30 d'oxygène, utilisable qu'une fois")