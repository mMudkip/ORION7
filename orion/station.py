from salle import Salle
from joueur import Joueur
from random import randint

class StationOrbitale:
  def __init__(self, nom: str):
    self.nom = nom
    self.salles: list[Salle] = []
    self.code = self.generer_code()
    print(self.code)

  def generer_code(self):
    return "".join([str(randint(0, 9)), str(randint(0, 9)), str(randint(0, 9)), str(randint(0, 9))])

  def ajouter_salle(self, *salles: Salle):
    for salle in salles:
      if not self.verifier_salle(salle):
        self.salles.append(salle)

  # Renvoie un bool pour si la Salle en paramètre est présente dans la StationOrbitale
  def verifier_salle(self, salle: Salle):
    return salle in self.acces_a

  # Permet d'ajouter un lien entre une Salle et une autre (dans les 2 sens)
  def ajouter_acces(self, salle_1: Salle, salle_2: Salle, condition = None):
    if not salle_1.verifier_acces(salle_2):
      salle_1.acces_a.append([salle_2, condition])
      if not salle_2.verifier_acces(salle_1):
        self.ajouter_acces(salle_2, salle_1, condition)
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
Vous êtes dans "{joueur.emplacement.nom}"\t\tOxygène : {joueur.oxygene} / 80
             ┌───────────┐
             │ {reserve} │
             └─────┬─────┘
 ┌───────┬─────────┘
 │ {sas} │
 └───────┴─────────┐
           ┌───────┴───────┐               ┌────────────┐                  ┌────────────┐
           │ {laboratoire} ├── badge (X) ──┤ {machines} ├── réacteur (X) ──┤ {commande} │
           └───────────────┘               └────────────┘                  └────────────┘
{"=" * 89}\n""")

  def afficher_liste_actions(self, joueur: Joueur):
    print("Voici les actions que vous pouvez faire :")
    print("1. Se déplacer (coût : 6)")
    print(f"2. Observer la salle \"{joueur.emplacement.nom}\" (coût : 1)")
    print("3. Lire le journal (coût : 1)")
    print("4. Ramasser un objet (coût : 2)")
    print("5. Utiliser un objet (coût : 2)")
    print("6. Tenter un code (coût : 3)")
    print("7. Évacuer (coût : 3)")
    print("8. Attendre (coût : 5)")
    print("9. Consulter État/Inventaire (coût : 0)")

  def action(self, joueur: Joueur):
    self.afficher_liste_actions(joueur)

    choix = 0
    while not 1 <= choix <= 9:
      try:
        choix = int(input("Que voulez-vous faire ? "))
        if not 1 <= choix <= 9:
          print(f"WARNING : Veuillez entrer un nombre entre 1 et 9.")
          continue

        print(f"\n{"-" * 89}")

        # Attendre / DEBUG_Quitter
        if choix == 8:
          # TEMP
          # if joueur.oxygene >= 5:
          #   joueur.oxygene -= 5
          return True
        
        # Se déplacer
        elif choix == 1:
          if joueur.oxygene >= 6:
            # Le joueur a la possibilité d'annuler le déplacement, donc le retrait d'oxygène dans la méthode joueur.choix_deplacement()
            joueur.choix_deplacement()
          else:
            print("\nWARNING : vous n'avez pas assez d'oxygène pour pouvoir vous déplacer.")
            continue

        # Observer la salle
        elif choix == 2:
          if joueur.oxygene >= 1:
            joueur.emplacement.observation()
            joueur.oxygene -= 1
          else:
            print("\nWARNING : vous n'avez pas assez d'oxygène pour pouvoir observer une salle.")
            continue

        # Lire le journal
        elif choix == 3:
          if joueur.emplacement.nom == "Laboratoire":
            if joueur.oxygene >= 1:
              print("\nURGENT - CODE RÉACTEUR")
              print(self.code)
              joueur.oxygene -= 1
            else:
              print("\nWARNING : vous n'avez pas assez d'oxygène pour pouvoir lire le Journal.")
          else:
            print("\nWARNING : vous devez être dans le Laboratoire pour pouvoir lire le Journal.")

        # Ramasser un objet
        elif choix == 4:
          if joueur.oxygene >= 2:
            # Le joueur a la possibilité d'annuler le ramassagee, donc le retrait d'oxygène dans la méthode joueur.choix_ramassage()
            joueur.choix_ramassage()
          else:
            print("\nWARNING : vous n'avez pas assez d'oxygène pour pouvoir ramasser un objet.")
            continue

        # Utiliser un objet
        elif choix == 5:
          if joueur.oxygene >= 2:
            # Le joueur a la possibilité d'annuler l'utilisation, donc le retrait d'oxygène dans la méthode joueur.utiliser() appelé dans joueur.choix_utilisation()
            joueur.choix_utilisation()
          else:
            print("\nWARNING : vous n'avez pas assez d'oxygène pour pouvoir utiliser un objet.")
            continue

        # Montrer état/inventaire
        elif choix == 9:
          joueur.montrer_etat()
          # Pour remettre la demande du choix sans afficher la map qui prend toute la place
          choix = 0
          print(f"{"-" * 89}\n")

          continue
      except ValueError:
        print("ERREUR : Valeur incorrecte, veuillez entrer un nombre entre 1 et 9.")