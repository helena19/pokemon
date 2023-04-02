from pydantic import BaseModel
from pydantic import Field

class StatDetails(BaseModel):
    name: str = Field(alias='name')


class Stat(BaseModel):
    details: StatDetails = Field(alias='stat')
    base_stat: int = Field(alias='base_stat')
    effort: int = Field(alias='effort')


class Pokemon(BaseModel):
    id: int = Field(alias='id')
    name: str = Field(alias='name')
    order: int = Field(alias='order')
    base_experience: int = Field(alias='base_experience')
    height: int = Field(alias='height')
    weight: int = Field(alias='weight')
    stats: list[Stat] = Field(alias='stats')
