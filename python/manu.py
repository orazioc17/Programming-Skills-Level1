import json
from enum import Enum


# Constants
MAIN_MENU = """
########## Welcome back, Erik Ten Hahahahahahag ##########

Type the number of the option you want to execute

1.- Player Review
2.- Compare two players
3.- Identify the fastest player
4.- Identify the top goal scorer
5.- Identify the player with the most assists
6.- Identify the player with higuest passing accuracy
7.- Identify the player with the most defensive involvements
8.- exit
"""
PLAYER_REVIEW_STRING = """
********** Player {name} statistics **********
Goals: {goals}
Speed points: {speed}
Assists: {assists}
Passing accuracy points: {passing_accuracy}
defensive Involvements: {defensive_involvements}

"""

# Strings keys of the players attributes
class PlayerAttributes(Enum):
    NAME = 'name'
    GOALS = 'goals'
    SPEED = 'speed'
    ASSISTS = 'assists'
    PASSING_ACCURACY = 'passing_accuracy'
    DEFENSIVE_INVOLVEMENTS = 'defensive_involvements'


class NumberOfPlayers(Enum):
    ONE = 1
    TWO = 2


class MainMenuOption(Enum):
    PLAYER_REVIEW = "By entering the player's jersey number, access the player's characteristics."
    COMPARE_2_PLAYERS = "The system prompts for two jersey numbers and displays the data of both players on screen."
    FASTEST_PLAYER = "Displays the player with the most points in speed."
    TOP_SCORER = "Displays the player with the most points in goals."
    MOST_ASSISTS = "Displays the player with the most points in assists."
    TOP_PASSING = "Displays the player with the most points in passing accuracy."
    TOP_DEFENDER = "Displays the player with the most points in defensive involvements."
    EXIT = "Exit."


class ManchesterUnited:
    __exit_menu_loop = False

    def __init__(self):
        with open('manu_players.json', 'r') as f:
            players = json.load(f)
        new_dict = {}
        for player_number in players.keys():
            new_dict[int(player_number)] = players[player_number]
        self.__players = new_dict
    
    def __input_1_player(self) -> int:
        print(f"Available players: {list(self.__players.keys())}")
        while True:
            player_number = input("Type the player's number: ")
            try:
                player_number = int(player_number)
            except Exception:
                print('Wrong input, try again.')
                continue
            if player_number not in self.__players.keys():
                print('That player is not in the database, try another one')
                continue
            else:
                return player_number

    def __input_2_players(self):
        print(f"Available players: {list(self.__players.keys())}")
        while True:
            player_1_number = input("Type the first player's number: ")
            try:
                player_1_number = int(player_1_number)
            except Exception:
                print('Wrong input, try again.')
                continue
            if player_1_number not in self.__players.keys():
                print('That player is not in the database, try another one')
                continue
            else:
                break
        while True:
            player_2_number = input("Type the second player's number: ")
            try:
                player_2_number = int(player_2_number)
            except Exception:
                print('Wrong input, try again.')
                continue
            if player_2_number not in self.__players.keys():
                print('That player is not in the database, try another one')
                continue
            elif player_2_number == player_1_number:
                print('You already selected that player')
                continue
            else:
                break
        return player_1_number, player_2_number

    def __menu_input(self, options: dict):
        while True:
            user_option = input('Type the number of the option you want to select: ')
            
            try:
                user_option = int(user_option)
            except Exception:
                print('Wrong input, try again.')
                continue
            
            if not user_option in options.keys():
                print('Wrong input, try again.')
                continue

            break
        return user_option

    def __show_main_menu(self) -> MainMenuOption:
        options = {
            1: MainMenuOption.PLAYER_REVIEW,
            2: MainMenuOption.COMPARE_2_PLAYERS,
            3: MainMenuOption.FASTEST_PLAYER,
            4: MainMenuOption.TOP_SCORER,
            5: MainMenuOption.MOST_ASSISTS,
            6: MainMenuOption.TOP_PASSING,
            7: MainMenuOption.TOP_DEFENDER,
            8: MainMenuOption.EXIT,
        }
        
        print()
        print(MAIN_MENU)
        user_option = self.__menu_input(options)

        return options[user_option]
    
    def __display_player_statistics(self, player: dict[str, str]):
        print(PLAYER_REVIEW_STRING.format(
            name=player[PlayerAttributes.NAME.value],
            goals=player[PlayerAttributes.GOALS.value],
            assists=player[PlayerAttributes.ASSISTS.value],
            speed=player[PlayerAttributes.SPEED.value],
            passing_accuracy=player[PlayerAttributes.PASSING_ACCURACY.value],
            defensive_involvements=player[PlayerAttributes.DEFENSIVE_INVOLVEMENTS.value]
        ))

    def __player_review(self):
        player = self.__input_1_player()
        player = self.__players[player]
        self.__display_player_statistics(player)

    def __compare_2_players(self):
        player1, player2 = self.__input_2_players()
        player1 = self.__players[player1]
        player2 = self.__players[player2]

        self.__display_player_statistics(player1)
        print('VERSUS\n')
        self.__display_player_statistics(player2)

    def __filter_player(self, player_attribute: str) -> dict:
        filtered_player = None
        for player_number, player_data in self.__players.items():
            if not filtered_player:
                filtered_player = player_number
            else:
                if player_data[player_attribute] > self.__players[filtered_player][player_attribute]:
                    filtered_player = player_number
                else:
                    continue
        
        return self.__players[filtered_player]

    def __fastest_player(self):
        player = self.__filter_player(PlayerAttributes.SPEED.value)
        self.__display_player_statistics(player)

    def __top_scorer(self):
        player = self.__filter_player(PlayerAttributes.GOALS.value)
        self.__display_player_statistics(player)

    def __more_assists(self):
        player = self.__filter_player(PlayerAttributes.ASSISTS.value)
        self.__display_player_statistics(player)

    def __top_passing(self):
        player = self.__filter_player(PlayerAttributes.PASSING_ACCURACY.value)
        self.__display_player_statistics(player)

    def __top_defender(self):
        player = self.__filter_player(PlayerAttributes.DEFENSIVE_INVOLVEMENTS.value)
        self.__display_player_statistics(player)

    def __exit(self):
        print(f'\nThanks for your trust, Erik Ten Hahahahahahag, come back soon!')
        self.__exit_menu_loop = True

    def main(self):
        main_menu_options = {
            MainMenuOption.PLAYER_REVIEW: self.__player_review,
            MainMenuOption.COMPARE_2_PLAYERS: self.__compare_2_players,
            MainMenuOption.FASTEST_PLAYER: self.__fastest_player,
            MainMenuOption.TOP_SCORER: self.__top_scorer,
            MainMenuOption.MOST_ASSISTS: self.__more_assists,
            MainMenuOption.TOP_PASSING: self.__top_passing,
            MainMenuOption.TOP_DEFENDER: self.__top_defender,
            MainMenuOption.EXIT: self.__exit,
        }

        while not self.__exit_menu_loop:
            # self.__exit_main_loop = False
            main_menu_user_option = self.__show_main_menu()
            main_menu_options[main_menu_user_option]()


def run():
    manu = ManchesterUnited()
    manu.main()


if __name__ == '__main__':
    run()