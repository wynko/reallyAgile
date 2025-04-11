import os

def supprimer_fichier():
    nom = input("Nom du fichier à supprimer : ")
    os.system("rm " + nom)

supprimer_fichier()
