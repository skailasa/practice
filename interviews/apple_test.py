'''Unit tests for apple code test'''
from unittest.mock import patch

import pytest

from .apple import min_distance, sub_array_generator


@pytest.mark.parametrize(
    'colour, colour_data, expected',
    [
        # colour we're looking for at beginning
        ('red', 'red blue blue',
         ([], ['blue', 'blue'])
         )
    ]
)
def test_sub_array_generator(colour, colour_data, expected):
    """Test that we generate correct left/right subarrays """
    result = sub_array_generator(colour, colour_data)
    for left_sub_array, right_sub_array in result:
        assert (left_sub_array, right_sub_array) == expected


@pytest.mark.parametrize(
    'colour_1, colour_2, colour_data, expected',
    [
        # test with provided cases
        ('red', 'blue', 'red red blue red end', 1),
        ('red', 'blue', 'red yellow blue end', 2),
        ('red', 'blue', 'yellow yellow blue yellow yellow red end', 3),
    ]
)
def test_min_distance(colour_1, colour_2, colour_data, expected):
    """Test that the correct minimum distance is found"""
    result = min_distance(colour_1, colour_2, colour_data.split(' '))
    assert result == expected


@pytest.mark.parametrize(
    'colour_1, colour_2, colour_data, error_msg',
    [
        ('red', 'notRealColour', 'red red blue red end',
         'Queried data set with unsupported colours')
    ]
)
def test_min_distance_improper_input(colour_1, colour_2, colour_data, error_msg):
    """
    Test that an error message is raised when you attempt to the
    function with a colour that doesn't exist
    """
    with pytest.raises(Exception) as e_info:
        min_distance(colour_1, colour_2, colour_data)
        assert error_msg in str(e_info.value)

