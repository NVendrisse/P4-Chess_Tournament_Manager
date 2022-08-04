from controllers.menu_controller import MainMenu

def main():
    main_menu=MainMenu()
    main_menu_selector=main_menu.select(input("Enter your choice : 0"))

if __name__=='__main__':
    main()