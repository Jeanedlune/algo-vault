from trapping_rain_water import trap


def test_basic_case():
    assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6


def test_mixed_heights():
    assert trap([4, 2, 0, 3, 2, 5]) == 9


def test_simple_valley():
    assert trap([2, 0, 2]) == 2


def test_no_water():
    assert trap([1, 2, 3, 4, 5]) == 0


def test_flat_surface():
    assert trap([3, 3, 3, 3]) == 0


def test_empty_list():
    assert trap([]) == 0


def test_single_element():
    assert trap([5]) == 0
