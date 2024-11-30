from page_objects.base import Base
from selenium.webdriver.common.by import By


class Authorization(Base):
    INPUT_EMAIL = (By.CSS_SELECTOR, "#input-email")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    BUTTON_LOGIN = (By.CSS_SELECTOR, "form:nth-child(3) > input.btn.btn-primary:nth-child(3)")
