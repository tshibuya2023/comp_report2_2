import pytest
from src.solution import fibonacci

@pytest.mark.timeout(100)
def test_all():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55
    assert fibonacci(15) == 610
