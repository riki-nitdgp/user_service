import json


def json_file_to_dict(_file: str) -> dict:
    config = None
    try:
        with open(_file) as config_file:
            config = json.load(config_file)
    except (TypeError, FileNotFoundError, ValueError) as exception:
        print(exception)

    return config
