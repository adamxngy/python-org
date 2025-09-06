from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

DEFAULT_WAIT = 10


class BasePage:

    def __init__(self, driver: WebDriver, wait_time: int = DEFAULT_WAIT):
        """
        :param wait_time: Default wait time (in seconds) for element conditions.
        """
        self._driver = driver
        self._wait_time = wait_time

    @property
    def current_url(self) -> str:
        """Return the current URL of the browser."""
        return self._driver.current_url

    def open_url(self, url: str):
        """Navigate to a specific URL."""
        self._driver.get(url)

    def find(self, locator: tuple) -> WebElement:
        """Find a web element on the page."""
        return self._driver.find_element(*locator)

    def type(self, locator: tuple, text: str, time: int = DEFAULT_WAIT):
        """Wait until the element is visible, then type text into it."""
        self.wait_until_element_is_visible(locator, time)
        self.find(locator).send_keys(text)

    def click(self, locator: tuple, time: int = DEFAULT_WAIT):
        """Wait until the element is clickable, then click it."""
        self.wait_until_element_is_visible(locator, time)
        self.find(locator).click()

    def wait_until_element_is_visible(self, locator: tuple, time: int = DEFAULT_WAIT):
        """Wait until the element is visible on the page."""
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locator))

    def is_displayed(self, locator: tuple) -> bool:
        """Check if the element is present and visible on the page."""
        try:
            return self.find(locator).is_displayed()
        except NoSuchElementException:
            return False

    def get_text(self, locator: tuple, time: int = DEFAULT_WAIT) -> str:
        """Wait until the element is visible, then return its text."""
        self.wait_until_element_is_visible(locator, time)
        return self.find(locator).text

    def wait_until_element_is_clickable(self, locator: tuple, time: int = DEFAULT_WAIT):
        """Wait until the element is clickable."""
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.element_to_be_clickable(locator))
