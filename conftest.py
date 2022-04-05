import pytest
from Common import base_page


@pytest.fixture(scope='session')
def driver():
    driver = base_page.chorme_driver()
    yield driver
    base_page.quit(driver)
