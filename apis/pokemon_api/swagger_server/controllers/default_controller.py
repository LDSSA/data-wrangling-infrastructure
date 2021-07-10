import connexion
import json
import os
import six


from swagger_server import util


# Loading the data
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f'{dir_path}/../data/pokemon.json', 'r') as f:
    POKEMON = json.load(f)

with open(f'{dir_path}/../data/moves.json', 'r') as f:
    MOVES = json.load(f)


def moves_get(name=None, power=None, accuracy=None):  # noqa: E501
    """Gets information about one or more Pokemon attack moves!

     # noqa: E501

    :param name: Name of the move to get. If ommited, at least one of the other filters must be present.
    :type name: str
    :param power: Minimum power of the move. If ommited, at least one of the other filters must be present.
    :type power: int
    :param accuracy: Minimum accuracy of the move. If ommited, at least one of the other filters must be present.
    :type accuracy: int

    :rtype: List[object]
    """
    if name is None and power is None and accuracy is None:
        return "At least one of the parameters can't be null", 400 

    filtered_moves = MOVES
    if name:
        filtered_moves = [
            move
            for move in filtered_moves
            if str(move['ename']) == name
        ]
    if power:
        filtered_moves = [
            move
            for move in filtered_moves
            if move.get('power', 0) is not None and move.get('power', 0) >= power
        ]
    if accuracy:
        filtered_moves = [
            move
            for move in filtered_moves
            if move.get('accuracy', 0) is not None and move.get('accuracy', 0) >= accuracy
        ]

    return filtered_moves


def pokemon_all_get():  # noqa: E501
    """Gets information about all Pokemon.

     # noqa: E501


    :rtype: List[object]
    """
    return POKEMON


def pokemon_get(name, exact=None, poke_type=None):  # noqa: E501
    """Gets information about one or more Pokemon.

     # noqa: E501

    :param name: Name of the Pokemon to get.
    :type name: str
    :param exact: Whether to match the name exactly, or to search as a substring on the Pokemon names.
    :type exact: bool
    :param poke_type: Filter by Pokemon type.
    :type poke_type: str

    :rtype: List[object]
    """

    if not exact:
        filtered_pokemon = [
            pokemon
            for pokemon in POKEMON
            if name in pokemon["name"]["english"]
        ]
    else:
        filtered_pokemon = [
            pokemon
            for pokemon in POKEMON
            if pokemon["name"]["english"] == name
        ]
    
    if poke_type:
        filtered_pokemon = list(filter(
            lambda pokemon: poke_type in pokemon["type"], filtered_pokemon)
        )

    return filtered_pokemon