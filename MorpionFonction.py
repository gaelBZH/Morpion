####################################
##                                ##
# Fait le 01/12/2022 par gaelBZH  ##
##                                ##
####################################

# JEU DE MORPION - 2 JOUEURS

from os import name
from os import system
L0=["1️⃣", "2️⃣", "3️⃣"]
L1=["⚫", "⚫", "⚫"]
L2=["⚫", "⚫", "⚫"]
L3=["⚫", "⚫", "⚫"]
Gagne=False
JeuBon=False
MatchNul=False
Ligne=0
Colonne=0
Tour="⭕" # Joueur qui ne commence pas

# FONCTION 1
def gagne():
    """Vérifie toutes les Possibilités de Victoire. Renvoie True ou False selon si il y a un gagnant"""
    if (L1[1 -1]=="❌" and L1[2-1]=="❌" and L1[3-1]=="❌") or (L2[1-1]=="❌" and L2[2-1]=="❌" and L2[3-1]=="❌") or (L3[1-1]=="❌" and L3[2-1]=="❌" and L3[3-1]=="❌")    or (L1[1 -1]=="❌" and L2[1-1]=="❌" and L3[1-1]=="❌") or (L1[2-1]=="❌" and L2[2-1]=="❌" and L3[2-1]=="❌") or (L1[3-1]=="❌" and L2[3-1]=="❌" and L3[3-1]=="❌")    or (L1[1 -1]=="❌" and L2[2-1]=="❌" and L3[3-1]=="❌") or (L1[3-1]=="❌" and L2[2-1]=="❌" and L3[1-1]=="❌")    or (L1[1 -1]=="⭕" and L1[2-1]=="⭕" and L1[3-1]=="⭕") or (L2[1-1]=="⭕" and L2[2-1]=="⭕" and L2[3-1]=="⭕") or (L3[1-1]=="⭕" and L3[2-1]=="⭕" and L3[3-1]=="⭕")    or (L1[1 -1]=="⭕" and L2[1-1]=="⭕" and L3[1-1]=="⭕") or (L1[2-1]=="⭕" and L2[2-1]=="⭕" and L3[2-1]=="⭕") or (L1[3-1]=="⭕" and L2[3-1]=="⭕" and L3[3-1]=="⭕")    or (L1[1 -1]=="⭕" and L2[2-1]=="⭕" and L3[3-1]=="⭕") or (L1[3-1]=="⭕" and L2[2-1]=="⭕" and L3[1-1]=="⭕"):
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
    L=["🟦 {}".format(L0), "1️⃣ {}".format(L1), "2️⃣ {}".format(L2), "3️⃣ {}".format(L3)] # Créer un tableau à partir des Lignes
    for i in L:
        print(i)
        
# FONCTION 5
def changertour(Tour):
    """Invese les tours X en O et O en X. Variable Tour de Base requise. Renvoie le Tour."""
    if Tour=="❌":
        Tour="⭕"
    elif Tour=="⭕":
        Tour="❌"
    return Tour

# FONCTION 6
def jouer(Ligne, Colonne, Tour):
    """Place l'emoji du Joueur sur la case de coordonnées (Ligne, Colonne).
    Renvoie True ou False, ce booléen représente si la case jouée est correcte (n'a pas déjà été jouée.)"""
    if (Ligne==1):
        if L1[Colonne-1]=="⚫":   
            L1[Colonne-1]=Tour
            return True
        else:
            return False

    elif (Ligne==2):
        if L2[Colonne-1]=="⚫":   
            L2[Colonne-1]=Tour
            return True
        else:
            return False
        
    elif (Ligne==3):
        if L3[Colonne-1]=="⚫":   
            L3[Colonne-1]=Tour
            return True
        else:
            return False

# FONCTION 7
def matchnul():
    """Vérifie si la Grille est pleine et qu'il y a Match Nul. Renvoie True ou False."""
    if Gagne==False and ("⚫" not in L1) and ("⚫" not in L2) and ("⚫" not in L3): # Si personne n'a gagné et grille pleine
        return True # Alors Match Nul
    else:
        return False
        

        
        
        
        
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
    
    
    
# FIN DU JEU
affichertableau()
if MatchNul==False:
    print("Le Joueur {} a gagné la partie !".format(Tour))
else:
    print("Match Nul ! Vous avez fait égalité !")
