
import json
import random


def guessing_game(x, y, z):
    """This function loads the json file which contains data about cities and countries. Then it randomly chooses the
    city and asks the user for its country. If you get it right then you can go to the next city. If you get it wrong
    then you are given two hints. First hint is about number of letters in the country's name. Second hint is the
    starting letter in the name of the country. The data is taken from https://datahub.io/core/world-cities#readme
    who have taken the data from geonames.org."""
    cities_list = json.load(open('world-cities_json.json'))
    no_of_cities = (len(cities_list))
    random_city_number = random.randint(0, no_of_cities - 1)
    print("In which country " + cities_list[random_city_number]["name"] + " is ?")
    guessed_country = input("Guessed country is: ")
    if guessed_country.title() == cities_list[random_city_number]["country"]:
        print("You got it right! " + cities_list[random_city_number]["name"] + " is in " +
              cities_list[random_city_number]["country"])
        x += 1
    while guessed_country.title() != cities_list[random_city_number]["country"]:
        y += 1
        if y == 1:
            print("Here's a hint for you! Country's name is a " + str(
                len(cities_list[random_city_number]["country"]) - cities_list[random_city_number]["country"].count(
                    " ")) + " letter word.")
            guessed_country = input("Guessed country is: ")
            if guessed_country.title() == cities_list[random_city_number]["country"]:
                print("You got it right! " + cities_list[random_city_number]["name"] + " is in " +
                      cities_list[random_city_number]["country"])
                x += 1
        elif y == 2:
            print("Another hint - The name starts with " + str(cities_list[random_city_number]["country"][0]))
            guessed_country = input("Guessed country is: ")
            if guessed_country.title() == cities_list[random_city_number]["country"]:
                print("You got it right! " + cities_list[random_city_number]["name"] + " is in " +
                      cities_list[random_city_number]["country"])
                x += 1
        else:
            print("That's wrong, " + cities_list[random_city_number]["name"] + " is in " +
                  cities_list[random_city_number]["country"])
            z += 1
            break
    return x, z


def main():
    """This function prints general information and some instructions to play the game. The function calls
    guessing_game function which is the actual game. After voluntarily finishing the game, your score is printed by
    the main function."""
    right_guess_counter = 0
    intermediate_wrong_counter = 0
    final_wrong_counter = 0
    print("Welcome to the 'Country-Guesser' game!")
    print("In this game, you'll be given name of the city and you have to guess the country it belongs to.")
    intent = input("Want to play the game? Type 'Y' to start and 'N' to end: ")
    while intent.upper() != "Y" and intent.upper() != "N":
        intent = input("Please write 'Y' or 'N' only: ")
    while intent.upper() == "Y":
        right_guess_counter, final_wrong_counter = guessing_game(right_guess_counter, intermediate_wrong_counter,
                                                                 final_wrong_counter)
        intent = input("Want to play the game? Type 'Y' to start and 'N' to end: ")
        while intent.upper() != "Y" and intent.upper() != "N":
            intent = input("Please write 'Y' or 'N' only: ")
    print("Hope you had a great time! You got " + str(right_guess_counter) + " guesses right! and " + str(
        final_wrong_counter) + " wrong. ")


if __name__ == '__main__':
    main()
