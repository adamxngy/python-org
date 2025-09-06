import pytest
from pages.documentation_page import DocumentationPage
from pages.home_page import HomePage


class TestDocumentationPage:

    @pytest.mark.smoke
    @pytest.mark.docs
    def test_documentation_search_box_visible(self, driver):

        menu_item = "Documentation"

        nav = HomePage(driver)
        nav.open()
        nav.click_menu_item(menu_item)

        docs = DocumentationPage(driver)

        assert docs.is_docs_button_visible(), "Python docs button not found on Documentation page"

    @pytest.mark.smoke
    @pytest.mark.docs
    @pytest.mark.redirection
    def test_docs_button_redirects(self, driver):

        menu_item = "Documentation"

        nav = HomePage(driver)
        nav.open()
        nav.click_menu_item(menu_item)

        docs = DocumentationPage(driver)
        python_docs_page = docs.go_to_docs_page()

        assert python_docs_page.is_loaded()
