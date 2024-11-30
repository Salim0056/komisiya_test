from selenium.webdriver import ActionChains, Keys

from page_objects.base import Base
from selenium.webdriver.common.by import By


class Main(Base):
    INPUT_SEARCH = (By.XPATH, "//header/div[1]/div[1]/div[2]/div[1]/input[1]")

    def enter(self):
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        self.logger.info("Press 'Enter'")
        return self
