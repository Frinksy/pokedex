"""
This is the main file of the pokédex
"""

import pokemon_database


def search():
    mode = -1
    while mode == -1:
        mode = input("How do you wish to search? (type, name, id)")
        mode = mode.lower()
        if mode not in ["type", "name", "id"]:
            mode = -1
            print("Invalid input!")
    if mode == "type":
        type_search()
    if mode == "name":
        name_search()
    if mode == "id":
        id_search()

def type_search():
    results = []
    print()
    print("-" * 100)
    print("Search: type mode")
    arg1 = -1
    tmode = -1
    while tmode == -1:
        tmode = str(input("How many types do you wish to search? (1 or 2)"))
        if tmode not in ["1", "2"]:
            tmode = -1
            print("Invalid!")

    while arg1 == -1:
        arg1 = input("Pokémon's type: ")
        if arg1 not in ["normal", "fire", "water", "electric",
                        "grass", "ice", "fighting", "poison", "ground",
                        "flying", "psychic", "bug", "rock", "ghost",
                        "dragon", "dark", "steel", "fairy"]:
            arg1 = -1
            print("Invalid!")
    if tmode == "2":
        arg2 = -1
        while arg2 == -1:
            arg2 = input("Pokémon's second type: ")
            if arg2 not in ["normal", "fire", "water", "electric",
                            "grass", "ice", "fighting", "poison", "ground",
                            "flying", "psychic", "bug", "rock", "ghost",
                            "dragon", "dark", "steel", "fairy"]:
                arg2 = -1
                print("Invalid!")

            try:
                arg2 = arg2.lower()
            except:
                pass

        if arg2 == arg1:
            tmode = "1"

    try:
        arg1 = arg1.lower()
    except:
        pass

    if tmode == "1":
        for pokemon in pokemon_database.pokedb:
            if pokemon.ptype == arg1 or pokemon.sec_ptype == arg1:
                results.append(pokemon.name)

    if tmode == "2":
        for pokemon in pokemon_database.pokedb:
            if (pokemon.ptype == arg1 and pokemon.sec_ptype == arg2) or (pokemon.sec_ptype == arg1 and
                                                                                 pokemon.ptype == arg2):
                results.append(pokemon.name)
                print("Debug " + pokemon.name)
    print("-"*100)
    print()
    print("Search results: ")
    for pokemon in results:
        print(pokemon)
    if len(results) == 0:
        print("No pokémon matches your search requirements.")


def name_search():
    results = []
    print()
    print("-"*100)
    arg = -1
    while arg == -1:
        arg = input("Please input at least 2 characters: ")
        if not arg.isalpha():
            print("Invalid")
            arg = -1
        if len(arg) < 2:
            arg = -1
            print("Invalid")
    for pokemon in pokemon_database.pokedb:
        if arg in pokemon.name:
            results.append(pokemon)

    print()
    print("-"*100)
    print("Search results: ")
    for pokemon in results:
        print(pokemon.name)

    if len(results) == 0:
        print("No pokémon matches your requirements.")



def id_search():
    results = []
    print()
    print("-"*100)
    arg = -1
    while arg == -1:
        arg = input("Please input the id of the desired pokémon: (000 format) ")
        if len(arg) != 3 or not arg.isnumeric():
            arg = -1
            print("Invalid")
    for pokemon in pokemon_database.pokedb:
        if pokemon.pokeid == arg:
            results.append(pokemon)
    print()
    print("-"*100)

    for pokemon in results:
        print(pokemon.name)
    if len(results) == 0:
        print("No pokémon matches you requirements.")


search()