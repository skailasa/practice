"""
Tests for laboratory objects.
"""
import os
from unittest.mock import patch

import pytest

from alchemist.laboratory import load_yaml
from alchemist.laboratory import update_shelves
from alchemist.laboratory import load_substance_data
from alchemist.laboratory import check_reaction
from alchemist.laboratory import Laboratory


HERE = os.path.abspath(os.path.dirname(__file__))
FIXTURE_FILEPATH = os.path.join(HERE, 'fixtures.yml')


def test_load_yaml():
    """
    Test the loading of a yaml file into a dict.
    """

    result = load_yaml(FIXTURE_FILEPATH)

    assert result == {'test': ['a', 'b', 'c']}


@pytest.mark.parametrize(
    "lower, upper, substance_1, substance_2_index, expected",
    [
        (
            ["a"],
            ["antia"],
            "a",
            0,
            ([], [])

        )
    ]
)
def test_update_shelves(
        lower, upper, substance_1, substance_2_index, expected):
    """
    Test function to update two shelves after a reaction.
    """
    result = update_shelves(lower, upper, substance_1, substance_2_index)

    assert result == expected


@pytest.mark.parametrize(
    "substance_1, substance_2, expected",
    [
        # Test substances which react
        ('a', 'antia', True),
        # Test for expected behaviour with substance named anti
        ('antianti', 'anti', True),
        # Substances which don't react
        ('a', 'b', False),
        ('a', 'antiB', False),
        # Test for expected behaviour with substance named anti
        ('anti', 'anti', False)
    ]
)
def test_check_reaction(substance_1, substance_2, expected):
    """
    Test reaction checker
    """
    result = check_reaction(substance_1, substance_2)

    assert result == expected


@pytest.mark.parametrize(
    "test_input, error_message",
    [
        # incorrect number of shelves
        (
            {'lower': [], 'upper': [], 'shelf_3': []},
            'Wrong number of shelves! Only standard two shelf labs '
            'supported'
        ),
        # incorrect format, i.e. not a dict of lists
        (
            [1, 2, 3],
            'Substances must be in YAML dict of lists! In format '
            '{"lower": [...], "upper": [...]}'
        ),
        # incorrect format, unsupported key names for shelves
        (
            {'shelf_a': [], 'shelf_b': []},
            'Wrong format of input YAML, must contain dict[lists] with '
            'keys "upper" and "lower" corresponding to upper and lower '
            'shelves.'
        )
    ]
)
def test_load_substance_data_raises_type_errors(test_input, error_message):
    """
    Test parsing of a YAML file containing:
        (i) Too many shelves
        (ii) Data in an unsupported format
    """

    with patch('alchemist.laboratory.load_yaml', return_value=test_input) as _:

        with pytest.raises(Exception) as e_info:
            load_substance_data('fake.yml')
            assert error_message in str(e_info.value)


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (
            {'lower': ['a'], 'upper': ['b']},
            {'lower': ['a'], 'upper': ['b']},
        )
    ]
)
def test_load_substance_data(test_input, expected):
    """
    Test that substance data is loaded correctly if YAML input in right
        format.
    """
    with patch('alchemist.laboratory.load_yaml', return_value=test_input) as _:
        result = load_substance_data('fake.yml')
        assert result == expected


@pytest.mark.parametrize(
    "test_input",
    [
        {'lower': ['a', 'b'], 'upper': ['antia', 'antib']}
    ]
)
def test_laboratory_instantiation(test_input):
    """
    Test that a Laboratory object is properly instantiated when input
        with with some substance data.
    """
    lab = Laboratory(test_input)

    assert hasattr(lab, 'check_reaction_func')
    assert hasattr(lab, 'reaction_count')
    assert hasattr(lab, 'lower')
    assert hasattr(lab, 'upper')


def test_improper_laboratory_instantiation():
    """
    Test that an error is raised if a Laboratory object is not
        correctly instantiated.
    """
    error_message = "TypeError: __init__() missing 1 required positional" \
                    " argument: 'substance_data'"

    with pytest.raises(Exception) as e_info:
        Laboratory()
        assert error_message in str(e_info.value)


@pytest.mark.parametrize(
    "test_input, test_substance, expected",
    [
        # simple case with only one possible target
        (
            {'lower': ['a', 'b'], 'upper': ['antia', 'antib']},
            'a',
            [0]
        ),
        # case where there are multiple possible targets
        (
            {'lower': ['a', 'b'], 'upper': ['antia', 'antia']},
            'a',
            [0, 1]
        ),
        # case where there are no possible targets
        (
            {'lower': ['a', 'b'], 'upper': ['c', 'd']},
            'a',
            []
        )
    ]
)
def test_laboratory_find_possible_targets(
        test_input, test_substance, expected):
    """
    Test that we the find_possible_targets method with different cases.
        Does so by asserting that the set of results of potential
        targets overlaps with what we expect, accounting for potentially
        random target selection with multiple possible targets.
    """
    lab = Laboratory(test_input, reaction_type='simple')

    upper = lab.upper

    result = lab._find_possible_targets(test_substance, upper)

    if expected:
        assert set(result).intersection(set(expected))
    else:
        assert result == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (
            {'lower': ['a', 'c'], 'upper': ['antia', 'antib']},
            (['c'], ['antib'])
        )
    ]
)
def test_laboratory_single_reaction(test_input, expected):
    """
    Test that a single reaction is correctly computed, with the shelves
        updated accordingly.
    """
    lab = Laboratory(test_input)

    result = lab._single_reaction()

    assert result == expected


@pytest.mark.parametrize(
    "test_input, expected_count, expected_output",
    [
        # simple case, where reactants exist
        (
            {'lower': ['a', 'b'], 'upper': ['antia', 'antib']},
            2,
            {'lower': [], 'upper': []}
        ),
        # more complex cases, where one/both shelves are empty
        (
            {'lower': ['a', 'b'], 'upper': []},
            0,
            {'lower': ['a', 'b'], 'upper': []}
        ),
        (
            {'lower': [], 'upper': []},
            0,
            {'lower': [], 'upper': []}
        )
    ]
)
def test_laboratory_run_experiment(
        test_input, expected_count, expected_output):
    """
    Check that a full experiment is run, until all substances which can
        react have done so. Check that the number of reactions is
        computed correctly.
    """
    lab = Laboratory(test_input)

    result = lab.run_experiment()

    assert lab.reaction_count == expected_count
    assert result == expected_output
