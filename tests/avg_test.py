# use pytests 
# to run: python3 -m pytest

import pytest
from src.main import avg_finder

def check_avg_finder():
    avg=6
    arr = [8, 9, 1]
    return avg_finder(arr) == avg

@pytest.mark.run(order=1)
def test_avg():
    assert check_avg_finder() # continues running if statement true