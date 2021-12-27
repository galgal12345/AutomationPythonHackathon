import pytest


@pytest.mark.usefixtures("my_mobile_starter")
class Test_Mobile:

    def test_01(self):
        print()
