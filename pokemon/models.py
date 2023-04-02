import dataclasses

from pokemon import enums
from pokemon import schema

@dataclasses.dataclass
class StatDetails:
    name: str


@dataclasses.dataclass
class Stat:
    details: str
    base_stat: int


@dataclasses.dataclass
class Pokemon:
    name: str
    height: int
    weight: int
    stats: list[Stat]

    @property
    def size(self) -> int:
        return self.height * self.weight
    
    @property
    def strength(self) -> int:
        stats = self.stats
        strength = 0
        for stat in stats:
            if stat.details.name != enums.Stat.HP:
                strength = strength + stat.base_stat
        
        return strength
    
    @property
    def power(self) -> int:
        stats = self.stats
        power = 0
        for stat in stats:
            if stat.details.name == enums.Stat.HP:
                power = self.strength * stat.base_stat
        
        return power if power > 0 else self.strength

    @staticmethod
    def from_pokemon_card(pokemon_card: schema.PokemonCard) -> 'Pokemon':
        return Pokemon(
            name=pokemon_card.name,
            height=pokemon_card.height,
            weight=pokemon_card.weight,
            stats=[
                Stat(
                    details=StatDetails(
                        name=stat.details.name,
                    ), 
                    base_stat=stat.base_stat
                ) for stat in pokemon_card.stats
            ]
        )
    
    @staticmethod
    def to_pokemon_card(pokemon: 'Pokemon') -> schema.PokemonCard:
        return schema.PokemonCard(
            name=pokemon.name,
            height=pokemon.height,
            weight=pokemon.weight,
            stats=[
                schema.Stat(
                    details=schema.StatDetails(
                        name=stat.details.name,
                    ), 
                    base_stat=stat.base_stat
                ) for stat in pokemon.stats
            ]
        )
