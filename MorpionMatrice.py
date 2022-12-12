####################################
##                                ##
# Fait le 01/12/2022 par gaelBZH  ##
##                                ##
####################################

# JEU DE MORPION - 2 JOUEURS

from os import name
from os import system
from random import randint
from time import sleep
from Module.py import *
system('cls' if name == 'nt' else 'clear')
L=["🟦", "1️⃣", "2️⃣", "3️⃣"],
  ["1️⃣", "⚫", "⚫", "⚫"],
  ["2️⃣", "⚫", "⚫", "⚫"],
  ["3️⃣", "⚫", "⚫", "⚫"]
Gagne=False
JeuBon=False
MatchNul=False
Ligne=0
Colonne=0
Tour="⭕" # Joueur qui ne commence pas
# FONCTION 1
def gagne():
    """Vérifie toutes les Possibilités de Victoire. Renvoie True ou False selon si il y a un gagnant"""
    if (L[1][1]=="❌" and L[1][2]=="❌" and L[1][3]=="❌")\
    or (L[2][1]=="❌" and L[2][2]=="❌" and L[2][3]=="❌")\
    or (L[3][1]=="❌" and L[3][2]=="❌" and L[3][3]=="❌")\
    or (L[1][1]=="❌" and L[2][1]=="❌" and L[3][1]=="❌")\
    or (L[1][2]=="❌" and L[2][2]=="❌" and L[3][2]=="❌")\
    or (L[1][3]=="❌" and L[2][3]=="❌" and L[3][3]=="❌")\
    or (L[1][1]=="❌" and L[2][2]=="❌" and L[3][3]=="❌")\
    or (L[1][3]=="❌" and L[2][2]=="❌" and L[3][1]=="❌")\

    or (L[1][1]=="⭕" and L[1][2]=="⭕" and L[1][3]=="⭕")\
    or (L[2][1]=="⭕" and L[2][2]=="⭕" and L[2][3]=="⭕")\
    or (L[3][1]=="⭕" and L[3][2]=="⭕" and L[3][3]=="⭕")\
    or (L[1][1]=="⭕" and L[2][1]=="⭕" and L[3][1]=="⭕")\
    or (L[1][2]=="⭕" and L[2][2]=="⭕" and L[3][2]=="⭕")\
    or (L[1][3]=="⭕" and L[2][3]=="⭕" and L[3][3]=="⭕")\
    or (L[1][1]=="⭕" and L[2][2]=="⭕" and L[3][3]=="⭕")\
    or (L[1][3]=="⭕" and L[2][2]=="⭕" and L[3][1]=="⭕")\
        return True
    else:
        return False

# FONCTION 2
def colonne():
    """Demande la Colonne à l'Utilisateur Tant qu'elle n'est pas correcte. Renvoie le numéro de colonne."""
    Colonne=0
    c=0
    while c!=1 and c!=2 and c!=3:
        c=int(input("[{}] Colonne=".format(Tour)))
    return c

# FONCTION 3
def ligne():
    """Demande la Ligne à l'Utilisateur Tant qu'elle n'est pas correcte. Renvoie le numéro de ligne."""
    Ligne=0
    l=0
    while l!=1 and l!=2 and l!=3:
        l=int(input("[{}] Ligne=".format(Tour)))
    return l
        
# FONCTION 4
def affichertableau():
    """Affiche la Grille Actuelle du Morpion. Renvoie None."""
    for i in range(len(L)):
        for j in range(len(T[0])):
            print("{:^10}".format(L[i][j]), end=' ')
        print(end='\n')
        
# FONCTION 5
def changertour(Tour):
    """Invese les tours ❌ en ⭕ et ⭕ en ❌. Variable Tour de Base requise. Renvoie le Tour."""
    if Tour=="❌":
        Tour="⭕"
    elif Tour=="⭕":
        Tour="❌"
    return Tour

# FONCTION 6
def jouer(Ligne, Colonne, Tour):
    """Place l'emoji du Joueur sur la case de coordonnées (Ligne, Colonne).
    Renvoie True ou False, ce booléen représente si la case jouée est correcte (n'a pas déjà été jouée.)"""
    if L[Ligne][Colonne]=="⚫":
        L[Ligne][Colonne]=Tour
        return True
    else:
        return False

# FONCTION 7
def matchnul():
    """Vérifie si la Grille est pleine et qu'il y a Match Nul. Renvoie True ou False."""
    if Gagne==False and ("⚫" not in L[1]) and ("⚫" not in L[2]) and ("⚫" not in L[3]): # Si personne n'a gagné et grille pleine
        return True # Alors Match Nul
    else:
        return False
        
# FONCTION 8
def ordinateurrandom():
    """Fonction qui joue au morpion aléatoirement. Renvoie None."""
    S=[] # Ensemble des Solutions Jouables
    for i in range(3):
        if L[1][i]=="⚫":
            S.append(1)
        else:
            S.append(0)
    for i in range(3):
        if L[2][i]=="⚫":
            S.append(1)
        else:
            S.append(0)
    for i in range(3):
        if L[3][i]=="⚫":
            S.append(1)
        else:
            S.append(0)
    Play=randint(0, 8)
    while S[Play]!=1:
        Play=randint(0, 8)
    if Play==0 or Play==1 or Play==2:
        L[1][Play]="⭕"
    elif Play==3 or Play==4 or Play==5:
        L[2][Play-3]="⭕"
    elif Play==6 or Play==7 or Play==8:
        L[3][Play-6]="⭕"
    print(Play)

# FONCTION 9
def rules():
    """Fonction qui affiche les règles du Jeu. Renvoie None."""   
    print("""Comment jouer au morpion ?\nPour jouer une partie de morpion, il suffit de tracer sur une grille\nde 3 cases sur 3 (selon les variantes, il est possible d’augmenter le nombre de cases).\nLe but du jeu est d’aligner avant son adversaire 3 symboles identiques\nhorizontalement, verticalement ou en diagonale.\nChaque joueur a donc son propre symbole, une croix pour l’un et un\nrond pour l’autre. La partie se termine quand l’un des joueurs à aligné 3 symboles ou\nquand la grille est complétée sans vainqueur. Il y a alors égalité.\n\nComment gagner une partie de Morpion ?\nLe premier joueur à aligner 3 symboles identiques gagne la partie. Attention, le joueur\nqui débute est toujours avantagé pour gagner. Pensez donc à alterner !""")

# FONCTION 10
def menu():
    """Fonction qui affiche le Menu. Renvoie l'Action Choisie. [Play-Multi-Rules]"""   

    Menu=["-----------------", "MENU 🌐", "-----------------", "play - Jouer en Solo", "multi - Jouer en mode 2 Joueurs", "rules - Afficher les Règles" ,"exit - Quitter le Jeu"]
    for i in Menu:
        print(i)
    Action=str(input("Séléctionner une Option : "))
    if Action=='play' or Action=='p' or Action=='P' or Action=='Play' or Action=='PLAY' or Action=='Jouer' or Action=='jouer' or Action=='j' or Action=='J':
        Action="Play"
    elif Action=='multi' or Action=='Multi' or Action=='MULTI' or Action=='m' or Action=='M' or Action=='mu' or Action=='Mu' or Action=='MU' or Action=='Multijoueur' or Action=='multijoueur' or Action=='MULTIJOUEUR':
        Action="Multi"
    elif Action=='rules' or Action=='r' or Action=='R' or Action=='Rules' or Action=='RULES' or Action=='Règles' or Action=='règles' or Action=='REGLES' or Action=='regles' or Action=='Regles' or Action=='RÈGLES':
        Action="Rules"
    else:
        print("Au Revoir 👋")
        exit()
    print("-----------------")
    system('cls' if name=='nt' else 'clear')
    return Action

  
Action=menu()
if Action=="Play":
    Multijoueur=False
elif Action=="Multi":
    Multijoueur=True
elif Action=="Rules":
    Multijoueur=None

if Multijoueur==True:        
# Tant que : match non nul et aucun gagnant
    while matchnul()==False and Gagne==False: # Joue tant que le jeu n'est pas fini


        affichertableau() # Afficher la Grille
        Tour=changertour(Tour) # Changer de Joueur à partir du Joueur actuel

        while JeuBon==False and MatchNul==False: # Tant que : Jeu Correct sans Match Nul
            Ligne=ligne() # Demander Ligne
            Colonne=colonne() # Demander Colonne

            JeuBon=jouer(Ligne, Colonne, Tour) # Joue selon les valeurs entrées, retourne True si le jeu est bon, False s'il est mauvais
            if JeuBon==False:
                print("Jeu Incorrect : Cette case a dejà été jouée")
                Ligne=0
                Colonne=0
            Gagne=gagne() # Renvoie True ou False si le jeu est terminé
        JeuBon=False
        MatchNul=matchnul() # Renvoie True ou False si il ya match nul
        print(" "), print("------------------------------------"), print(" ")


if Multijoueur==False:   
    while matchnul()==False and Gagne==False: # Joue tant que le jeu n'est pas fini


        affichertableau() # Afficher la Grille
        Tour=changertour(Tour) # Changer de Joueur à partir du Joueur actuel
        if Tour=="❌":
            while JeuBon==False and MatchNul==False: # Tant que : Jeu Correct sans Match Nul
                Ligne=ligne() # Demander Ligne
                Colonne=colonne() # Demander Colonne

                JeuBon=jouer(Ligne, Colonne, Tour) # Joue selon les valeurs entrées, retourne True si le jeu est bon, False s'il est mauvais
                if JeuBon==False:
                    print("Jeu Incorrect : Cette case a dejà été jouée")
                    Ligne=0
                    Colonne=0
                Gagne=gagne() # Renvoie True ou False si le jeu est terminé
        elif Tour=="⭕":
            print("Jeu de l'Ordinateur ...")
            sleep(1)
            ordinateurrandom() # Fait jouer l'ordinateur. Renvoie None.
            Gagne=gagne() # Renvoie True ou False si le jeu est terminé

        JeuBon=False
        MatchNul=matchnul() # Renvoie True ou False si il ya match nul
        print(" "), print("------------------------------------"), print(" ")

if Action=="Rules":
    rules()

# FIN DU JEU
if Multijoueur!=None:
    affichertableau()
    if MatchNul==False:
        print("Le Joueur {} a gagné la partie !".format(Tour))
    else:
        print("Match Nul ! Vous avez fait égalité !")
