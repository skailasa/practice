"""
Core Alchemical Laboratory
"""
import random

import yaml


def check_reaction(substance_1, substance_2):
    """
    Check whether substance_1 and substance_2 react, simply checks if
        one of the two substances has an 'Anti' prefix and they both
        have the same suffix. i.e. 'AntiA' reacts with 'A'
    :param str substance_1: The first substance
    :param str substance_2: The substance being checked against.
    :return bool: True if a reaction occurs, False otherwise.
    """
    return (
        (substance_1 == "anti" + substance_2) or
        (substance_2 == "anti" + substance_1)
    )


# store all reaction functions in a dict
REACTION_FUNC_DICT = {
    'simple': check_reaction
}


def load_yaml(filepath):
    """
    Returns a yaml parsed using PyYaml.
    :param str filepath: The input filepath.
    :returns data with appropriate datatype:
    """
    with open(filepath) as file_object:
        data = yaml.load(file_object)
    return data


def update_shelves(lower, upper, substance_1, substance_2_index):
    """
    Remove substances from shelves after a reaction.
    :param list[str] lower: The first shelf containing substances
        being checked for reactions.
    :param list[str] upper: The second shelf, containing substances
        being reacted against.
    :param str substance_1: The substance being checked for a reaction,
        is removed from lower post-reaction.
    :param int substance_2_index: The index of the substance being
        checked against for a reaction, is removed from upper
        post-reaction.
    :return tuple[list[str], list[str]]: Return a tuple of both
        shelves containing remaining substances.
    """
    index_1 = lower.index(substance_1)

    lower = lower[:index_1] + lower[index_1+1:]
    upper = upper[:substance_2_index] + upper[substance_2_index+1:]

    return lower, upper


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


class Laboratory:
    """
    Concrete Alchemical Laboratory class.

    Run full experiment, with all possible reactions:

    >>> data = {
    ...     'lower': ['A', 'antiB'],
    ...     'upper': ['antiA', 'C']
    ... }
    >>> lab = Laboratory(data)
    >>> lab.run_experiment()
    (['antiB'], ['C'])
    >>> lab.reaction_count  # count number of reactions
    1
    """

    def __init__(self, substance_data, reaction_type='simple'):
        """
        Initialise object with dict of lists containing both shelves,
            and their respecteive substances.
        :param dict[str, list[str]] substance_data: The two shelf
            standard Lab containing substances and their reactants.
        :param str reaction_type: The type of reaction being checked,
            if no custom reaction is specified, defaults to 'simple',
            which simply checks for a substance against it's
            corresponding anti-substance.
        >>> substance_data = {
        ...         'lower': ['A', 'antiB'],
        ...         'upper': ['antiA', 'C'],
        ...     }
        >>> # defaults to simple reaction
        >>>  lab = Laboratory(substance_data)
        >>> # specify a custom reaction
        >>> lab = Laboratory(substance_data, reaction_type='custom')
        """
        self.check_reaction_func = REACTION_FUNC_DICT[reaction_type]
        self.reaction_count = 0
        self.lower = substance_data['lower']
        self.upper = substance_data['upper']

    def _check_reaction(self, substance_1, substance_2):
        """
        Check reaction using user specified check reaction function.
            Defaults to simple check for direct
            alchemical/anti-alchemical match.
        :param str substance_1: A given substance.
        :param str substance_2: A substance to test substance_1
            against to see if they react.
        :return bool: Return True if reaction occurs, False otherwise.
        """
        return self.check_reaction_func(substance_1, substance_2)

    def _find_possible_targets(self, substance_1, upper):
        """
        Check for possible reaction targets for a substance_1 from
            lower, in another shelf upper.
        :param str substance_1: A given substance.
        :param list[str] upper: The second shelf, containing
            substances being reacted against.
        :return list[str]: List of potential targets for a given
            substance_1 in upper.
        """
        return [
            i for i, target
            in enumerate(upper)
            if self._check_reaction(substance_1, target)
        ]

    def _single_reaction(self):
        """
        Attempt a single reaction from substances in lower and upper
            If a reaction occurs, remove these items from their
            respective shelves, otherwise return the shelves.
        :return tuple[list[str], list[str]]: Return a tuple of both
            shelves containing remaining substances.
        """

        for substance_1 in self.lower:

            possible_targets = self._find_possible_targets(
                substance_1,
                self.upper
            )

            if not possible_targets:
                continue

            else:
                substance_2_index = random.choice(possible_targets)

                return update_shelves(
                    self.lower,
                    self.upper,
                    substance_1,
                    substance_2_index
                )

        return self.lower, self.upper

    def run_experiment(self):
        """
        Run a full experiment, until all possible reactions have occured
            Return both shelves, with reacted substances removed.
        :return dict[list[str], list[str]]: Return a dict of both
            shelves containing remaining substances, with the names
            formatted to 'lower' and 'upper' instead of 'lower' and
            'upper'
        """
        count = 0
        ended = False

        while not ended:
            lower_new, upper_new = self._single_reaction()
            if lower_new != self.lower:
                count += 1

            ended = (
                (lower_new == self.lower) and
                (upper_new == self.upper)
            )

            self.lower, self.upper = lower_new, upper_new

        self.reaction_count += count

        return {'lower': self.lower, 'upper': self.upper}
