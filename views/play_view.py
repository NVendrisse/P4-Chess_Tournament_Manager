from modules.coloprint import cprint
from tabulate import tabulate


class MainPlay:

    def list_display(list_to_display:list):
        selectors = [i + 1 for i in range(len(list_to_display))]
        for t in range(len(list_to_display)):
            cprint("{} : {}".format(selectors[t], list_to_display[t]))
        

    def main_title():
        return "Début du tournois : {}"

    def round_display():
        return "Round {}"

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
