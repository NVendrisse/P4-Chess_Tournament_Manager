from views.menus import *
from modules.players import Player
from controllers.manager_controller import Manager


class MainMenu:
    def __init__(self) -> None:
        print_main = Menus.main_menu()

    def select(self, selector: int):
        while True:
            try:
                if selector == "1":
                    play_tournament = 1
                elif selector == "2":
                    tournament_management = PlayersMenu()
                    option_tournament = tournament_management.select(
                        input("Selection : "))
                elif selector == "3":
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
        new_player = Player(fname, lname, bdate, genre, rank)
        self.players_list.append(new_player)
        if len(self.players_list)<8:
            print(PlayersCreationInteract.ask_new().format(len(self.players_list)))
            answer=input("Y/n : ")
            if answer=="Y" or answer=="y":
                self.create_new()
            else:
                return_back=PlayersMenu()
                back_selector=return_back.select(input("Enter your choice : "))

