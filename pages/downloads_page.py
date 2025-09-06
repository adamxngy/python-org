from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DownloadsPage(BasePage):

    url = "https://www.python.org/downloads/"
    latest_release = (By.CSS_SELECTOR, ".release-number a")

    def open(self):
        """Opening the 'downloads' page."""
        self.open_url(self.url)

    def get_latest_release_text(self):
        """Finding the latest release of python and returning its text."""
        element = self.find(self.latest_release)
        return element.text
