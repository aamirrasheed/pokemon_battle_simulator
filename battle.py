class Battle:
    def __init__(self, trainer_1, trainer_2):
        self.trainer_1 = trainer_1
        self.trainer_2 = trainer_2
    
    def start(self):
        # set active initial pokemon
        active_pokemon_1 = self.trainer_1.first_pokemon()
        active_pokemon_2 = self.trainer_2.first_pokemon()

        # introduce battle
        
        # start battle sequence
        while self.trainer_1.has_conscious_pokemon() and self.trainer_2.has_conscious_pokemon():
            
            # get battle choices by trainer
            # for 3 variables returned, only one of them is not None per loop
            # this dictates which battle choice each trainer picked
            switch_pokemon_struct_1, use_item_struct_1, use_move_struct_1 = self.trainer_1.query_battle_choice()
            switch_pokemon_struct_2, use_item_struct_2, use_move_struct_2 = self.trainer_1.query_battle_choice()
            
            # execute pokemon switches
            if switch_pokemon_struct_1 is not None:

                print(self.trainer_1.name + " withdrew " + active_pokemon_1.name )

                self.trainer_1.switch_pokemon(switch_pokemon_struct_1)
                active_pokemon_1 = switch_pokemon_struct_1.next_pokemon
                
                print(self.trainer_1.name + " sent out " + active_pokemon_1.name )

            if switch_pokemon_struct_2 is not None:
                print(self.trainer_2.name + " withdrew " + active_pokemon_2.name )

                self.trainer_2.switch_pokemon(switch_pokemon_struct_2)
                active_pokemon_2 = switch_pokemon_struct_2.next_pokemon
                
                print(self.trainer_2.name + " sent out " + active_pokemon_2.name )

            # execute bag items
            if use_item_struct_1 is not None:
                self.trainer_1.use_item(use_item_struct_1.itemID, use_item_struct_1.pokemonID)
                print(self.trainer_1.name + " used " + use_item_struct_1.item_name)
                print(use_item_struct_1.item_effect_text)

            if use_item_struct_2 is not None:
                self.trainer_2.use_item(use_item_struct_2.itemID, use_item_struct_2.pokemonID)
                print(self.trainer_2.name + " used " + use_item_struct_2.item_name)
                print(use_item_struct_2.item_effect_text)

            # execute moves
            if use_move_struct_1 is not None and use_move_struct_2 is None:
                use_move_struct_1.move.execute(active_pokemon_1, active_pokemon_2)
                print(use_move_struct_1.move_text)
                print(use_move_struct_1.effect_text)
            
            if use_move_struct_2 is not None and use_move_struct_1 is None:
                use_move_struct_2.move.execute(active_pokemon_2, active_pokemon_1)
                print(use_move_struct_2.move_text)
                print(use_move_struct_2.effect_text)
                
            else: # this is the main battle thread where both pokemon use moves
                if active_pokemon_1.speed > active_pokemon_2.speed:
                    use_move_struct_1.move.execute(active_pokemon_1, active_pokemon_2)
                    print(use_move_struct_1.move_text)
                    print(use_move_struct_1.effect_text)

                    use_move_struct_2.move.execute(active_pokemon_2, active_pokemon_1)
                    print(use_move_struct_2.move_text)
                    print(use_move_struct_2.effect_text)
                else:
                    use_move_struct_2.move.execute(active_pokemon_2, active_pokemon_1)
                    print(use_move_struct_2.move_text)
                    print(use_move_struct_2.effect_text)

                    use_move_struct_1.move.execute(active_pokemon_1, active_pokemon_2)
                    print(use_move_struct_1.move_text)
                    print(use_move_struct_1.effect_text)

            # post move effects
            if active_pokemon_1.has_post_move_effect():
                active_pokemon_1.execute_post_move_effect()
                if active_pokemon_1.check_end_post_move_effect():
                    active_pokemon_1.remove_post_move_effect()

            if active_pokemon_2.has_post_move_effect():
                active_pokemon_2.execute_post_move_effect()
                if active_pokemon_2.check_end_post_move_effect():
                    active_pokemon_2.remove_post_move_effect()
                    
            # check for fainted pokemon, and if so, query trainers for new ones. If failed, end battle
            if active_pokemon_1.is_fainted():
                active_pokemon_1 = self.trainer_1.query_next_pokemon()
                if active_pokemon_1 is None:
                    break
            if active_pokemon_2.is_fainted():
                active_pokemon_2 = self.trainer_2.query_next_pokemon()
                if active_pokemon_2 is None:
                    break
        
        # end of battle sequence
        if self.trainer_1.has_conscious_pokemon():
            print("Trainer 1 wins!")
        if self.trainer_2.has_conscious_pokemon():
            print("Trainer 2 wins!")
