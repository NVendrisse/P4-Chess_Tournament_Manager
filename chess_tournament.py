from controllers.menu_controller import MainMenu, SplashScreenLoader
from genericpath import exists
import shutil
import os



def main():
    # main function outside MVC, launch the soft
    if not exists("./save/players_list"):
        os.makedirs("./save/players_list", exist_ok=False)
    if not exists("./save/tournament/"):
        os.makedirs("./save/tournament/", exist_ok=False)
    SplashScreenLoader.display()
    input("Press enter to start...")
    main_menu = MainMenu()
    main_menu.select(input("Enter your choice : "))


if __name__ == '__main__':
    main()
