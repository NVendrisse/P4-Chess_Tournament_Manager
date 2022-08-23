from modules.coloprint import cprint
class Menus:

    def main_menu():
        cprint("Tournois d'échecs","black","bright_green")
        cprint("1- Jouer un tournoi")
        cprint("2- Gestion des joueurs")
        cprint("3- Gestion des tournois")
        cprint("4- Quitter")

    def players_menu():
        cprint("Menu des joueurs","black","bright_green")
        cprint("1- Créer un nouveau joueur")
        cprint("2- Afficher la liste des joueurs")
        cprint("3- Retour")

    def tournament_menu():
        cprint("Menu des Tournois","black","bright_green")
        cprint("1- Jouer un tournois")
        cprint("2- Créer un tournois")
        cprint("3- Retour")


class PlayersCreationInteract:

    def player_creation():
        print("Création d'un nouveau joueur")

    def ask_new():
        return "Voulez-vous créer un nouveau joueur?\n({}/8 joueurs créés)"

class TournamentCreationInteractive:

    def tournament_creation():
        cprint("Création d'un nouveau Tournoi","black","yellow")
    
    def tournament_add_player_menu():
        return "Gestion des joueurs du tournois : {}"

        