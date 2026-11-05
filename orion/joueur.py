from salle import Salle
from objet import Objet

class Joueur:
  def __init__(self):
    self.emplacement: Salle = None
    self.oxygene = 48
    self.objets = []

  def montrer_etat(self):
    print(f"\nVous êtes dans \"{self.emplacement.nom}\"")
    print(f"Vous avez {self.oxygene} / 80 en oxygène.")
    if len(self.objets) == 0:
      print("Vous n'avez aucun objet en votre possession.\n") 
    else:
      print(f"Vous avez : {", ".join(objet.nom for objet in self.objets)}\n")

  # Gère le choix du déplacement et les blocages si l'objet n'est pas obtenu
  def choix_deplacement(self):
    print(f"\nDepuis le {self.emplacement.nom}, vous pouvez aller dans ces salles :")

    liste_deplacements_brut = self.emplacement.get_possibilite_acces()
    liste_deplacements = [[salle[0].nom, salle[1]] for salle in liste_deplacements_brut]
    
    for i, (salle, condition) in enumerate(liste_deplacements, start=1):
      if not condition:
        print(f"{i}. {salle}")
      else:
        print(f"{i}. {salle} - {condition}")
    print(f"{len(liste_deplacements) + 1}. Ne pas se déplacer")

    choix = 0
    # len(liste_deplacements) + 1 pour avoir la longueur de la liste de déplacement + 1 pour inclure l'option d'annuler
    try:
      while not 1 <= choix <= (len(liste_deplacements) + 1):
        choix = int(input("Où voulez-vous allez ? "))
        if not 1 <= choix <= (len(liste_deplacements) + 1):
          print(f"WARNING : Veuillez entrer un nombre entre 1 et {len(liste_deplacements) + 1}.")
          choix = 0
          continue
        else:
          # Si le choix est correct mais n'est pas l'annulation (sinon crash)
          if choix <= len(liste_deplacements):
            if liste_deplacements[choix - 1][1]:
              print(f"Vous n'avez pas l'objet {liste_deplacements[choix - 1][1]} requis.")
              choix = 0
              continue
      # Si le choix est correct mais n'est pas l'annulation
      if choix <= len(liste_deplacements):
        print(f"Déplacement vers {liste_deplacements[choix - 1][0]}...")
        self.oxygene -= 6
        self.se_deplacer(liste_deplacements_brut[choix - 1][0])
      # Si le choix est l'annulation
      else:
        print("Déplacement annulé, retour au choix principal.")
        return True
    except ValueError:
      print("ERREUR : Valeur incorrecte, déplacement annulé.")

  # Change de salle (je trouve que joueur.se_deplacer(salle) est plus lisible que joueur.emplacement = salle) 
  def se_deplacer(self, salle: Salle):
    self.emplacement = salle

  # Gère le choix du ramassage d'un objet
  def choix_ramassage(self):
    liste_objets = self.emplacement.objets

    if len(liste_objets) == 0:
      print("\nIl n'y a aucun objet à ramasser dans cette salle.")
    else:
      if len(liste_objets) == 1:
        print("\nDans cette salle, vous pouvez ramasser cet objet :")
      else:
        print("\nDans cette salle, vous pouvez ramasser les objets suivants :")
      for i, objet in enumerate(liste_objets, start=1):
        print(f"{i}. {objet.nom} - {objet.utilisation}")
      print(f"{len(liste_objets) + 1}. Ne rien ramasser")

      choix = 0
      # len(liste_objets) + 1 pour avoir la longueur de la liste d'objets + 1 pour inclure l'option d'annuler
      try:
        while not 1 <= choix <= (len(liste_objets) + 1):
          choix = int(input("Quel objet voulez-vous ramasser ? "))
          if not 1 <= choix <= (len(liste_objets) + 1):
            print(f"WARNING : Veuillez entrer un nombre entre 1 et {len(liste_objets) + 1}.")
            choix = 0
            continue
        # Si le choix est correct mais n'est pas l'annulation
        if choix <= len(liste_objets):
          print(f"Vous avez ramassé {liste_objets[choix - 1].nom}.")
          self.oxygene -= 2
          self.ramasser(liste_objets[choix - 1])
        # Si le choix est l'annulation
        else:
          print("Ramassage annulé, retour au choix principal.")
          return True
      except ValueError:
        print("ERREUR : Valeur incorrecte, ramassage annulé.")

  # Ramasse un objet (même justification que .se_deplacer(salle)) 
  def ramasser(self, objet: Objet):
    self.objets.append(objet)
    self.emplacement.objets.remove(objet)

  # Gère le choix de l'utilisation d'un objet
  def choix_utilisation(self):
    if len(self.objets) == 0:
      print("\nVous n'avez aucun objet.")
    else:
      print("\nVotre liste d'objets :")
      for i, objet in enumerate(self.objets, start=1):
        print(f"{i}. {objet.nom} - {objet.utilisation}")
      print(f"{len(self.objets) + 1}. Ne rien utiliser")

      choix = 0
      # len(self.objets) + 1 pour avoir la longueur de la liste d'objets + 1 pour inclure l'option d'annuler
      try:
        while not 1 <= choix <= (len(self.objets) + 1):
          choix = int(input("Quel objet voulez-vous utiliser ? "))
          if not 1 <= choix <= (len(self.objets) + 1):
            print(f"WARNING : Veuillez entrer un nombre entre 1 et {len(self.objets) + 1}.")
            choix = 0
            continue
        # Si le choix est correct mais n'est pas l'annulation
        if choix <= len(self.objets):
          print(f"Vous avez utilisé {self.objets[choix - 1].nom}.")
          self.utiliser(self.objets[choix - 1])
        # Si le choix est l'annulation
        else:
          print("Utilisation annulé, retour au choix principal.")
          return True
      except ValueError:
        print("ERREUR : Valeur incorrecte, utilisation annulé.")

  def utiliser(self, objet: Objet):
    if objet.nom == "Bonbonne":
      self.oxygene += 30
      self.oxygene -= 2
      self.objets.remove(objet)
      print("Vous avez regagné 30 d'oxygène.")