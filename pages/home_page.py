from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):

    url = "https://www.python.org/"
    search_input_locator = (By.ID, "id-search-field")
    submit_button = (By.ID, "submit")
    menu_items = {
        "About": (By.LINK_TEXT, "About"),
        "Downloads": (By.LINK_TEXT, "Downloads"),
        "Documentation": (By.LINK_TEXT, "Documentation"),
        "Community": (By.LINK_TEXT, "Community"),
        "Success Stories": (By.LINK_TEXT, "Success Stories"),
        "News": (By.LINK_TEXT, "News"),
        "Events": (By.LINK_TEXT, "Events"),
    }

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        """Opening the home page."""
        super().open_url(self.url)

    def search(self, term):
        """Searching for a term."""
        super().type(self.search_input_locator, term)
        super().click(self.submit_button)

    def is_menu_item_visible(self, name):
        """Checking if a menu item is visible in the navigation."""
        locator = self.menu_items[name]
        return self.find(locator).is_displayed()

    def click_menu_item(self, name):
        """Clicking on the menu item."""
        locator = self.menu_items[name]
        self.click(locator)
