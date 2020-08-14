# import pytest
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
#
#
#
# @pytest.fixture(scope="session")
# def browser():
#     driver = webdriver.Chrome(executable_path="../browsers/chromedriver")
#     driver.implicitly_wait(10)
#     driver.maximize_window() # can I add this here?
#     yield driver
#     driver.quit()
#
#
# def test_login(browser):
#     # login_page = LoginHelper(browser)
#     # login_page.go_to_test_page("https://patriotgaming.com/customer/account/login/")
#     # login_title = login_page.get_account_page_title()
#     # assert login_title == "LOGIN OR CREATE AN ACCOUNT", f"Wrong title:{login_title}"
#     # register_button = login_page.check_register_button()
#     # assert register_button, f":{register_button=}"  # assert register button exists
#     # login_page.insert_login_credentials("imalikova", "Estoyfeliz1234*")
#     # login_page.click_login()
#     # assert '/customer/account/' in str(login_page.check_my_account_page())
#     # assert 'afinabenpalladen@gmail.com' in str(login_page.check_email_visible()), f"Wrong result: {login_page.check_email_visible()}"
#
#     browser = run_login(browser)
#     run_logout(browser)
#
#
# def run_login(browser):
#     login_page = LoginHelper(browser)
#     login_page.go_to_test_page("https://patriotgaming.com/customer/account/login/")
#     login_title = login_page.get_account_page_title()
#     assert "LOGIN OR CREATE AN ACCOUNT" == login_title, f"Wrong title:{login_title}"
#     register_button = login_page.check_register_button()
#     assert register_button, f":{register_button=}"  # assert register button exists
#     login_page.insert_login_credentials("imalikova", "Estoyfeliz1234*")
#     login_page.click_login()
#     assert '/customer/account/' in str(login_page.check_my_account_page())
#     assert 'afinabenpalladen@gmail.com' in str(
#         login_page.check_email_visible()), f"Wrong result: {login_page.check_email_visible()}"
#     return browser
#
#
# def run_logout(browser):
#     login_page = LoginHelper(browser)
#     logout_success = login_page.logout()
#     assert "YOU ARE SIGNED OUT" == logout_success, f"Wrong title:{logout_success}"
#
#
#
# #locators
#
#
# class LoginLocators:
#     REGISTER_BUTTON = (By.CSS_SELECTOR, "div .create")
#     LOGIN_FIELD = (By.ID, "email")
#     PASSWORD_FIELD = (By.ID, "pass")
#     LOGIN_BUTTON = (By.ID, "send2")
#     ACCOUNT_EMAIL = (By.XPATH, "//div[@class='box box-information']/div/p")
#
#
# class LogoutLocators:
#     MY_ACCOUNT_MENU = (By.CSS_SELECTOR, ".header-block_account a")
#     MY_ACCOUNT_MENU_OPTION = (By.CSS_SELECTOR, ".header-block_account li:nth-child(1)")
#     LOG_OUT_MENU_OPTION = (By.CSS_SELECTOR, ".header-block_account li:nth-child(2) > a")
#     SIGNED_OUT_TEXT = (By.CSS_SELECTOR, "H1")
#
#
# class BasePage:
#
#     def __init__(self, driver):
#         self.driver = driver
#         # self.base_url = "https://patriotgaming.com/"
#
#     def find_element(self, locator, time=10):
#         return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
#                                                       message=f"Can't find element by locator {locator}")
#
#     def find_elements(self, locator, time=10):
#         return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
#                                                       message=f"Can't find elements by locator {locator}")
#
#     def go_to_test_page(self, url):
#         return self.driver.get(url)
#
#     def check_my_account_page(self):
#         return self.driver.current_url
#
#     # pageobject
#
#
# class LoginHelper(BasePage):
#
#     def get_account_page_title(self):
#         return self.driver.title
#
#     def check_register_button(self):
#         return self.find_element(LoginLocators.REGISTER_BUTTON)
#
#     def insert_login_credentials(self, login, password):
#
#         login_field = self.find_element(LoginLocators.LOGIN_FIELD)
#         login_field.send_keys(login)
#         password_field = self.find_element(LoginLocators.PASSWORD_FIELD)
#         password_field.send_keys(password)
#         return login_field, password_field
#
#     def click_login(self):
#         return self.find_element(LoginLocators.LOGIN_BUTTON).click()
#
#     def check_email_visible(self):
#         return self.find_element(LoginLocators.ACCOUNT_EMAIL).text
#
#     def logout(self):
#         my_account = self.find_element(LogoutLocators.MY_ACCOUNT_MENU)
#         my_account_2 = self.find_element(LogoutLocators.MY_ACCOUNT_MENU_OPTION)
#         log_out = self.find_element(LogoutLocators.LOG_OUT_MENU_OPTION)
#         actions = ActionChains(self.driver)
#         actions.move_to_element(my_account).move_to_element(my_account_2).move_to_element(log_out).click().perform()
#         return self.find_element(LogoutLocators.SIGNED_OUT_TEXT).text
#
