# def test_a1():
#     assert 5 + 3 == 8

import pytest
import sys

class TestClass:
    @pytest.mark.skip(reason="demonstrating skipping")
    def test_a2(self):
        assert 2 * 3 == 5

    @pytest.mark.skipif(sys.version_info > (3, 7), reason="requires python3.7 or lower")
    def test_a3(self):
        assert 1 + 1 == 2