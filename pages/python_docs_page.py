from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class PythonDocsPage(BasePage):

    title_locator = (By.XPATH, "/html/body/div[3]/div[1]/div/div/h1")

    def is_loaded(self):
        """Check if the 'python docs' button redirects to the correct page."""
        self.wait_until_element_is_visible(self.title_locator)
        return self.find(self.title_locator).is_displayed()
