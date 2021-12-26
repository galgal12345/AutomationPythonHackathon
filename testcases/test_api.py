import pytest
from utils.conftest import my_mobile_starter


@pytest.mark.usefixtures("my_mobile_starter")
class Test_Api:

    def test_01(self):
        print()