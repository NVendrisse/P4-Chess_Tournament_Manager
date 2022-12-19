from controllers.menu_controller import MainMenu, SplashScreenLoader


def main():
    SplashScreenLoader.display()
    input("Press enter to start...")
    main_menu = MainMenu()
    main_menu.select(input("Enter your choice : "))


if __name__ == '__main__':
    main()
