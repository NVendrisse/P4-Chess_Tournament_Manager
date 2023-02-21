from modules.coloprint import cprint
from tabulate import tabulate
from modules.tournament import Tournament


class Menus:

    def splash_screen(splash: str):
        cprint(splash, "bright_white", "black")

    def main_menu(print_play: bool, print_tournament: bool):
        cprint("Tournois d'échecs", "black", "bright_green")
        cprint("1- Jouer un tournoi", foreground_color=("bright_red" if not print_play else "bright_white"),
               attribute=("italic" if not print_play else "None"))
        cprint("2- Gestion des joueurs")
        cprint("3- Gestion des tournois", foreground_color=("bright_red" if not print_tournament else "bright_white"),
               attribute=("italic" if not print_tournament else "None"))
        cprint("4- Quitter et générer un rapport sur le programme")

    def players_menu():
        cprint("Menu des joueurs", "black", "bright_green")
        cprint("1- Créer une nouvelle liste de joueurs")
        cprint("2- Afficher la liste des joueurs")
        cprint("3- Ajouter de nouveaux joueurs à la liste actuelle")
        cprint("4- Retour")

    def tournament_menu():
        cprint("Menu des Tournois", "black", "bright_green")
        cprint("1- Créer un tournois")
        cprint("2- Visualisation des tournois")
        cprint("3- Retour")


class PlayersCreationInteract:

    def player_creation():
        cprint("Création d'un nouveau joueur", "black", "cyan", "italic")

    def ask_new():
        return "Voulez-vous créer un nouveau joueur?\n({}/8 joueurs créés)"


class TournamentCreationInteractive:

    def tournament_creation():
        cprint("Création d'un nouveau Tournoi", "black", "yellow")

    def tournament_add_player_menu():
        return "Gestion des joueurs du tournois : {}"


class PlayersDisplay:

    def menu():
        cprint("Affichage des joueurs", "black", "bright_magenta")
        print("1- Classé par nom")
        print("2- Classé par rang")
        print("3- Retour")

    def table(data):
        cols_names = ["Firstname", "Lastname",
                      "Birthdate", "Genre", "Rank", "Score"]
        cprint(tabulate(data, headers=cols_names, tablefmt="fancy_grid"),
               "bright_red", "black", "bold")


class TournamentDisplay:
    def display(data: Tournament):
        cprint(data.name)
        cprint("Début : {} ({})| Fin : {} ({})".format(
            data.start_date, data.start, data.end_date, data.stop))
        cprint("Lieux : {}".format(data.location))
        for i in data.turn:
            cprint(i[0])
            for j in i[1]:
                cprint(tabulate(j, tablefmt="fancy_grid"))
