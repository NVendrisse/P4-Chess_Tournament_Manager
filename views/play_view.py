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
    
    