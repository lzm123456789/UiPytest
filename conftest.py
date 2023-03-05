import pytest
from Common import base_page


@pytest.fixture(scope='session')
def driver():
    driver = base_page.chorme_driver()
    yield driver
    base_page.quit(driver)


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")
