import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://app.qa.guru/automation-practice-form/'
    browser.config.timeout = 4.0
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--headless=new')
    browser.config.window_width = 1024
    browser.config.window_height = 1366

    yield

    browser.quit()