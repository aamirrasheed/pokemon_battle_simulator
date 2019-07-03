import errno
import os

class Pokemon:
    def __init__(self, pokename):
        pokefile_name = pokename + ".txt"
        if os.path.exists(pokefile_name):
            pokefile = open(pokefile_name, "r")
            lines = pokefile.readlines()

            # permanent traits
            self.primary_type = lines[0]
            self.secondary_type = lines[1] 
            self.health = lines[2]
            self.attack = lines[3]
            self.defense = lines[4]
            self.special_attack = lines[5]
            self.special_defense = lines[6]
            self.speed = lines[7]
            self.move1 = lines[8]
            self.move2 = lines[9]
            self.move3 = lines[10]
            self.move4 = lines[11]

            # variable traits
            self.current_health = self.health
            self.status = None # TODO: make into enum

        else:
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), pokefile_name)

    def attacked_by(pokemon, move):
        


