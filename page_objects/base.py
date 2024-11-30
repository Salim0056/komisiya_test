import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class Base:
    def __init__(self, driver, wait=10):
        self.driver = driver
        self.logger = driver.logger
        self.wait = WebDriverWait(self.driver, wait)
        self.className = self.__class__.__name__
        self.logger.info(f"{self.className} initialized")

    def is_tuple(self, element_locator):
        if isinstance(element_locator, tuple):
            return self.wait.until(ec.presence_of_element_located(*element_locator))
        else:
            return self.wait.until(ec.presence_of_element_located(element_locator))

    def element_name(self, element):
        for name, value in vars(self.__class__).items():
            if isinstance(value, (list, tuple)) and element in value:
                return f"{name}[{value.index(element)}]"
            elif value == element:
                return name
        return str(element)

    def click(self, element_locator):
        try:
            element_name = self.element_name(element_locator)
            self.wait.until(ec.element_to_be_clickable(element_locator)).click()
            self.logger.info(f"{self.className}: Clicked on '{element_name}'")
        except Exception as e:
            self.logger.error(f"Error clicking on element: {e}")
            raise e

    def _input(self, element_locator, value):
        try:
            element = self.wait.until(ec.presence_of_element_located(element_locator))
            element_name = self.element_name(element_locator)
            element.clear()
            element.send_keys(value)
            self.logger.info(f"{self.className}: Entered '{value}' into '{element_name}'")
        except Exception as e:
            self.logger.error(f"Error entering text into element: {e}")
            raise e

    def write(self, element, value):
        self.click(element)
        self._input(element, value)
        return self
