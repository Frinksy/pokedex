"""
This file contains all the pokémon in the pokedex's database
pokédex entries are taken from bulbapedia.bulbagarden.net

"""


class Pokemon(object):
    # pokémon class to store all the different pokémon variables with functions to display them

    def __init__(self, name, pokeid, desc, ptype, sec_ptype):
        self.name = name
        self.pokeid = pokeid
        self.desc = desc
        self.ptype = ptype
        self.sec_ptype = sec_ptype

    def show_inf(self):
        print("Pokemon #{0} : {1}")
        print(self.desc)



bulbasur = Pokemon("Bulbasur", "001", "A seed is growing on its back.", "grass", "poison")
ivysaur = Pokemon("Ivysaur", "002", "When the bulb on its back grows large, it appears to lose the ability to stand on its hind legs. ", "grass", "poison")
venusaur = Pokemon("Venusaur", "003", "The plant blooms when it is absorbing solar energy. It stays on the move to seek sunlight. ", "grass", "poison")
charmander = Pokemon("Charmander", "004", " 	Obviously prefers hot places. When it rains, steam is said to spout from the tip of its tail. ", "fire", None)
charmeleon = Pokemon("Charmeleon", "005", " 	When it swings its burning tail, it elevates the temperature to unbearably high levels. ", "fire", None )
charizard = Pokemon("Charizard", "006", "Spits fire that is hot enough to melt boulders. Known to cause forest fires unintentionally. ", "fire", "flying")
squirtle = Pokemon("Squirtle", "007", "After birth, its back swells and hardens into a shell. Powerfully sprays foam from its mouth. ", "fater", None)
wartortle = Pokemon("Wartortle", "008", "Often hides in water to stalk unwary prey. For swimming fast, it moves its ears to maintain balance. ", "water", None)
blastoise = Pokemon("Blastoise", "009", "A brutal Pok�mon with pressurized water jets on its shell. They are used for high speed tackles. ", "water", None)


pokedb = [
    bulbasur,
    ivysaur,
    venusaur,
    charmander,
    charmeleon,
    charizard,
    squirtle,
    wartortle,
    blastoise,
]