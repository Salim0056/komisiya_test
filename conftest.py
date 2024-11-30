import datetime
import logging
import os

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--log_level", action="store", default="INFO")


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")
    log_level = request.config.getoption("--log_level")
    url = "https://demo-opencart.ru/"

    if not os.path.exists("log"):
        os.makedirs("log")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"log/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info(
        "===> Test %s started at %s" % (
            request.node.name, datetime.datetime.now()
        )
    )

    if browser_name == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise Exception("Driver not supported")
    allure.attach(
        name=driver.session_id,
        body=driver.current_url,
        attachment_type=allure.attachment_type.JSON,
    )

    driver.maximize_window()
    driver.get(url)
    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name

    logger.info("Browser %s started" % browser_name)

    def fin():
        driver.quit()
        logger.info(
            "===> Test %s finished at %s" % (request.node.name, datetime.datetime.now())
        )

    request.addfinalizer(fin)
    return driver
