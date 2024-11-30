from conftest import *
from page_objects.main import Main
from page_objects.authorization import Authorization
from page_objects.registration import Registration

email = "firstsur1@mail.ru"
password = "Passvv0rd"
url = "https://demo-opencart.ru/index.php?route=account/"


@allure.feature("Тестирование регистрации")
@allure.title("Проверка, того что новая учетная запись может быть успешно зарегистрирована")
def test_1(driver):
    driver.get(url + "register")
    registration = Registration(driver)
    registration.write(Registration.INPUT_FIRSTNAME, "firstname")
    registration.write(Registration.INPUT_LASTNAME, "surname")
    registration.write(Registration.INPUT_EMAIL, email)
    registration.write(Registration.INPUT_TELEPHONE, "88005553535")
    registration.write(Registration.INPUT_PASSWORD, password)
    registration.write(Registration.INPUT_CONFIRM, password)
    registration.click(Registration.BUTTON_SUBSCRIBE)
    registration.click(Registration.BUTTON_INPUT)
    registration.click(Registration.BUTTON_NEXT)


@allure.feature("Тестирование регистрации")
@allure.title("Проверьте, что повторная регистрация с уже существующим логином выдаёт сообщение об ошибке")
def test_2(driver):
    test_1(driver)


@allure.feature("Тестирование функциональности входа в систему")
@allure.title("Проверка успешного входа с корректными учетными данными")
def test_3(driver):
    driver.get(url + "login")
    Authorization(driver).write(Authorization.INPUT_EMAIL, email)
    Authorization(driver).write(Authorization.INPUT_PASSWORD, password)
    Authorization(driver).click(Authorization.BUTTON_LOGIN)


@allure.feature("Тестирование функциональности входа в систему")
@allure.title("Проверьте вход с некорректными учетными данными (например, неправильный логин или пароль)")
def test_4(driver):
    driver.get(url + "login")
    Authorization(driver).write(Authorization.INPUT_EMAIL, email)
    Authorization(driver).write(Authorization.INPUT_PASSWORD, "password")
    Authorization(driver).click(Authorization.BUTTON_LOGIN)


@allure.feature("Тестирование функциональности поиска")
@allure.title("Проверка, что поиск по ключевым словам возвращает правильные результаты")
def test_5(driver):
    Main(driver).write(Main.INPUT_SEARCH, "macbook")
    Main(driver).enter()


@allure.feature("Тестирование функциональности поиска")
@allure.title("Проверка поведение приложения при отсутствии результатов поиска")
def test_6(driver):
    Main(driver).write(Main.INPUT_SEARCH, "kkk")
    Main(driver).enter()
