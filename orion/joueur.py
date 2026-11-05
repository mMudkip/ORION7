from salle import Salle

class Joueur:
  def __init__(self):
    self.emplacement: Salle = None

  def choix_deplacement(self):
    print(f"Depuis le {self.emplacement.nom}, vous pouvez aller dans ces salles :")

    liste_deplacements_brut = self.emplacement.get_possibilite_acces()
    liste_deplacements = [[salle[0].nom, salle[1]] for salle in liste_deplacements_brut]
    
    for i, (salle, objet) in enumerate(liste_deplacements, start=1):
      if not objet:
        print(f"{i}. {salle}")
      else:
        print(f"{i}. {salle} - {objet} requis")
    print(f"{len(liste_deplacements) + 1}. Ne pas se déplacer")

    choix = 0
    # len(liste_deplacements) + 1 pour avoir la longueur de la liste de déplacement + 1 pour inclure l'option d'annuler
    try:
      while not 0 < choix <= (len(liste_deplacements) + 1):
        choix = int(input("Où voulez-vous allez ? "))
        if not 0 < choix <= (len(liste_deplacements) + 1):
          print(f"WARNING : Veuillez entrer un nombre entre 1 et {len(liste_deplacements) + 1}.")
          choix = 0
          continue
        else:
          # Si le choix est correct mais n'est pas l'annulation
          if choix < (len(liste_deplacements) + 1):
            if liste_deplacements[choix - 1][1]:
              print(f"Vous n'avez pas l'objet {liste_deplacements[choix - 1][1]} requis.")
              choix = 0
              continue
      if choix <= len(liste_deplacements):
        print(f"Déplacement vers {liste_deplacements[choix - 1][0]}...")
        self.se_deplacer(liste_deplacements_brut[choix - 1][0])
      else:
        print("Déplacement annulé, retour au choix principal.")
        return True
    except ValueError:
      print("ERREUR : Valeur incorrecte, déplacement annulé.")

  def se_deplacer(self, salle: Salle):
    self.emplacement = salle