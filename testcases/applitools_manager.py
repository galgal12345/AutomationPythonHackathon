import pytest
from applitools.selenium import Eyes, Target, BatchInfo, ClassicRunner


@pytest.fixture(scope="module")
def batch_info():
    """
    Use one BatchInfo for all tests inside module
    """
    return BatchInfo("Some general Test cases name")


@pytest.fixture(name="driver", scope="function")
def driver_setup():
    """
    New browser instance per test and quite.
    """
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield driver
    # Close the browser.
    # driver.quit()


@pytest.fixture(name="runner", scope="session")
def runner_setup():
    """
    One test runner for all tests. Print test results in the end of execution.
    """
    runner = ClassicRunner()
    yield runner
    all_test_results = runner.get_all_test_results()
    print(all_test_results)


@pytest.fixture(name="eyes", scope="function")
def eyes_setup(runner, batch_info):
    """
    Basic Eyes setup. It'll abort test if wasn't closed properly.
    """
    eyes = Eyes(runner)
    # Initialize the eyes SDK and set your private API key.
    eyes.api_key = "Y7YclUHy7uKAB110GYMAC9bTPBHimPnc3wUQ4UyPgBtRs110"
    eyes.configure.batch = batch_info
    yield eyes
    # If the test was aborted before eyes.close was called, ends the test as aborted.
    eyes.abort_if_not_closed()
