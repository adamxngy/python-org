import pytest
from pages.downloads_page import DownloadsPage


@pytest.mark.smoke
@pytest.mark.downloads
def test_latest_python_release_visible(driver):

    text_word = "Python"

    downloads = DownloadsPage(driver)
    downloads.open()

    latest_release_text = downloads.get_latest_release_text()

    assert latest_release_text.startswith(text_word), \
        f"Expected a Python release, got: {latest_release_text}"
