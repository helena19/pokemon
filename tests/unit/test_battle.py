from pokemon import battle
from pokemon import enums
from pokemon import models

class TestFight:
    _charizard = models.Pokemon(
        name='charizard',
        height=17,
        weight=905,
        stats=[
            models.Stat(
                details=models.StatDetails(name=enums.Stat.HP),
                base_stat=78,
            ),
            models.Stat(
                details=models.StatDetails(name=enums.Stat.ATTACK),
                base_stat=84,
            ),
            models.Stat(
                details=models.StatDetails(name=enums.Stat.DEFENSE),
                base_stat=78,
            ),
            models.Stat(
                details=models.StatDetails(name=enums.Stat.SPECIAL_ATTACK),
                base_stat=109,
            ),
            models.Stat(
                details=models.StatDetails(name=enums.Stat.SPECIAL_DEFENSE),
                base_stat=85,
            ),
            models.Stat(
                details=models.StatDetails(name=enums.Stat.SPEED),
                base_stat=100,
            ),
        ]
    )

    _bulbasaur = models.Pokemon(
        name='bulbasaur',
        height=7,
        weight=69,
        stats=[
            models.Stat(
                details=models.StatDetails(name=enums.Stat.HP),
                base_stat=45,
            ),
            models.Stat(
                details=models.StatDetails(name=enums.Stat.ATTACK),
                base_stat=49,
            ),
            models.Stat(
                details=models.StatDetails(name=enums.Stat.DEFENSE),
                base_stat=49,
            ),
            models.Stat(
                details=models.StatDetails(name=enums.Stat.SPECIAL_ATTACK),
                base_stat=65,
            ),
            models.Stat(
                details=models.StatDetails(name=enums.Stat.SPECIAL_DEFENSE),
                base_stat=65,
            ),
            models.Stat(
                details=models.StatDetails(name=enums.Stat.SPEED),
                base_stat=45,
            ),
        ]
    )

    _a_fantastic_pokemon = models.Pokemon(
        name='_a_fantastic_pokemon',
        height=17,
        weight=905,
        stats=[
            models.Stat(
                details=models.StatDetails(name=enums.Stat.HP),
                base_stat=78,
            ),
            models.Stat(
                details=models.StatDetails(name=enums.Stat.ATTACK),
                base_stat=84,
            ),
            models.Stat(
                details=models.StatDetails(name=enums.Stat.DEFENSE),
                base_stat=78,
            ),
            models.Stat(
                details=models.StatDetails(name=enums.Stat.SPECIAL_ATTACK),
                base_stat=109,
            ),
            models.Stat(
                details=models.StatDetails(name=enums.Stat.SPECIAL_DEFENSE),
                base_stat=85,
            ),
            models.Stat(
                details=models.StatDetails(name=enums.Stat.SPEED),
                base_stat=100,
            ),
        ]
    )

    def test_pokemon_1_wins(self):
        # arrange & act
        winner = battle.fight(
            pokemon_1=self._charizard, 
            pokemon_2=self._bulbasaur
        )

        # assert
        assert winner == self._charizard

    def test_pokemon_2_wins(self):
        # arrange & act
        winner = battle.fight(
            pokemon_1=self._bulbasaur, 
            pokemon_2=self._charizard
        )

        # assert
        assert winner == self._charizard

    def test_first_pokemon_wins_when_stats_equal(self):
         # arrange & act
        winner = battle.fight(
            pokemon_1=self._charizard, 
            pokemon_2=self._a_fantastic_pokemon
        )

        # assert
        assert winner == self._charizard
