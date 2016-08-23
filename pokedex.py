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


def type_search():
    results = []
    print()
    print("-" * 10)
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
    print("-"*10)
    print()
    print("Search results: ")
    for pokemon in results:
        print(pokemon)
    if len(results) == 0:
        print("No pokémon matches your search arguments.")


search()