from modules.tournament import Tournament
from views.menus import *
from modules.players import Player
from controllers.manager_controller import Manager
from controllers.saving_controller import Save


class MainMenu:
    def __init__(self) -> None:
        Manager.clear_screen()
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
                print("0000 You have entered a wrong selector")

class PlayersMenu:
    def __init__(self) -> None:
        Manager.clear_screen()
        print_playermenu = Menus.players_menu()

    def select(self, selector: int):
        while True:
            try:
                if selector == "1":
                    add_player = PlayerCreation()
                    new_player = add_player.create_new()
                elif selector == "2":
                    view_players = PlayersVisualization(Save.import_("players"))
                    menu_display = view_players.select()
                elif selector == "3":
                    return_back = MainMenu()
                    main_menu_selector = return_back.select(
                        input("Enter your choice : "))
                else:
                    print("This option is unavailable, please try again")
            except TypeError:
                print("0001 You have entered a wrong selector")

class PlayerCreation:
    def __init__(self, players_list=[]) -> None:
        Manager.clear_screen()
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
                player_dict=Manager.serialize_player_list(self.players_list)
                saving_list=Save.export_(self.players_list,"players")
                return_back=PlayersMenu()
                back_selector=return_back.select(input("Enter your choice : "))
        else:
            player_dict=Manager.serialize_player_list(self.players_list)
            saving_list=Save.export_(self.players_list,"players")
            return_back=PlayersMenu()
            back_selector=return_back.select(input("Enter your choice : "))

class PlayersVisualization:
    def __init__(self,players:list) -> None:
        Manager.clear_screen()
        self.players=players
        
    def select(self):
        menu=PlayersDisplay.menu()
        ans_menu=input("Sélection : ")
        while True:
            try:
                if ans_menu == "1":
                    self.ordered_by_name()
                elif ans_menu == "2":
                    self.ordered_by_rank()
                elif ans_menu == "3":
                    return_back = PlayersMenu()
                    main_menu_selector = return_back.select(
                        input("Enter your choice : "))
                else:
                    print("This option is unavailable, please try again")
            except TypeError:
                print("0005 You have entered a wrong selector")

    def ordered_by_name(self):
        Manager.clear_screen()
        players_list=Manager.unserialize_player_dict(self.players)
        ordered_list=sorted(players_list, key=lambda player: player.lastname,reverse=False)
        table_data=[]
        for i in ordered_list:
            table_data.append([i.firstname,i.lastname,i.birthdate,i.genre,i.rank])
        player_display=PlayersDisplay.table(table_data)
        tamp=input("Press enter to continue...")
        back_to_menu=PlayersMenu()
        btm.select=back_to_menu.select(input("Enter your choice :"))

    def ordered_by_rank(self):
        Manager.clear_screen()
        players_list=Manager.unserialize_player_dict(self.players)
        ordered_list=sorted(players_list, key=lambda player: player.rank,reverse=False)
        table_data=[]
        for i in ordered_list:
            table_data.append([i.firstname,i.lastname,i.birthdate,i.genre,i.rank])
        player_display=PlayersDisplay.table(table_data)
        tamp=input("Press enter to continue...")
        back_to_menu=PlayersMenu()
        btm.select=back_to_menu.select(input("Enter your choice :"))

class TournamentMenu:
    def __init__(self) -> None:
        Manager.clear_screen()
        print_tournament_menu=Menus.tournament_menu()
    
    def select(self,selector:int):
        while True:
            try:
                if selector == "1":
                    start_tournament=1
                elif selector == "2":
                    create_tournament=TournamentCreation()
                    new_tournament=create_tournament.create_new()
                elif selector == "3":
                    return_back = MainMenu()
                    main_menu_selector = return_back.select(
                        input("Enter your choice : "))
                else:
                    print("This option is unavailable, please try again")
            except TypeError:
                print("0002 You have entered a wrong selector")
                break

class TournamentCreation:
    def __init__(self) -> None:
        Manager.clear_screen()
        print_title=TournamentCreationInteractive.tournament_creation()

    def create_new(self):
        n=input("Nom : ")
        l=input("Localisation : ")
        dd=input("Date de début : ")
        df=input("Date de fin : ")
        tc=input("Controle de temps : ")
        rm=input("Nombre de tours (4 par défaut) : ")
        d=input("Description : ")
        #Controle des inputs
        self.new_tournament=Tournament(n,l,dd,df,tc,d,[],rm,[])
        print(TournamentCreationInteractive.tournament_add_player_menu().format(n))
        self.add_players_list(Save.import_("players"))
        serialized_tournament=Manager.serialize_tournament(self.new_tournament)
        print(serialized_tournament)
        saving_tournament=Save.export_(serialized_tournament,"tournament")#erreur
        tournament_menu=TournamentMenu()
        tournament_selection=tournament_menu.select(input("Enter your choice : "))

    def add_players_list(self,players_list:list):
        self.new_tournament.players=players_list

