from BaseApp import BasePage
from selenium.webdriver import ActionChains
from Locators import LoginLocators
from Locators import LogoutLocators


class LoginHelper(BasePage):

    def get_account_page_title(self):
        return self.driver.title

    def check_register_button(self):
        return self.find_element(LoginLocators.REGISTER_BUTTON)

    def insert_login_credentials(self, login, password):

        login_field = self.find_element(LoginLocators.LOGIN_FIELD)
        login_field.send_keys(login)
        password_field = self.find_element(LoginLocators.PASSWORD_FIELD)
        password_field.send_keys(password)
        return login_field, password_field

    def click_login(self):
        return self.find_element(LoginLocators.LOGIN_BUTTON).click()

    def check_email_visible(self):
        return self.find_element(LoginLocators.ACCOUNT_EMAIL).text

    def logout(self):
        my_account = self.find_element(LogoutLocators.MY_ACCOUNT_MENU)
        my_account_2 = self.find_element(LogoutLocators.MY_ACCOUNT_MENU_OPTION)
        log_out = self.find_element(LogoutLocators.LOG_OUT_MENU_OPTION)
        actions = ActionChains(self.driver)
        actions.move_to_element(my_account).move_to_element(my_account_2).move_to_element(log_out).click().perform()
        return self.find_element(LogoutLocators.SIGNED_OUT_TEXT).text



