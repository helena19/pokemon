from pokemon import models

def fight(
        pokemon_1: models.Pokemon, 
        pokemon_2: models.Pokemon,
    ) -> models.Pokemon:

    # Theoretically, the first pokemon has an advantage as it is attacking first
    if pokemon_1.size * pokemon_1.power >= pokemon_2.size * pokemon_2.power:
        winner = pokemon_1
    else:
        winner = pokemon_2
    
    return winner
