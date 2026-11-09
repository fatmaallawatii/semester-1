import pytest

def test_floats_approx():
    assert (0.1 + 0.3) == pytest.approx(0.4)

def test_floats_equals():
    # this test will fail
    assert (0.1 + 0.3) == 0.4
