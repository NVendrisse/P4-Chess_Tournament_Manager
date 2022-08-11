from views.menus import *


class MainMenu:
    def __init__(self) -> None:
        print_main = main_menu()

    def select(self, selector: int):
        while True:
            try:
                if selector == "1":
                    play_tournament = 1
                elif selector == "2":
                    tournament_management = PlayersMenu()
                    option_tournament = PlayersMenu.select(
                        input("Selection : "))
                elif selector == "3":
                    exit()
                else:
                    print("This option is unavailable, please try again")
            except TypeError:
                print("You have entered a wrong selector")


class PlayersMenu:
    def __init__(self) -> None:
        print_playermenu = players_menu()

    def select(self, selector: int):
        while True:
            try:
                if selector == "1":
                    add_player = 1
                elif selector == "2":
                    view_players = 2
                elif selector == "3":
                    return_back = MainMenu()
                    main_menu_selector = main_menu.select(
                        input("Enter your choice : "))
                else:
                    print("This option is unavailable, please try again")
            except TypeError:
                print("You have entered a wrong selector")
