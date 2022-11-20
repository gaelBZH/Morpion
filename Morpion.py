####################################
##                                ##
# Fait le 19/11/2022 par gaelBZH  ##
##                                ##
####################################

from os import name
from os import system
L0=["1️⃣ ", "2️⃣ ", "3️⃣ "]
L1=["⚫", "⚫", "⚫"]
L2=["⚫", "⚫", "⚫"]
L3=["⚫", "⚫", "⚫"]
Gagne=False
JeuBon=False
MatchNul=False
Ligne=0
Colonne=0
Tour="⭕" # Joueur qui ne commence pas
while Gagne==False and MatchNul==False:
    system('cls' if name == 'nt' else 'clear')
    print("🟦{}".format(L0)), print("1️⃣", L1), print("2️⃣", L2), print("3️⃣", L3)
    if Tour=="❌":
        Tour="⭕"
    elif Tour=="⭕":
        Tour="❌"
    
    while JeuBon==False and MatchNul==False:
        while Ligne!=1 and Ligne!=2 and Ligne!=3:
            Ligne=int(input("[{}] Ligne=".format(Tour)))
        while Colonne!=1 and Colonne!=2 and Colonne!=3:
            Colonne=int(input("[{}] Colonne=".format(Tour)))
    
        if (Ligne==1):
            if L1[Colonne-1]=="⚫":   
                JeuBon=True
                if Tour=="❌":
                    if Ligne==1:
                        L1.pop(Colonne-1)
                        L1.insert(Colonne-1, "❌")
                    if Ligne==2:
                        L2.pop(Colonne-1)
                        L2.insert(Colonne-1, "❌")
                    if Ligne==3:
                        L3.pop(Colonne-1)
                        L3.insert(Colonne-1, "❌")
                if Tour=="⭕":
                    if Ligne==1:
                        L1.pop(Colonne-1)
                        L1.insert(Colonne-1, "⭕")
                    if Ligne==2:
                        L2.pop(Colonne-1)
                        L2.insert(Colonne-1, "⭕")
                    if Ligne==3:
                        L3.pop(Colonne-1)
                        L3.insert(Colonne-1, "⭕")
    
        if (Ligne==2):
            if L2[Colonne-1]=="⚫":   
                JeuBon=True
                if Tour=="❌":
                    if Ligne==1:
                        L1.pop(Colonne-1)
                        L1.insert(Colonne-1, "❌")
                    if Ligne==2:
                        L2.pop(Colonne-1)
                        L2.insert(Colonne-1, "❌")
                    if Ligne==3:
                        L3.pop(Colonne-1)
                        L3.insert(Colonne-1, "❌")
                if Tour=="⭕":
                    if Ligne==1:
                        L1.pop(Colonne-1)
                        L1.insert(Colonne-1, "⭕")
                    if Ligne==2:
                        L2.pop(Colonne-1)
                        L2.insert(Colonne-1, "⭕")
                    if Ligne==3:
                        L3.pop(Colonne-1)
                        L3.insert(Colonne-1, "⭕")
        
        if (Ligne==3):
            if L3[Colonne-1]=="⚫":   
                JeuBon=True
                if Tour=="❌":
                    if Ligne==1:
                        L1.pop(Colonne-1)
                        L1.insert(Colonne-1, "❌")
                    if Ligne==2:
                        L2.pop(Colonne-1)
                        L2.insert(Colonne-1, "❌")
                    if Ligne==3:
                        L3.pop(Colonne-1)
                        L3.insert(Colonne-1, "❌")
                if Tour=="⭕":
                    if Ligne==1:
                        L1.pop(Colonne-1)
                        L1.insert(Colonne-1, "⭕")
                    if Ligne==2:
                        L2.pop(Colonne-1)
                        L2.insert(Colonne-1, "⭕")
                    if Ligne==3:
                        L3.pop(Colonne-1)
                        L3.insert(Colonne-1, "⭕")
        if JeuBon==False:
            print("Jeu Incorrect : Cette case a dejà été jouée")
            Ligne=0
            Colonne=0

    # Si 3 "❌" alignés horizontalement ; Si 3 "❌" alignés verticalement ; Si 3 "❌" alignés diagonalement
    # Si 3 "⭕" alignés horizontalement ; Si 3 "⭕" alignés verticalement ; Si 3 "⭕" alignés diagonalement
    # -1 veut dire qu'on prend l'élement avant dans la liste (1,2,3 devient 0,1,2 en Python)
    if (L1[1 -1]=="❌" and L1[2-1]=="❌" and L1[3-1]=="❌") or (L2[1-1]=="❌" and L2[2-1]=="❌" and L2[3-1]=="❌") or (L3[1-1]=="❌" and L3[2-1]=="❌" and L3[3-1]=="❌")\
    or (L1[1 -1]=="❌" and L2[1-1]=="❌" and L3[1-1]=="❌") or (L1[2-1]=="❌" and L2[2-1]=="❌" and L3[2-1]=="❌") or (L1[3-1]=="❌" and L2[3-1]=="❌" and L3[3-1]=="❌")\
    or (L1[1 -1]=="❌" and L2[2-1]=="❌" and L3[3-1]=="❌") or (L1[3-1]=="❌" and L2[2-1]=="❌" and L3[1-1]=="❌")\
    or (L1[1 -1]=="⭕" and L1[2-1]=="⭕" and L1[3-1]=="⭕") or (L2[1-1]=="⭕" and L2[2-1]=="⭕" and L2[3-1]=="⭕") or (L3[1-1]=="⭕" and L3[2-1]=="⭕" and L3[3-1]=="⭕")\
    or (L1[1 -1]=="⭕" and L2[1-1]=="⭕" and L3[1-1]=="⭕") or (L1[2-1]=="⭕" and L2[2-1]=="⭕" and L3[2-1]=="⭕") or (L1[3-1]=="⭕" and L2[3-1]=="⭕" and L3[3-1]=="⭕")\
    or (L1[1 -1]=="⭕" and L2[2-1]=="⭕" and L3[3-1]=="⭕") or (L1[3-1]=="⭕" and L2[2-1]=="⭕" and L3[1-1]=="⭕"):
        Gagne=True
    Ligne=0
    Colonne=0
    JeuBon=False
    if Gagne==False and (L1[1-1]=="❌" or L1[1-1]=="⭕") and (L1[2-1]=="❌" or L1[2-1]=="⭕") and (L1[3-1]=="❌" or L1[3-1]=="⭕") and (L2[1-1]=="❌" or L2[1-1]=="⭕") and (L2[2-1]=="❌" or L2[2-1]=="⭕") and (L2[3-1]=="❌" or L2[3-1]=="⭕") and (L3[1-1]=="❌" or L3[1-1]=="⭕") and (L3[2-1]=="❌" or L3[2-1]=="⭕") and (L3[3-1]=="❌" or L3[3-1]=="⭕"):
        MatchNul=True
system('cls' if name == 'nt' else 'clear')
print(" ", L0), print("1️⃣", L1), print("2️⃣", L2), print("3️⃣", L3)
if MatchNul==False:
    print("Le Joueur {} a gagné la partie !".format(Tour))
else:
    print("Match Nul ! Vous avez fait égalité !")