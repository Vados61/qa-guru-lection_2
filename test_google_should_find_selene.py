import pytest as pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture(scope="session")
def open_browser():
    browser.config.window_width = 500
    browser.config.window_height = 500
    browser.config.hold_browser_open = True
    browser.open('https://google.com/ncr')
    yield browser
    browser.quit()


def test_find_selene(open_browser):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_negative_search(open_browser):
    browser.element('[name="q"]').clear().type('dflkjfgklj').press_enter()
    browser.element('body').should(have.text('No results containing all your search terms were found'))
