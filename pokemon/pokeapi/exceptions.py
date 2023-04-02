class PokemonClientException(BaseException):
    pass


class ServerError(PokemonClientException):
    pass


class ClientError(PokemonClientException):
    pass


class ValidationError(PokemonClientException):
    pass
