from selenium.webdriver.common.by import By


class LoginLocators:
    REGISTER_BUTTON = (By.CSS_SELECTOR, "div .create")
    LOGIN_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "pass")
    LOGIN_BUTTON = (By.ID, "send2")
    ACCOUNT_EMAIL = (By.XPATH, "//div[@class='box box-information']/div/p")



class LogoutLocators:
    MY_ACCOUNT_MENU = (By.CSS_SELECTOR, ".header-block_account a")
    MY_ACCOUNT_MENU_OPTION = (By.CSS_SELECTOR, ".header-block_account li:nth-child(1)")
    LOG_OUT_MENU_OPTION = (By.CSS_SELECTOR, ".header-block_account li:nth-child(2) > a")
    SIGNED_OUT_TEXT = (By.CSS_SELECTOR, "H1")