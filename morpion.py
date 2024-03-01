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


def main():
    taille_plateau = int(input("Choisissez la taille du plateau : "))
    plateau = creer_plateau(taille_plateau)
    symboles = ['X', 'O']
    tour = 0

    while True:
        affichage_plateau(plateau)
        joueur = symboles[tour % 2]
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
                    tour = tour + 1
                else:
                    print("Cette case est déjà occupée")
            else:
                print("Choisissez une case dans le plateau")
        except ValueError:
            print("Entrez les coordonnées sous la forme (ligne colonne), ex: 1 2")

main()


