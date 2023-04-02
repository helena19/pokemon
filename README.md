# Pokemon api integration

## Commands
You need `docker` and `docker compose` to run the project.

Build image:
```bash
make image
```

Run app :
```bash
# (run the app)
docker-compose run app
# (run the app tests)
docker-compose run app-tests
```

Access through: http://0.0.0.0:5000/

## Notes

### Endpoints
- `/`: the root of the app, a welcome message
- `/pokemon_card/{name}`: takes as parameter a Pokemon name, retrieves all the details about a Pokemon and displays some of them (like stats, height, weight, those that will be used in the battle calculations)
- `/pokemon_battle/{first_pokemon}/vs/{second_pokemon}`: takes as parameters two Pokemon names and returns the result of the fight between those two

### Battle winner

The battle winner is decided by a combination of the Pokemon's stats.
I take into consideration the Pokemon's size which is `height * weight`, all the other stats apart from the Pokemon's `HP` and I consider the summary of those as the Pokemon's `strenght`. I multiply the Pokemon's `HP` with its `strength` to calculate the total power of the Pokemon. The winner is decided by the multiplying the size with the power, whichever Pokemon has a greater result is the winner. In case two Pokemons have exactly the same stats or the result of the math is the same, I consider the first Pokemon as the winning one since it has the advantage of attacking first.

### Future improvements
- At the moment each Pokemon is fetched directly from the `pokeapi`. In the future, we could add a database, each time we fetch a Pokemon we could store everything related to it in the database and each time a Pokemon is requested, first look in our database for the Pokemon and in case we don't get a result, only then request the details from the `pokeapi`.
- The battles could be saved in a database as well so that in case we know the outcome of a battle, we won't have to make the calculation again.
- We could add a retry mechanism in case the first call to the `pokeapi` fails limited to a maximum of 3 attempts (probably with some exponential backoff time).
- We could have another endpoint that would trigger a battle with a specific identifier (a uuid) which would return the identifier of the battle. We'd sace this identifier in our database and we could have another endpoint that would take as parameter this identifier and would return the status of the battle (in progress, completed) and the result if it is available. This way we could reduce the latency of our responses since the external calls can delay the response time and making the app functionality async would provide the user with a better experience. Plus, they would be able to see at which state the battle is (in case we decide sometime to expand the app and actually make moves etc. based on the data provided by the `pokeapi`).
