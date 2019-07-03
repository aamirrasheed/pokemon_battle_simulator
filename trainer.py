from typing import NamedTuple
from pokemon import Pokemon

# Battle Choice Structs
class SwitchPokemon(NamedTuple):
    next_pokemon: Pokemon

class UseItem(NamedTuple):
    bagID: int
    pokemon_target: Pokemon

class UseMove(NamedTuple):
    moveID: int
    attacking_pokemon: Pokemon
    defending_pokemon: Pokemon

# Trainer Classes and Subclasses
class Trainer:
    def __init__(self, name, pokemon_list, item_list):
        self.name = name
        self.pokemon_list = pokemon_list
        self.item_list = item_list
    
    def first_pokemon(self):
        return self.pokemon_list[0]
    
    def has_conscious_pokemon(self):
        for pokemon in self.pokemon_list:
            if pokemon.health > 0:
                return True
        return False
    
    def switch_pokemon()

    
class HumanTrainer(Trainer):
    def __init__(self, pokemon_list, item_list):
        super().__init__(pokemon_list, item_list)

    def query_battle_choice(self):
        # TODO: fill in 
        
class ComputerTrainer(Trainer):
    def __init__(self, pokemon_list, item_list):
        super().__init__(pokemon_list, item_list)

    def query_battle_choice(self):
        # TODO: fill in 

