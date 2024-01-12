from enum import Enum
import json


# Constants
COUNTRY_STRING = 'country'
ACTIVITIES_STRING = 'activities'
MAIN_MENU = """
########## Welcome to CappaTravel ##########

Type the number of the option you want to execute

1.- Procceed to a travel recommendation
2.- exit
"""
SHOW_SEASON_PRICES = """
1.- Traveling in {} costs {}
2.- Traveling in {} costs {}
3.- Traveling in {} costs {}
4.- Traveling in {} costs {}
"""
SHOW_TYPE_OF_TRAVELS = """
1.- A travel full of extreme physical activities and sports.
2.- A travel more oriented to cultural/historical/relaxed activities.
"""
TRAVEL_INFO = """
We recommend you this destination
####      {country_name}      ####
You have this activities available at this location: {activities}
"""


# Enums
class Seasons(Enum):
    WINTER = 'winter'
    SPRING = 'spring'
    SUMMER = 'summer'
    AUTUMN = 'autumn'


class TypeOfTravel(Enum):
    PHYSICAL = 0
    CULTURAL = 1


class Costs(Enum):
    WINTER = 100
    AUTUMN = 200
    SPRING = 300
    SUMMER = 400


class Countries(Enum):
    ANDORRA = 'Andorra'
    SWITZERLAND = 'Switzerland'
    SPAIN = 'Spain'
    PORTUGAL = 'Portugal'
    FRANCE = 'France'
    ITALY = 'Italy'
    BELGIUM = 'Belgium'
    AUSTRIA = 'Austria'


class MainMenuOption(Enum):
    GENERATE_RECOMENDATION = 1
    EXIT = 2


class InputUserOptions(Enum):
    GET_SEASON = 1
    GET_TYPE_OF_TRAVEL = 2


class TravelAgency:
    __exit_menu_loop = False
    def __init__(self):
        with open('destinies.json', 'r') as f:
            self.__destinies = json.load(f)
        
    def __user_input(self, option):
        match option:
            case InputUserOptions.GET_SEASON:
                options = {
                    1: Seasons.SPRING.name,
                    2: Seasons.SUMMER.name,
                    3: Seasons.AUTUMN.name,
                    4: Seasons.WINTER.name,
                }
                print(SHOW_SEASON_PRICES.format(
                    Seasons.SPRING.value, Costs.SPRING.value,
                    Seasons.SUMMER.value, Costs.SUMMER.value,
                    Seasons.AUTUMN.value, Costs.AUTUMN.value,
                    Seasons.WINTER.value, Costs.WINTER.value,
                ))
                while True:
                    user_option = input('Type the number of the option you want: ')
                    try:
                        user_option = int(user_option)
                    except Exception:
                        print('Wrong input, try again.')
                        continue

                    if user_option not in options.keys():
                        print('Wrong number, out of the range of options, try again.')
                        continue
                        
                    return options[user_option]

            case InputUserOptions.GET_TYPE_OF_TRAVEL:
                options = {
                    1: TypeOfTravel.PHYSICAL.value,
                    2: TypeOfTravel.CULTURAL.value,
                }
                print(SHOW_TYPE_OF_TRAVELS)
                while True:
                    user_option = input('Type the number of the option you want: ')
                    try:
                        user_option = int(user_option)
                    except Exception:
                        print('Wrong input, try again.')
                        continue

                    if user_option not in options.keys():
                        print('Wrong number, out of the range of options, try again.')
                        continue
                        
                    return options[user_option]
                
    def __generate_recommendation(self, season, type_of_travel):
        return self.__destinies[season][type_of_travel]
    
    def __display_recommendation(self, travel):
        print(TRAVEL_INFO.format(
            country_name=travel[COUNTRY_STRING],
            activities=travel[ACTIVITIES_STRING]
        ))

    def __get_recomendation(self):
        # 1st step, show prices for every destination, 2nd step, ask for which type of travel ()
        season = self.__user_input(InputUserOptions.GET_SEASON)
        type_of_travel = self.__user_input(InputUserOptions.GET_TYPE_OF_TRAVEL)
        travel_recommendation = self.__generate_recommendation(season, type_of_travel)
        self.__display_recommendation(travel_recommendation)

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

    def __show_main_menu(self, options) -> MainMenuOption:
        
        print(MAIN_MENU)
        user_option = self.__menu_input(options)

        options[user_option]()

    def __exit(self):
        print(f'\nThanks for your trust, use CappaTravel again soon!')
        self.__exit_menu_loop = True

    def main(self):
        while not self.__exit_menu_loop:
            main_menu_options = {
                MainMenuOption.GENERATE_RECOMENDATION.value: self.__get_recomendation,
                MainMenuOption.EXIT.value: self.__exit,
            }
            self.__show_main_menu(main_menu_options)


def run():
    travel_agency = TravelAgency()
    travel_agency.main()


if __name__ == '__main__':
    run()
    