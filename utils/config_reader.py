import json


def read_config():
    """Read configuration file and validate values"""
    with open('config.json') as config_file:
        config = json.load(config_file)

    assert config['browser'].lower() in ['chrome', 'firefox', 'edge'], "Unsupported browser"
    assert isinstance(config['implicit_wait'], int) and config['implicit_wait'] > 0, "Invalid implicit_wait value"

    return config
