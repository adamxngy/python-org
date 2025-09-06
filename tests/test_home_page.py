import pytest
from selenium.webdriver.support.wait import WebDriverWait
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from selenium.webdriver.support import expected_conditions as EC


class TestHomePage:

    @pytest.mark.smoke
    @pytest.mark.home
    @pytest.mark.search
    def test_search(self, driver):

        search_term = "python"

        homepage = HomePage(driver)
        homepage.open()
        homepage.search(search_term)

        result = SearchResultsPage(driver)
        WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located(result.result_titles))
        titles = result.get_result_titles()

        assert any(search_term in title.lower() for title in titles),\
            f"Expected result with 'pytest', but got: {titles}"

    @pytest.mark.smoke
    @pytest.mark.home
    @pytest.mark.navigation
    def test_main_menu_items_visible(self, driver):

        nav = HomePage(driver)
        nav.open()

        for item in nav.menu_items.keys():
            assert nav.is_menu_item_visible(item), f"{item} menu item is not visible"
