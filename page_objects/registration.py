from page_objects.base import Base
from selenium.webdriver.common.by import By


class Registration(Base):
    INPUT_FIRSTNAME = (By.CSS_SELECTOR, "#input-firstname")
    INPUT_LASTNAME = (By.CSS_SELECTOR, "#input-lastname")
    INPUT_EMAIL = (By.CSS_SELECTOR, "#input-email")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    INPUT_TELEPHONE = (By.CSS_SELECTOR, "#input-telephone")
    INPUT_CONFIRM = (By.CSS_SELECTOR, "#input-confirm")
    BUTTON_SUBSCRIBE = (By.CSS_SELECTOR, "label.radio-inline:nth-child(1) > input:nth-child(1)")
    BUTTON_INPUT = (By.CSS_SELECTOR, "div.pull-right > input:nth-child(3)")
    BUTTON_NEXT = (By.CSS_SELECTOR, "div.pull-right > input.btn.btn-primary:nth-child(4)")


