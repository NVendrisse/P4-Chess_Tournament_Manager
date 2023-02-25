from modules.coloprint import cprint
from tabulate import tabulate


class MainPlay:

    def list_display(list_to_display: list):
        selectors = [i + 1 for i in range(len(list_to_display))]
        for t in range(len(list_to_display)):
            cprint("{} : {}".format(selectors[t], list_to_display[t]))

    def main_title(data):
        return print("Début du tournois : {}".format(data))

    def round_display(nb):
        return print("Round {}".format(nb))

    def play_menu():
        cprint("1- Entrer les scores des matchs")
        cprint("2- Visualiser le classement")
        cprint("3- Retour")

    def scoring_display():
        return "Match {0} - {1}\n1 - {0} gagne le match\n2 - {1} gagne le match\n3 - Match nul"

    def ranking_display(data):
        cols_names = ["Firstname", "Lastname", "Score"]
        cprint(tabulate(data, headers=cols_names, tablefmt="fancy_grid"),
               "bright_red", "black", "bold")

    def error_no_tournament_available():
        return print("Tous les tournois sont terminés, veuillez en créer un nouveau")

    def continue_ask():
        return print("Voulez-vous passer au round suivant ?")
