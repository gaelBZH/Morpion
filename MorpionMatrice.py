####################################
##                                ##
# Fait le 01/12/2022 par gaelBZH  ##
##                                ##
####################################

# JEU DE MORPION - 1 ou 2 JOUEURS
# A ouvrir de préférence avec Jupyter ou VSCode

from os import name
from os import system
from random import randint
from time import sleep
system('cls' if name == 'nt' else 'clear')
L=[["🟦", "1️⃣", "2️⃣", "3️⃣"],
["1️⃣", "⚫", "⚫", "⚫"],
["2️⃣", "⚫", "⚫", "⚫"],
["3️⃣", "⚫", "⚫", "⚫"]]

Emojis=["❌", "⭕"] # Emojis par Défaut
Forme='  ' # Rectangle
Gagne=False
JeuBon=False
MatchNul=False
Ligne=0
Colonne=0
Tour=Emojis[1] # Joueur qui ne commence pas
Action=None
Multijoueur=None

# FONCTION 1
def gagne():
    """Vérifie toutes les Possibilités de Victoire. Renvoie True ou False selon si il y a un gagnant"""
    if (L[1][1]==Emojis[0] and L[1][2]==Emojis[0] and L[1][3]==Emojis[0])\
    or (L[2][1]==Emojis[0] and L[2][2]==Emojis[0] and L[2][3]==Emojis[0])\
    or (L[3][1]==Emojis[0] and L[3][2]==Emojis[0] and L[3][3]==Emojis[0])\
    or (L[1][1]==Emojis[0] and L[2][1]==Emojis[0] and L[3][1]==Emojis[0])\
    or (L[1][2]==Emojis[0] and L[2][2]==Emojis[0] and L[3][2]==Emojis[0])\
    or (L[1][3]==Emojis[0] and L[2][3]==Emojis[0] and L[3][3]==Emojis[0])\
    or (L[1][1]==Emojis[0] and L[2][2]==Emojis[0] and L[3][3]==Emojis[0])\
    or (L[1][3]==Emojis[0] and L[2][2]==Emojis[0] and L[3][1]==Emojis[0])\
    or (L[1][1]==Emojis[1] and L[1][2]==Emojis[1] and L[1][3]==Emojis[1])\
    or (L[2][1]==Emojis[1] and L[2][2]==Emojis[1] and L[2][3]==Emojis[1])\
    or (L[3][1]==Emojis[1] and L[3][2]==Emojis[1] and L[3][3]==Emojis[1])\
    or (L[1][1]==Emojis[1] and L[2][1]==Emojis[1] and L[3][1]==Emojis[1])\
    or (L[1][2]==Emojis[1] and L[2][2]==Emojis[1] and L[3][2]==Emojis[1])\
    or (L[1][3]==Emojis[1] and L[2][3]==Emojis[1] and L[3][3]==Emojis[1])\
    or (L[1][1]==Emojis[1] and L[2][2]==Emojis[1] and L[3][3]==Emojis[1])\
    or (L[1][3]==Emojis[1] and L[2][2]==Emojis[1] and L[3][1]==Emojis[1]):
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
        for j in range(len(L[0])):
            print("{:^0}".format(L[i][j]), end=Forme)
        print(end='\n')
        
# FONCTION 5
def changertour(Tour):
    """Invese les tours ❌ en ⭕ et ⭕ en ❌. Variable Tour de Base requise. Renvoie le Tour."""
    if Tour==Emojis[0]:
        Tour=Emojis[1]
    elif Tour==Emojis[1]:
        Tour=Emojis[0]
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
    S=[]
    for li in range(1,4):
        for co in range(1,4):
            if L[li][co]=="⚫":
                S.append(True)
            else:
                S.append(False)
    Play=randint(0, 8)
    while S[Play]==False:
        Play=randint(0, 8)
    
    if Play==0 or Play==1 or Play==2:
        L[1][Play+1]=Emojis[1]
    elif Play==3 or Play==4 or Play==5:
        L[2][Play-2]=Emojis[1]
    elif Play==6 or Play==7 or Play==8:
        L[3][Play-5]=Emojis[1]
        
# FONCTION 8
def ordinateur():
    """Fonction qui joue au morpion en bloquant les attaques adverses et en complétant les lignes pour gagner. Renvoie None."""
    S=[]
    for li in range(1,4):
        for co in range(1,4):
            if L[li][co]=="⚫":
                S.append(True)
            else:
                S.append(False)
    
    # Si : (Deux Emojis Différents sur une Ligne) et Case Vide
    if (((S[1]==False and S[2]==False and L[1][2]==L[1][3]) or (S[3]==False and S[6]==False and L[2][1]==L[3][1]) or (S[4]==False and S[8]==False and L[2][2]==L[3][3]))) and L[1][1]=="⚫":
        L[1][1]=Emojis[1]
    elif (((S[0]==False and S[2]==False and L[1][1]==L[1][3]) or (S[4]==False and S[7]==False and L[2][2]==L[3][2]))) and L[1][2]=="⚫":
        L[1][2]=Emojis[1]
    elif (((S[0]==False and S[1]==False and L[1][1]==L[1][2]) or (S[5]==False and S[8]==False and L[2][3]==L[3][3]) or (S[4]==False and S[6]==False and L[2][2]==L[3][2]))) and L[1][3]=="⚫":
        L[1][3]=Emojis[1]
    elif (((S[4]==False and S[5]==False and L[2][2]==L[2][3]) or (S[0]==False and S[6]==False and L[1][1]==L[3][2]))) and L[2][1]=="⚫":
        L[2][1]=Emojis[1]
    elif (((S[3]==False and S[5]==False and L[2][1]==L[2][3]) or (S[1]==False and S[7]==False and L[1][2]==L[3][2]) or (S[0]==False and S[8]==False and L[1][1]==L[3][3]) or (S[2]==False and S[6]==False and L[1][3]==L[3][1]))) and L[2][2]=="⚫":
        L[2][2]=Emojis[1]
    elif (((S[3]==False and S[4]==False and L[2][1]==L[2][2]) or (S[2]==False and S[8]==False and L[1][3]==L[3][3]))) and L[2][3]=="⚫":
        L[2][3]=Emojis[1]
    elif (((S[7]==False and S[8]==False and L[3][2]==L[3][3]) or (S[0]==False and S[3]==False and L[1][1]==L[2][1]) or (S[2]==False and S[4]==False and L[1][3]==L[2][2]))) and L[3][1]=="⚫":
        L[3][1]=Emojis[1]
    elif (((S[6]==False and S[8]==False and L[3][1]==L[3][3]) or (S[1]==False and S[4]==False and L[1][2]==L[2][2]))) and L[3][2]=="⚫":
        L[3][2]=Emojis[1]
    elif (((S[6]==False and S[7]==False and L[3][1]==L[3][2]) or (S[2]==False and S[5]==False and L[1][3]==L[2][3]) or (S[0]==False and S[4]==False and L[1][1]==L[2][2]))) and L[3][3]=="⚫":
        L[3][3]=Emojis[1]
    else:
        ordinateurrandom()


# FONCTION 9
def rules():
    """Fonction qui affiche les règles du Jeu. Renvoie None."""   
    print("""\n❌ Comment jouer au morpion ? ⭕\nPour jouer une partie de morpion, il suffit de tracer sur une grille\nde 3 cases sur 3.\nLe but du jeu est d’aligner avant son adversaire 3 symboles identiques\nhorizontalement, verticalement ou en diagonale.\nChaque joueur a donc son propre symbole, une croix pour l’un et un\nrond pour l’autre. La partie se termine quand l’un des joueurs a aligné 3 symboles ou\nquand la grille est complétée sans vainqueur. Il y a alors égalité.\n\nComment gagner une partie de Morpion ? 🏆\nLe premier joueur à aligner 3 symboles identiques gagne la partie. Attention, le joueur\nqui débute est toujours avantagé pour gagner. Pensez donc à alterner !\n""")

# FONCTION 10
def menu():
    """Fonction qui affiche le Menu. Renvoie l'Action Choisie. [Play-Multi-Rules-Forme-Emojis-Exit]"""   

    Menu=["-----------------", "MENU 🌐", "-----------------", "play - Jouer en Solo (Ordinateur)", "multi - Jouer en mode 2 Joueurs", "rules - Afficher les Règles", "forme - Choisir la Forme de la Grille" , "emojis - Changer les Emojis par Défaut", "exit - Quitter le Jeu"]
    for i in Menu:
        print(i)
    Action=str(input("Séléctionner une Option : "))
    if Action=='play' or Action=='p' or Action=='P' or Action=='Play' or Action=='PLAY' or Action=='Jouer' or Action=='jouer' or Action=='j' or Action=='J':
        Action="Play"
    elif Action=='multi' or Action=='Multi' or Action=='MULTI' or Action=='m' or Action=='M' or Action=='mu' or Action=='Mu' or Action=='MU' or Action=='Multijoueur' or Action=='multijoueur' or Action=='MULTIJOUEUR':
        Action="Multi"
    elif Action=='rules' or Action=='r' or Action=='R' or Action=='Rules' or Action=='RULES' or Action=='Règles' or Action=='règles' or Action=='REGLES' or Action=='regles' or Action=='Regles' or Action=='RÈGLES':
        Action="Rules"
    elif Action=='forme' or Action=='f' or Action=='F' or Action=='Forme' or Action=='FORME':
        Action="Forme"
    elif Action=='Emojis' or Action=='Emoji' or Action=='E' or Action=='e' or Action=='emojis' or Action=='emoji' or Action=='EMOJI' or Action=='EMOJiS':
        Action="Emojis"
    else:
        Action='Exit'
        print("Au Revoir 👋")
    print("-----------------")
    system('cls' if name=='nt' else 'clear')
    return Action

# FONCTION 11
def emojis(Liste):
    """Fonction qui propose à l'utilisateur de changer les emojis. Renvoie None."""   
    print("Emojis Actuels : {} / {}".format(Liste[0], Liste[1]))
    print("-----------------\nDoublons Prédéfinis :\ndefault  - ❌ / ⭕\nbattle   - 🔵 / 🔴\ntropical - 🟡 / 🟢\nfruit    - 🍓 / 🥝\nmeteo    - ☀️  / ❄️\nclassic  -  X /  O\nEnvoyez none pour personaliser les emojis.\n-----------------")
    Doublon=str(input("Doublon : "))
    if Doublon=="d" or Doublon=="D" or Doublon=="default" or Doublon=="defaut" or Doublon=="Default" or Doublon=="Defaut" or Doublon=="DEFAULT" or Doublon=="DEFAUT":
        Liste.pop(0)
        Liste.pop(0)
        Liste.append("❌")
        Liste.append("⭕")
    elif Doublon=="b" or Doublon=="B" or Doublon=="battle "or Doublon=="Battle" or Doublon=="BATTLE":
        Liste.pop(0)
        Liste.pop(0)
        Liste.append("🔵")
        Liste.append("🔴")
    elif Doublon=="t" or Doublon=="T" or Doublon=="tropical" or Doublon=="tropic" or Doublon=="Tropical" or Doublon=="Tropic" or Doublon=="TROPICAL" or Doublon=="TROPIC":
        Liste.pop(0)
        Liste.pop(0)
        Liste.append("🟡")
        Liste.append("🟢")
    elif Doublon=="f" or Doublon=="F" or Doublon=="fruit"or Doublon=="Fruit" or Doublon=="FRUIT" or Doublon=="fruits" or Doublon=="FRUITS" or Doublon=="Fruits":
        Liste.pop(0)
        Liste.pop(0)
        Liste.append("🍓")
        Liste.append("🥝")
    elif Doublon=="m" or Doublon=="M" or Doublon=="meteo" or Doublon=="météo" or Doublon=="Météo" or Doublon=="Meteo" or Doublon=="METEO" or Doublon=="MÉTÉO":
        Liste.pop(0)
        Liste.pop(0)
        Liste.append("☀️")
        Liste.append("❄️")
    elif Doublon=="c" or Doublon=="C" or Doublon=="classic" or Doublon=="classique" or Doublon=="Classic" or Doublon=="Classique" or Doublon=="CLASSIC" or Doublon=="CLASSIQUE":
        Liste.pop(0)
        Liste.pop(0)
        Liste.append("X")
        Liste.append("O")
    else:
        for i in range(2):
            temp=str(input("Emoji {} : [cancel pour ne pas changer]".format(i+1)))
            if temp!='cancel' and temp!='Cancel':
                Liste[i]=temp
    print("Nouveux Emojis : {} / {}".format(Liste[0], Liste[1]))

# FONCTION 12
def findujeu():
    """Fonction qui Adapte la fin du jeu en fonction des actions qui ont été faites précédemment. Renvoie None."""
    if Multijoueur!=None:
        affichertableau()
        if MatchNul==False:
            print("Le Joueur {} a gagné la partie !".format(Tour))
        else:
            print("Match Nul ! Vous avez fait égalité !")

    if Action=='Rules':
        print("------------")
        print("Vous allez être renvoyé au Menu dans 15 sec")
        sleep(15)
        print(" "), print(" "), print(" "), print("-----------------------------------------------------------"), print(" "), print(" "), print(" ")
    elif Action!="Exit":
        print("------------")
        print("Vous allez être renvoyé au Menu dans 5 sec")
        sleep(5)
        print(" "), print(" "), print(" "), print("-----------------------------------------------------------"), print(" "), print(" "), print(" ")

while Action!='Exit':
    Action=menu()
    if Action=="Play":
        Multijoueur=False
    elif Action=="Multi":
        Multijoueur=True
    else:
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
            if Tour==Emojis[0]:
                while JeuBon==False and MatchNul==False: # Tant que : Jeu Correct sans Match Nul
                    Ligne=ligne() # Demander Ligne
                    Colonne=colonne() # Demander Colonne

                    JeuBon=jouer(Ligne, Colonne, Tour) # Joue selon les valeurs entrées, retourne True si le jeu est bon, False s'il est mauvais
                    if JeuBon==False:
                        print("Jeu Incorrect : Cette case a dejà été jouée")
                        Ligne=0
                        Colonne=0
                    Gagne=gagne() # Renvoie True ou False si le jeu est terminé
            elif Tour==Emojis[1]:
                print("Jeu de l'Ordinateur ...")
                sleep(1)
                ordinateur() # Fait jouer l'ordinateur. Renvoie None.
                Gagne=gagne() # Renvoie True ou False si le jeu est terminé

            JeuBon=False
            MatchNul=matchnul() # Renvoie True ou False si il ya match nul
            
            print(" "), print("------------------------------------"), print(" ")
    if Action=="Forme":
        print("Exemple de Rectangle :\n🟦  1️⃣  2️⃣  3️⃣\n1️⃣  ❌  ⭕  ❌\n2️⃣  ⭕  ⭕  ❌\n3️⃣  ❌  ❌  ⭕\n\nExemple de Carré :\n🟦1️⃣2️⃣3️⃣\n1️⃣❌⭕❌\n2️⃣❌⭕❌\n3️⃣⭕❌⭕")
        Forme=str(input("Choisir la Forme de la Grille [Carré-Rectangle]"))
        if Forme=='Carré' or Forme=='CARRÉ' or Forme=='carré' or Forme=='Carre' or Forme=='CARRE' or Forme=='carre' or Forme=='C' or Forme=='c':
            Forme=''
        else:
            Forme='  '
    if Action=="Rules":
        rules()
    if Action=="Emojis":
        emojis(Emojis)
    findujeu()

    # Réinistialisation des Variables.
    system('cls' if name == 'nt' else 'clear')
    L=[["🟦", "1️⃣", "2️⃣", "3️⃣"], ["1️⃣", "⚫", "⚫", "⚫"], ["2️⃣", "⚫", "⚫", "⚫"], ["3️⃣", "⚫", "⚫", "⚫"]]
    Gagne=False
    JeuBon=False
    MatchNul=False
    Ligne=0
    Colonne=0
    Tour=Emojis[1] # Joueur qui ne commence pas
    Multijoueur=None
