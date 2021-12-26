import pytest
from utils.conftest import my_web_starter


@pytest.mark.usefixtures("my_web_starter")
class Test_Web:

    def test_01(self):
        print()