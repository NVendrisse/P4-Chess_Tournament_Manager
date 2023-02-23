import controllers.menu_controller
from modules.tournament import Turn, Match
from controllers.manager_controller import Manager
from views.play_view import MainPlay
from controllers.saving_controller import Save, TurnSave, MatchSave


class Play:
    # Classe de gestion du déroulé d'un tournois
    def __init__(self) -> None:
        # Initialisation et sélection du tournois a jouer
        tournament_available = Save.select_tournament()
        if len(tournament_available):
            MainPlay.list_display(tournament_available)
            selected_tournament = input("Sélection du tournois : ")
            tournament_name = tournament_available[int(selected_tournament)-1]
            tournament_serialized = Save.import_(
                "tournament", "./save/tournament/{}".format(tournament_name[:len(tournament_name) - 5]))
            tournament_unserialized = Manager.unserialize_tournament(
                tournament_serialized)
            Manager.clear_screen()
            MainPlay.play_menu()
            self.tournament = tournament_unserialized
            self.players = self.tournament.players
            self.pairs = []
            MainPlay.main_title(self.tournament.name)
        else:
            MainPlay.error_no_tournament_available()
            input("Press enter to continue")
            return_back = controllers.menu_controller.MainMenu()
            return_back.select(
                input("Enter your choice : "))

    def select(self, selection: int):
        # Fonction de sélection des items du menu
        if selection == "1":
            self.start_tournament()
        elif selection == "2":
            visu = controllers.menu_controller.TournamentVisualization()
            visu.display()
            input("Press enter to continue")
            back = controllers.menu_controller.TournamentMenu()
            back.select("Enter your choice : ")
        else:
            return_back = controllers.menu_controller.MainMenu()
            return_back.select(
                input("Enter your choice : "))

    def first_player_pairing(self):
        # Fonction d'apairage des joueur en fonction du classement
        self.pairs.clear()
        players_list = Manager.unserialize_player_dict(self.players)
        self.ordered_players = sorted(
            players_list, key=lambda player: player.rank, reverse=False)
        for _index in range(len(self.ordered_players[:len(self.ordered_players)//2])):
            self.pairs.append((_index, _index+len(self.ordered_players)//2))

    def start_tournament(self):
        # Fonction de lancement d'un tournois
        # Permet le jeu d'un tournois
        self.tournament.tournament_start()
        _round = Turn(self.tournament, [], self.tournament.current_turn)
        while _round.ct <= int(self.tournament.round_amount):
            self.play_turn(_round)
            self.sort_player()
            self.tournament.current_turn = _round.ct
            self.tournament.players = Manager.serialize_player_list(
                self.ordered_players)
        self.tournament.results = Manager.serialize_player_list(sorted(Manager.unserialize_player_dict(
                self.tournament.players), key=lambda player: player.score, reverse=True))
        self.tournament.tournament_stop()
        export_tournament = Manager.serialize_tournament(self.tournament)
        Save.export_(export_tournament, "tournament",
                     "./save/tournament/{}".format(self.tournament.name))
        return_back = controllers.menu_controller.MainMenu()
        return_back.select(
            input("Enter your choice : "))

    def sort_player(self):
        # Fonction de classement des joueur d'un tournois selon le score
        self.pairs.clear()
        try:
            self.ordered_players = self.tournament.players
            self.ordered_players = sorted(
                self.ordered_players, key=lambda player: player.score, reverse=True)
            for _index in range(len(self.ordered_players[:len(self.ordered_players)//2])):
                self.pairs.append(
                    (_index, _index+len(self.ordered_players)//2))
        except AttributeError:
            self.ordered_players = Manager.unserialize_player_dict(
                self.tournament.players)
            self.ordered_players = sorted(
                self.ordered_players, key=lambda player: player.score, reverse=True)
            for _index in range(len(self.ordered_players[:len(self.ordered_players)//2])):
                self.pairs.append(
                    (_index, _index+len(self.ordered_players)//2))

    def play_turn(self, round: Turn):
        # Fonction permettant le jeu d'un tour 
        Manager.clear_screen()
        round.turn_start()
        if round.ct == 1:
            self.first_player_pairing()
        else:
            self.sort_player()
        MainPlay.round_display(self.tournament.current_turn)
        ranking = ((i.firstname, i.lastname, i.score)
                   for i in self.ordered_players)
        MainPlay.ranking_display(ranking)
        round.m = []
        for match_number in range(len(self.pairs)):
            match_pair = (self.ordered_players[self.pairs[match_number][0]],
                          self.ordered_players[self.pairs[match_number][1]])
            this_match = Match(match_pair)
            match_play = this_match.define_score()
            scoring = this_match.export_score()
            MatchSave.save(round, scoring)
            match_pair[0].score, match_pair[1].score = match_play
            self.saver()

        round.turn_stop()
        round.ct = self.tournament.current_turn
        TurnSave.save(self.tournament, round)
        self.saver()

    def saver(self):
        # Fonction de sauvegarde
        self.tournament.players = Manager.serialize_player_list(
            self.ordered_players)
        serial_tournament = Manager.serialize_tournament(self.tournament)
        Save.export_(serial_tournament, "tournament",
                     "./save/tournament/{}".format(self.tournament.name))
