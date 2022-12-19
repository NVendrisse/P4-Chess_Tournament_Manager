from modules.coloprint import cprint
from tabulate import tabulate


class MainPlay:

    def tournament_list_display(tournament_list:list):
        print(tournament_list)
        columns = ["n°", "Tournament"]
        selectors = [i + 1 for i in range(len(tournament_list))]
        for t in range(len(tournament_list)):
            cprint("{} : {}".format(selectors[t], tournament_list[t]))
        

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
