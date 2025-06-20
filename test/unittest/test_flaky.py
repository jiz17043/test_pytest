from flaky import flaky
from src.function import might_be_unstable

@flaky(max_runs=4, min_passes=1)
def test_might_be_unstable():
    assert might_be_unstable()
