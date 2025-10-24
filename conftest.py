import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from utils.config_reader import read_config

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Get the outcome of the test
    outcome = yield
    report = outcome.get_result()

    # Run only when a test fails
    if report.when == "call" and report.failed:
        # Get the browser fixture if it exists
        browser = item.funcargs.get("browser")
        if browser:
            # Take a screenshot
            screenshot = browser.get_screenshot_as_png()
            allure.attach(
                screenshot,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )


@pytest.fixture(scope='session')
def config():
    """Load config.json once per session"""
    return read_config()

@pytest.fixture
def browser(config, request):
    """Create WebDriver instance based on config"""
    browser_name = config['browser'].lower()

    if browser_name == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser_name == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.implicitly_wait(config['implicit_wait'])
    yield driver
    driver.quit()
