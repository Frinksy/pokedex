"""
This is the main file of the pokédex
"""


def search():
    mode = -1
    while mode == -1:
        mode = input("How do you wish to search? (type, name, id)")
        mode = mode.lower()
        if mode not in ["type", "name", "id"]:
            mode = -1
            print("Invalid input!")

    if mode == "type":
        print()
        print("-"*10)
        print("Search: type mode")
        arg1 = -1
        tmode = -1
        while tmode == -1:
            tmode = str(input("How many types do you wish to search? (1 or 2)"))
            if tmode not in ["1", "2"]:
                tmode = -1

        while arg1 == -1:
            arg1 = input("Pokémon's type: ")
            if arg1 not in ["normal", "fire", "water", "electric",
                            "grass", "ice", "fighting", "poison", "ground",
                            "flying", "psychic", "bug", "rock", "ghost",
                            "dragon", "dark", "steel", "fairy"]:
                arg1 = -1
        if tmode == "2":
            arg2 = -1
            while arg2 == -1:
                arg2 = input("Pokémon's second type: ")
                if arg2 not in ["normal", "fire", "water", "electric",
                                "grass", "ice", "fighting", "poison", "ground",
                                "flying", "psychic", "bug", "rock", "ghost",
                                "dragon", "dark", "steel", "fairy"]:
                    arg2 = -1
                elif arg2 == arg1:
                    tmode = "1"