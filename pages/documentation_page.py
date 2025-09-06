from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.python_docs_page import PythonDocsPage


class DocumentationPage(BasePage):

    docs_button_locator = (By.XPATH, "//*[@id='touchnav-wrapper']/header/div/div[2]/div/p[3]/a")

    def is_docs_button_visible(self):
        """Checks if the 'python docs' button is visible."""
        return self.find(self.docs_button_locator).is_displayed()

    def go_to_docs_page(self):
        """Redirecting to the 'python docs' page."""
        self.find(self.docs_button_locator).click()
        return PythonDocsPage(self._driver)
