# def test_a1():
#     assert 5 + 3 == 8

from random import random
import pytest
import sys

class TestClass:
    # @pytest.mark.skip(reason="demonstrating skipping")
    @pytest.mark.skipif(pytest.__version__ > "6.0.0", reason="requires pytest 6.0.0 or lower")
    def test_a2(self):
        print(sys.platform)
        print(pytest.__version__)
        assert 2 * 3 == 6

    # @pytest.mark.skipif(sys.version_info > (3, 7), reason="requires python3.7 or lower")
    @pytest.mark.skipif(random() > 0.5, reason="randomly skipping")
    def test_a3(self):
        assert 1 + 1 == 2