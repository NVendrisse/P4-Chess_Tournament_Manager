from modules.tournament import Tournament
from views.menus import *
from modules.players import Player
from controllers.manager_controller import Manager
from controllers.saving_controller import Save


class MainMenu:
    def __init__(self) -> None:
        print_main = Menus.main_menu()

    def select(self, selector: int):
        while True:
            try:
                if selector == "1":
                    play_tournament = 1
                elif selector == "2":
                    player_management = PlayersMenu()
                    option_player = player_management.select(
                        input("Selection : "))
                elif selector == "3":
                    tournament_management = TournamentMenu()
                    option_tournament = tournament_management.select(
                        input("Selection : "))
                elif selector == "4":
                    exit()
                else:
                    print("This option is unavailable, please try again")
            except TypeError:
                print("You have entered a wrong selector")


class PlayersMenu:
    def __init__(self) -> None:
        print_playermenu = Menus.players_menu()

    def select(self, selector: int):
        while True:
            try:
                if selector == "1":
                    add_player = PlayerCreation()
                    new_player = add_player.create_new()
                elif selector == "2":
                    view_players = 2
                elif selector == "3":
                    return_back = MainMenu()
                    main_menu_selector = return_back.select(
                        input("Enter your choice : "))
                else:
                    print("This option is unavailable, please try again")
            except TypeError:
                print("You have entered a wrong selector")


class PlayerCreation:
    def __init__(self, players_list=[]) -> None:

        self.players_list = players_list
        print_title = PlayersCreationInteract.player_creation()

    def create_new(self):
        fname = input("Prénom : ")
        lname = input("Nom : ")
        bdate = input("Date de naissance (jj/mm/aaaa) : ")
        genre = input("Genre (M/F/Nc) : ")
        rank = input("Classement : ")
        ##Controle des inputs
        new_player = Player(fname, lname, bdate, genre, rank)
        self.players_list.append(new_player)
        if len(self.players_list)<8:
            print(PlayersCreationInteract.ask_new().format(len(self.players_list)))
            answer=input("Y/n : ")
            if answer=="Y" or answer=="y":
                self.create_new()
            elif answer=="N" or answer=="n":
                player_dict=Manager.serialize_player_list(self.players_list)
                saving_list=Save.export_(player_dict,"players")
                return_back=PlayersMenu()
                back_selector=return_back.select(input("Enter your choice : "))
            else:
                saving_list=Save.export_(self.players_list,"players")
                return_back=PlayersMenu()
                back_selector=return_back.select(input("Enter your choice : "))


class TournamentMenu:
    def __init__(self) -> None:
        print_tournament_menu=Menus.tournament_menu()
    
    def select(self,selector:int):
        while True:
            try:
                if selector == "1":
                    start_tournament=1
                elif selector == "2":
                    create_tournament=2
                elif selector == "3":
                    return_back = MainMenu()
                    main_menu_selector = return_back.select(
                        input("Enter your choice : "))
                else:
                    print("This option is unavailable, please try again")
            except TypeError:
                print("You have entered a wrong selector")

class TournamentCreation:
    def __init__(self) -> None:
        print_title=TournamentCreationInteractive.tournament_creation()

    def create_new(self):
        n=input("Nom : ")
        l=input("Localisation : ")
        dd=input("Date de début : ")
        df=input("Date de fin : ")
        tc=input("Controle de temps : ")
        rm=input("Nombre de tours (4 par défaut) : ")
        d=input("Description : ")
        self.new_tournament=Tournament(n,l,dd,df,tc,d,[],rm,[])
        

    def add_players_list(self,players_list:list):
        self.new_tournament.players=players_list
