from controllers.menu_controller import MainMenu


def main():
    main_menu = MainMenu()
    main_menu.select(input("Enter your choice : "))


if __name__ == '__main__':
    main()
