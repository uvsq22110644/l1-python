#########################################
# groupe MIASHS 7
# GOREAU THELMA
# VIGNERON THOMAS
# SOW MAHMOUD
# LIMOUZIN MATTHIEU
# https://github.com/Thelma47/projet1bi
#########################################

# import des modules
import tkinter as tk
import random as rd

# variables globales
H = 600
W = 700 #largeur
m = 6 #nb lignes
n = 7 #nb colonnes
joueur1 = True
grille = []
fin = False
global prenom1
l_coup = []


#création liste à deux dimensions
# 0 : case vide
# 1 : case avec un pion jaune
# 2 : case avec un pion rouge
for i in range(m):
    grille.append([0]*n)



# fonctions
def creation_grille():
    """créer une grille de puissance 4 avec m lignes et n colonnes"""
    #m = int(input("Nombre de lignes ?"))
    #n = int(input("Nombre de colonnes ?"))
    #W = n*100
    #H = m*100
    for i in range(m):
        for j in range(n):
            canvas.create_oval(W/n*j, H/m*i, W/n*(j+1), H/m*(i+1), fill="Dodgerblue3", outline="Dodgerblue2")
            canvas.create_oval(W/n*j+5, H/m*i+5, W/n*(j+1)-5, H/m*(i+1)-5, fill="white", outline="blue")

def choix_joueur():
    """choisit aléatoirement le premier des deux joueurs qui va jouer"""
    global premier_joueur, prenom1, prenom2
    prenom1 = input("prénom du joueur 1 ?")
    prenom2 = input("prénom du joueur 2 ?")
    premier_joueur = rd.choice([prenom1, prenom2])

def affiche_joueur():
    """affiche qui doit commencer"""
    choix_joueur()
    label_joueur.config(text= premier_joueur + " commence à jouer")

#def paramètres():
#    nb_pions = int(input("Nombre de pions alignés nécessaire pour gagner ?"))

def trouver_colonne(clic_x):
    """retourne la colonne sur laquelle le jeton va apparaître"""
    colonne = clic_x // 100
    return colonne 

def trouver_ligne(colonne):
    """retourne la ligne sur laquelle le jeton va apparaître"""
    chgt_ligne = m-1
    for i in range(m):
        if grille[chgt_ligne][colonne] == 0 :
            ligne = chgt_ligne
        else:
            chgt_ligne -= 1
    return ligne

def gestion_clic(event):
    """affiche le jeton dans la grille"""
    global joueur1, fin, ligne, colonne
    grille_pleine()
    if fin == True:
        return
    if 0<event.x<W and 0<event.y<H :
        clic_x = event.x
        colonne = trouver_colonne(clic_x)
        ligne = trouver_ligne(colonne)
        if joueur1:
            canvas.create_oval(colonne*100+5, ligne*100+5, colonne*100+100-5, ligne*100+100-5, fill ="yellow")
            grille[ligne][colonne] = 1
            joueur1 = not joueur1
        else:
            canvas.create_oval(colonne*100+5, ligne*100+5, colonne*100+100-5, ligne*100+100-5, fill="red")
            grille[ligne][colonne] = 2
            joueur1 = True
    alignement(ligne, colonne)
    dernier_coup()


def alignement(ligne, colonne):
    """détecte alignement de 4 pions à partir du dernier pion posé"""
    global id_joueur
    id_joueur = grille[ligne][colonne]
    #vertical 
    cpt = 1 #compteur qui part de 1 et qui compte le nombre de pion de même couleur par rapport au dernier pion posé
    while (ligne + cpt < 6) and (grille[ligne+cpt][colonne] == id_joueur):
        cpt += 1
        if cpt == 4:
            fin_du_jeu()

    #horizontal (gauche et droite)
    cpt = 1
    while (colonne - cpt >= 0) and (grille[ligne][colonne - cpt] == id_joueur): #gauche
        cpt += 1
        if cpt == 4:
            fin_du_jeu()
    while (colonne + cpt < 7) and (grille[ligne][colonne + cpt] == id_joueur): #droite
        cpt += 1
        if cpt == 4:
            fin_du_jeu()

    # 2 diagonales (montante vers la droite ou la gauche)
    # montante vers la droite
    cpt = 1
    while (colonne - cpt >=0) and (ligne + cpt < 6) and (grille[ligne + cpt][colonne - cpt] == id_joueur): # bas gauche
        cpt += 1
        if cpt == 4:
            fin_du_jeu()
    while (colonne + cpt < 7) and (ligne - cpt >=0) and (grille[ligne-cpt][colonne + cpt] == id_joueur): # haut droite
        cpt += 1
        if cpt == 4:
            fin_du_jeu()
    # montante vers la gauche
    cpt = 1
    while (colonne + cpt < 7 ) and (ligne + cpt < 6) and (grille[ligne + cpt][colonne + cpt] == id_joueur): # bas droite
        cpt += 1
        if cpt == 4:
            fin_du_jeu()
    while (colonne - cpt >= 0) and (ligne - cpt >=0) and (grille[ligne-cpt][colonne - cpt] == id_joueur): # haut gauche
        cpt += 1
        if cpt == 4:
            fin_du_jeu()
        

def colonne_pleine(colonne):
    """vérifie si la colonne que le joueur a choisie est pleine ou non"""
    for i in range(m):
        if grille[i][colonne] == 0:
                pass

def grille_pleine():
    global nb_pions
    """vérifie si la grille est pleine ou non"""
    nb_pions = 0
    for i in range(m):
        for j in range(n): 
           if grille[i][j] == 1 or grille[i][j] == 2:
               nb_pions += 1
           if nb_pions == n*m:
               fin_du_jeu()


def fin_du_jeu():
    """affiche quel joueur à gagner (s'il y en a un) et arrête le jeu"""
    global fin
    fin = True
    if id_joueur == 1:
        label_gagnant.config(text=" Le gagant est " + premier_joueur)
    elif id_joueur == 2:
        if premier_joueur == prenom1:
            label_gagnant.config(text= prenom2 + " a gagné ", font="20")
        else:
            label_gagnant.config(text= prenom1 + " a gagné", font="20")
    elif nb_pions == n*m:
        label_gagnant.config(text= "Il n'y a aucun gagnant", font="20")

def dernier_coup():
    """rajoute dans une liste les coordonnées du dernier coup """
    l_coup.extend([ligne, colonne])

def retour():
    """annule le dernier coup et change le numéro dans la grille"""
    grille[l_coup[-2]][l_coup[-1]] = 0
    canvas.create_oval(l_coup[-1]*100+5, l_coup[-2]*100+5, l_coup[-1]*100+100-5, l_coup[-2]*100+100-5, fill="white")
    del l_coup[-1]
    del l_coup[-1]

def sauvegarde():
    """ Ecrit la grille dans le fichier sauvegarde.txt """
    fic = open("sauvegarde.txt", "w")
    fic.write(str(grille))
    fic.close() 

def charger():
    """Lit le fichier sauvegarde.txt et met à jour la grille en conséquence (modifie l'affichage)"""
    fic = open("sauvegarde.txt", "r")

    fic.close()
    





    


######################
# programme principal
######################

# création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, height=H, width=W, bg="blue")
bouton_retour = tk.Button(racine, command=retour, text="retour")
bouton_sauvegarde = tk.Button(racine, command=sauvegarde, text="sauvegarde")
label_joueur = tk.Label(racine, text= " puissance 4 ", padx=20, pady=20, borderwidth=5, font = ("helvetica", "20")) 
label_gagnant = tk.Label(racine)

# positionnement des widgets
racine.grid()
canvas.grid(rowspan=10)
bouton_retour.grid(column=1, row=6)
bouton_sauvegarde.grid(column=1, row=7)
label_joueur.grid(column=1,row=0)
label_gagnant.grid(column=1, row=3)

# fonctions
creation_grille()
affiche_joueur()

# gestions clic
canvas.bind("<Button-1>", gestion_clic)


# boucle principale
racine.mainloop()