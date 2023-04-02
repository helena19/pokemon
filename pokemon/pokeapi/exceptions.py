class PokemonClientException(BaseException):
    pass


class ServerError(PokemonClientException):
    pass


class ClientError(PokemonClientException):
    pass


class ResourceNotFound(PokemonClientException):
    pass


class ValidationError(PokemonClientException):
    pass
