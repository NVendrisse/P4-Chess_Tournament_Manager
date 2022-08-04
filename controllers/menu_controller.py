from views.main_menu import main_menu


class MainMenu:
    def __init__(self) -> None:
        print_main=main_menu()

    def select(self,selector:int):
        while True:
            try:
                if selector==1:
                    play_tournament=1
                elif selector==2:
                    tournament_management=2
                elif selector==3:
                    exit()
                else:
                    print("This option is unavailable, please try again")
            except TypeError:
                print("You have entered a wrong selector")
