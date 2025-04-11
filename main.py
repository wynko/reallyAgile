import sys

def afficher_introduction():

  print("""
Bonjour.


""")


def main():
  """Fonction principale du script."""
  afficher_introduction()
  print("Veuillez saisir votre question ou requête.")

  while True:
    requete = input("> ")

    if requete.lower() == "quitter":
      print("Fin de la session.")
      break
    else:
      print("Réponse simulée pour : " + requete + ". Veuillez consulter la documentation pertinente pour une réponse précise.")



if __name__ == "__main__":
  main()
