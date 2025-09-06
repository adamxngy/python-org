from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class EventsPage(BasePage):

    recent_events = (By.XPATH, "//*[@id='content']/div/section/div/div[1]/ul/li")

    def happening_now_events(self):
        """Finding the events under 'happening now'."""
        elements = self._driver.find_elements(*self.recent_events)
        return [element.text for element in elements]
