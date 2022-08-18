
class Menus:

    def main_menu():
        print("Tournois d'échecs")
        print("1- Jouer un tournoi")
        print("2- Gestion des joueurs")
        print("3- Gestion des tournois")
        print("4- Quitter")

    def players_menu():
        print("Menu des joueurs")
        print("1- Créer un nouveau joueur")
        print("2- Afficher la liste des joueurs")
        print("3- Retour")

    def tournament_menu():
        print("Menu des Tournois")
        print("1- Jouer un tournois")
        print("2- Créer un tournois")
        print("3- Retour")


class PlayersCreationInteract:

    def player_creation():
        print("Création d'un nouveau joueur")

    def ask_new():
        return "Voulez-vous créer un nouveau joueur?\n({}/8 joueurs créés)"
