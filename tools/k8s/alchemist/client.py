import argparse

import requests
import yaml


def load_yaml(filepath):
    """
    Returns a yaml parsed using PyYaml.
    :param str filepath: The input filepath.
    :returns data with appropriate datatype:
    """
    with open(filepath) as file_object:
        data = yaml.load(file_object)
    return data


def load_substance_data(filepath):
    """
    Parses input YAML filepath into dtype supported by Laboratory.
    :param str filepath: The input YAML filepath.
    :returns dict[str, list[str]]: The substance data in a format
        supported by Laboratory class.
    """
    data = load_yaml(filepath)
    if not isinstance(data, dict):
        raise TypeError(
            'Substances must be in YAML dict of lists! In format '
            '{"lower": [...], "upper": [...]}'
        )
    elif len(data) != 2:
        raise TypeError(
            'Wrong number of shelves! Only standard two shelf labs '
            'supported'
        )

    elif {'lower', 'upper'}.intersection(
            set(data.keys())) != {'lower', 'upper'}:
        raise TypeError(
            "Wrong format of input YAML, must contain dict[lists] with "
            "keys 'upper' and 'lower' corresponding to upper and lower "
            "shelves."
        )

    return data


def parse_cl_arguments():
    """
    Parse command line arguments
    """
    help_text = "The command line interface for alchemist, returns the \n" \
                "final state of the upper and lower shelves after running \n" \
                "a full experiment, i.e. all reactions possible for a \n" \
                "given laboratory setup."
    parser = argparse.ArgumentParser(help_text)

    parser.add_argument(
        'filepath',
        type=str,
        help='The filepath of your laboratory file, must be in yaml.'
    )

    return parser.parse_args()    


def main():
    args = parse_cl_arguments()
    filepath = args.filepath 
    substance_data = load_substance_data(filepath)
    res = requests.post('http://localhost:5000/', json=substance_data)
    
    if res.ok:
        print(res.json())


if __name__ == "__main__":
    main()
