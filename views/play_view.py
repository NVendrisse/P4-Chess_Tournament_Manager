from modules.coloprint import cprint

class MainPlay:
    
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
    
    