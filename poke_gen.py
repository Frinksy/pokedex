print("-"*100)
print("Pokemon generator started.")
print("To add a pokémon, please follow the instructions that will follow.")
print("If you wish to stop the program, please type in 'STOP'.")

pokef = open("pokemon_database.py", "a")

while True:
    name = input("Name of the pokémon:")
    if name.lower() == "stop":
        break
    ptype = input("What is the pokémon's type? : ")
    if ptype.lower() == "stop":
        break
    sec_ptype = input("What is the pokémon's secondary type? (if not leave blank) : ")
    if sec_ptype.lower() == "stop":
        break
    desc = input("What is the pokémon's description? : ")
    if desc.lower == "stop":
        break
    pokeid = input("What is the pokémon id? s(use the 000 format): ")
    if pokeid.lower() == "stop":
        break
    print()
    print()

    pokef.write("""{0} = Pokemon("{1}", "{2}", "{3}", {4}, {5})\n""".format(name.lower(), name, pokeid, desc, ptype, sec_ptype))
    print("""{0} = Pokemon("{1}", "{2}", "{3}", {4}, {5})""".format(name.lower(), name, pokeid, desc, ptype, sec_ptype))
print("END")