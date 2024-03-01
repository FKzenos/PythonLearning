
def affichage_plateau(plateau):
    for ligne in plateau:
        print(' | '.join(ligne))
        print('-' * (4 * len(ligne) - 1))


def winEvent(plateau, symbole):
    taille = len(plateau)

    for i in range(taille):
        if all(plateau[i][j] == symbole for j in range(taille)) or all(plateau[j][i] == symbole for j in range(taille)):
            return True
    if all(plateau[i][i] == symbole for i in range(taille)) or all(
            plateau[i][taille - 1 - i] == symbole for i in range(taille)):
        return True

    return False


def creer_plateau(taille):
    return [[' ' for _ in range(taille)] for _ in range(taille)]

def tour_ordi(plateau, symbole): # action de l'ordi
    taille = len(plateau)

    # Vérifier s'il peut gagner en complétant une ligne
    for i in range(taille):
        if plateau[i].count(symbole) == taille - 1 and ' ' in plateau[i]:
            colonne = plateau[i].index(' ')
            plateau[i][colonne] = symbole
            return

    # Vérifier s'il peut gagner en complétant une colonne
    for j in range(taille):
        colonne = [plateau[i][j] for i in range(taille)]
        if colonne.count(symbole) == taille - 1 and ' ' in colonne:
            ligne = colonne.index(' ')
            plateau[ligne][j] = symbole
            return

    # Vérifier s'il peut gagner en complétant la diagonale
    diagonal1 = [plateau[i][i] for i in range(taille)]
    if diagonal1.count(symbole) == taille - 1 and ' ' in diagonal1:
        index = diagonal1.index(' ')
        plateau[index][index] = symbole
        return

    # Vérifier s'il peut gagner en complétant la diagonale opposée
    diagonal2 = [plateau[i][taille - 1 - i] for i in range(taille)]
    if diagonal2.count(symbole) == taille - 1 and ' ' in diagonal2:
        index = diagonal2.index(' ')
        plateau[index][taille - 1 - index] = symbole
        return

    # Si aucune opportunité de gagner, choisir la première case vide trouvée
    for i in range(taille):
        for j in range(taille):
            if plateau[i][j] == ' ':
                plateau[i][j] = symbole
                return

def rejouer():
    choix = input("Voulez-vous rejouer ? (Oui/Non): ").lower()
    if choix == "oui":
        return True

def main():
    while True:
        taille_plateau = int(input("Choisissez la taille du plateau : "))
        plateau = creer_plateau(taille_plateau)
        symboles = ['X', 'O']
        tour = 0

        while True:
            affichage_plateau(plateau)

            if tour % 2 == 0:
                joueur = symboles[0]
                choix = input(f"Joueur {joueur}, choisissez une case (ligne colonne) : ")

                try:
                    ligne, colonne = map(int, choix.split())
                    if 1 <= ligne <= taille_plateau and 1 <= colonne <= taille_plateau:
                        if plateau[ligne - 1][colonne - 1] == ' ':
                            plateau[ligne - 1][colonne - 1] = joueur
                            if winEvent(plateau, joueur):
                                affichage_plateau(plateau)
                                print(f"Le joueur {joueur} a gagné !")
                                break
                            elif all(plateau[i][j] != ' ' for i in range(taille_plateau) for j in range(taille_plateau)):
                                affichage_plateau(plateau)
                                print("Match nul !")
                                break
                            tour += 1
                        else:
                            print("Cette case est déjà occupée")
                    else:
                        print("Choisissez une case dans le plateau")
                except ValueError:
                    print("Entrez les coordonnées sous la forme (ligne colonne), ex: 1 2")
            else:
                joueur = symboles[1]
                print(f"Tour de l'ordinateur ({joueur}) :")
                tour_ordi(plateau, joueur)
                if winEvent(plateau, joueur):
                    affichage_plateau(plateau)
                    print(f"L'ordinateur ({joueur}) a gagné !")
                    break
                elif all(plateau[i][j] != ' ' for i in range(taille_plateau) for j in range(taille_plateau)):
                    affichage_plateau(plateau)
                    print("Match nul !")
                    break
                tour += 1

        if not rejouer():
            break

main()
