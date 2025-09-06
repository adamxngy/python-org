import pytest
from pages.events_page import EventsPage
from pages.home_page import HomePage


@pytest.mark.events
def test_upcoming_events_listed(driver):

    menu_item = "Events"

    nav = HomePage(driver)
    nav.open()
    nav.click_menu_item(menu_item)

    events = EventsPage(driver)
    upcoming = events.happening_now_events()

    assert len(upcoming) > 0, "Expected at least one 'happening now' event"
