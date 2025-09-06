from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchResultsPage(BasePage):

    result_titles = (By.CSS_SELECTOR, "ul.list-recent-events li h3")

    def get_result_titles(self):
        """Getting the search result titles."""
        titles = self._driver.find_elements(*self.result_titles)
        return [title.text for title in titles]
