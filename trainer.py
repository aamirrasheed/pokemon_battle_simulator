from typing import NamedTuple
from pokemon import Pokemon
from abc import ABC, abstractmethod

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
class Trainer(ABC):
    def __init__(self, name, pokemon_list, item_list):
        # initialized class variables
        self.name = name
        self.pokemon_list = pokemon_list
        self.bag = item_list

        # other class variables
        self.active_pokemon = None
    
    def set_active_pokemon(self):
        self.active_pokemon = self.pokemon_list[0]
    
    def has_conscious_pokemon(self):
        for pokemon in self.pokemon_list:
            if pokemon.health > 0:
                return True
        return False
    
    def switch_pokemon(self, switch_pokemon_struct):
        self.pokemon_list.remove(switch_pokemon_struct.next_pokemon)
        self.pokemon_list.add(self.active_pokemon)
        self.active_pokemon = switch_pokemon_struct.next_pokemon

    def use_item(self, itemID, pokemonID):
        self.bag.remove(wo)

    @abstractmethod
    def query_battle_choice(self):
        pass


    
class HumanTrainer(Trainer):
    def __init__(self, pokemon_list, item_list):
        super().__init__(pokemon_list, item_list)

    def query_battle_choice(self):
        pass
        # TODO: fill in 
        
class ComputerTrainer(Trainer):
    def __init__(self, pokemon_list, item_list):
        super().__init__(pokemon_list, item_list)

    def query_battle_choice(self):
        pass
        # TODO: fill in 

