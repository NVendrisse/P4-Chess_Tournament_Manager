from modules.tournament import Tournament
from views.menus import Menus, PlayersCreationInteract, PlayersDisplay
from views.menus import TournamentCreationInteractive, TournamentDisplay
from views.play_view import MainPlay
from modules.players import Player
from controllers.manager_controller import Manager
from controllers.saving_controller import Save
from controllers.play_tournament import Play
from controllers.flake8_generator import FlakeControl
import re
import os


class SplashScreenLoader:
    def display():
        Manager.clear_screen()
        file = open("./views/chess_piece.txt")
        file_content = file.read()
        Menus.splash_screen(file_content)
        file.close()


class MainMenu:
    def __init__(self) -> None:
        Manager.clear_screen()
        self.is_players_list = bool(len(os.listdir("./save/players_list")))
        self.is_tournament_list = bool(len(os.listdir("./save/tournament")))
        Menus.main_menu(self.is_tournament_list, self.is_players_list)

    def select(self, selector: int):
        while True:
            '''try:'''
            if selector == "1" and self.is_tournament_list:
                play_tournament = Play()
                play_tournament.select(
                    input("Selection : "))
            elif selector == "2":
                player_management = PlayersMenu()
                player_management.select(
                    input("Selection : "))
            elif selector == "3" and self.is_players_list:
                tournament_management = TournamentMenu()
                tournament_management.select(
                    input("Selection : "))
            elif selector == "4":
                Manager.clear_screen()
                FlakeControl.control()
                exit()
            else:
                print("This option is unavailable, please try again")
                input("Press enter to continue")
                menu = MainMenu()
                menu.select(input("Selection : "))
            '''except TypeError:
                print("0000 You have entered a wrong selector")
                break'''


class PlayersMenu:
    def __init__(self) -> None:
        Manager.clear_screen()
        Menus.players_menu()

    def select(self, selector: int):
        while True:
            try:
                if selector == "1":
                    new_list_name = input(
                        "Nom de la nouvelle liste de joueur : ")
                    add_player = PlayerCreation(listname=new_list_name)
                    add_player.create_new()
                elif selector == "2":
                    existing_list = os.listdir("./save/players_list")
                    MainPlay.list_display(existing_list)
                    select_list = input("Sélection d'une liste de joueur : ")
                    selected_item = existing_list[int(select_list)-1][:len(existing_list[int(select_list)-1])-5]
                    existing_players_dict = Save.import_(
                        "players", "./save/players_list/{}".format(selected_item))
                    view_players = PlayersVisualization(existing_players_dict)
                    view_players.select()
                elif selector == "3":
                    existing_list = os.listdir("./save/players_list")
                    MainPlay.list_display(existing_list)
                    select_list = input("Sélection d'une liste de joueur : ")
                    selected_item = existing_list[int(select_list)-1][:len(existing_list[int(select_list)-1])-5]
                    existing_players_dict = Save.import_(
                        "players", "./save/players_list/{}".format(selected_item))
                    existing_players_list = Manager.unserialize_player_dict(
                        existing_players_dict)
                    add_player = AddingPlayer(existing_players_list, existing_list[int(
                        select_list)-1][:len(existing_list[int(select_list)-1])-5]).add()
                elif selector == "4":
                    return_back = MainMenu()
                    return_back.select(
                        input("Enter your choice : "))
                else:
                    print("This option is unavailable, please try again")
                    break
            except TypeError:
                print("0001 You have entered a wrong selector")
                break


class PlayerCreation:
    def __init__(self, players_list=[], listname="") -> None:
        Manager.clear_screen()
        self.players_list = players_list
        self.list_name = listname
        PlayersCreationInteract.player_creation()

    def create_new(self):

        Manager.clear_screen()
        fname = input("Prénom : ")
        lname = input("Nom : ")
        bdate = ""
        genre = ""
        while not re.match(r'[0-3][0-9]/[0-1][0-9]/[0-9][0-9][0-9][0-9]', bdate):
            bdate = input("Date de naissance (jj/mm/aaaa) : ")
        while not re.match(r'[MFN]', genre):
            genre = input("Genre (M/F/N) : ").upper()
        rank = input("Classement : ")
        new_player = Player(fname, lname, bdate, genre, rank)
        self.players_list.append(new_player)
        if len(self.players_list) < 8:
            print(PlayersCreationInteract.ask_new().format(
                len(self.players_list)))
            answer = input("Y/n : ")
            if answer == "Y" or answer == "y":
                self.create_new()
            elif answer == "N" or answer == "n":
                player_dict = Manager.serialize_player_list(self.players_list)
                Save.export_(player_dict, "players",
                             "./save/players_list/{}".format(self.list_name))
                return_back = PlayersMenu()
                return_back.select(
                    input("Enter your choice : "))
            else:
                player_dict = Manager.serialize_player_list(self.players_list)
                Save.export_(player_dict, "players",
                             "./save/players_list/{}".format(self.list_name))
                return_back = PlayersMenu()
                return_back.select(
                    input("Enter your choice : "))
        else:
            player_dict = Manager.serialize_player_list(self.players_list)
            Save.export_(player_dict, "players",
                         "./save/players_list/{}".format(self.list_name))
            return_back = PlayersMenu()
            return_back.select(input("Enter your choice : "))


class AddingPlayer:
    def __init__(self, players_list, players_list_name: str) -> None:
        self.players_list = players_list
        self.players_list_name = players_list_name

    def add(self):
        adding = PlayerCreation(self.players_list, self.players_list_name)
        adding.create_new()


class PlayersVisualization:
    def __init__(self, players: list) -> None:
        Manager.clear_screen()
        self.players = players

    def select(self):
        PlayersDisplay.menu()
        ans_menu = input("Sélection : ")
        while True:
            try:
                if ans_menu == "1":
                    self.ordered_by_name()
                elif ans_menu == "2":
                    self.ordered_by_rank()
                elif ans_menu == "3":
                    return_back = PlayersMenu()
                    return_back.select(
                        input("Enter your choice : "))
                else:
                    print("This option is unavailable, please try again")
                    break
            except TypeError:
                print("0005 You have entered a wrong selector")
                break

    def ordered_by_name(self):
        Manager.clear_screen()
        players_list = Manager.unserialize_player_dict(self.players)
        ordered_list = sorted(
            players_list, key=lambda player: player.lastname, reverse=False)
        table_data = []
        for i in ordered_list:
            table_data.append(
                [i.firstname, i.lastname, i.birthdate, i.genre, i.rank, i.score])
        PlayersDisplay.table(table_data)
        input("Press enter to continue...")
        back_to_menu = PlayersMenu()
        back_to_menu.select(input("Enter your choice :"))

    def ordered_by_rank(self):
        Manager.clear_screen()
        players_list = Manager.unserialize_player_dict(self.players)
        ordered_list = sorted(
            players_list, key=lambda player: player.rank, reverse=False)
        table_data = []
        for i in ordered_list:
            table_data.append(
                [i.firstname, i.lastname, i.birthdate, i.genre, i.rank, i.score])
        PlayersDisplay.table(table_data)
        input("Press enter to continue...")
        back_to_menu = PlayersMenu()
        back_to_menu.select(input("Enter your choice :"))


class TournamentMenu:
    def __init__(self) -> None:
        Manager.clear_screen()
        Menus.tournament_menu()

    def select(self, selector: int):
        while True:
            '''try:'''
            if selector == "1":
                create_tournament = TournamentCreation()
                create_tournament.create_new()
            elif selector == "2":
                visu = TournamentVisualization()
                visu.display()
            elif selector == "3":
                return_back = MainMenu()
                return_back.select(
                    input("Enter your choice : "))
            else:
                print("This option is unavailable, please try again")
                break
            '''except TypeError:
                print("0002 You have entered a wrong selector")
                break'''


class TournamentCreation:
    def __init__(self) -> None:
        Manager.clear_screen()
        TournamentCreationInteractive.tournament_creation()

    def create_new(self):
        n = input("Nom : ")
        loc = input("Localisation : ")
        dd = input("Date de début : ")
        df = input("Date de fin : ")
        tc = input("Controle de temps : ")
        rm = input("Nombre de tours (4 par défaut) : ")
        d = input("Description : ")
        # Controle des inputs
        self.new_tournament = Tournament(n, loc, dd, df, tc, d, [], rm, [])
        print(TournamentCreationInteractive.tournament_add_player_menu().format(n))
        existing_list = os.listdir("./save/players_list")
        MainPlay.list_display(existing_list)
        select_list = input("Sélection d'une liste de joueur :")
        import_player_dict = Save.import_("players", "./save/players_list/{}".format(
            existing_list[int(select_list)-1][:len(existing_list[int(select_list)-1])-5]))
        self.new_tournament.players = import_player_dict
        serialized_tournament = Manager.serialize_tournament(
            self.new_tournament)
        Save.export_(serialized_tournament, "tournament",
                     "./save/tournament/{}".format(n))
        input()
        tournament_menu = TournamentMenu()
        tournament_menu.select(
            input("Enter your choice : "))


class TournamentVisualization:

    def __init__(self) -> None:
        tournament_available = Save.select_tournament()
        MainPlay.list_display(tournament_available)
        selected_tournament = input("Sélection du tournois : ")
        tournament_name = tournament_available[int(selected_tournament)-1]
        tournament_serialized = Save.import_(
            "tournament", "./save/tournament/{}".format(tournament_name[:len(tournament_name)-5]))
        self.t = Manager.unserialize_tournament(tournament_serialized)

    def display(self):
        Manager.clear_screen()
        TournamentDisplay.display(self.t)
