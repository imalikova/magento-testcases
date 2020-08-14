from MagentoPages import LoginHelper


def test_login(browser): #how was browser imported?
    browser = run_login(browser)
    run_logout(browser)


def run_login(browser):
    login_page = LoginHelper(browser)
    login_page.go_to_test_page("https://patriotgaming.com/customer/account/login/")
    login_title = login_page.get_account_page_title()
    assert "LOGIN OR CREATE AN ACCOUNT" == login_title, f"Wrong title:{login_title}"
    register_button = login_page.check_register_button()
    assert register_button, f":{register_button=}"  # assert register button exists
    login_page.insert_login_credentials("imalikova", "Estoyfeliz1234*")
    login_page.click_login()
    assert '/customer/account/' in str(login_page.check_current_page())
    assert 'afinabenpalladen@gmail.com' in str(
        login_page.check_email_visible()), f"Wrong result: {login_page.check_email_visible()}"
    return browser


def run_logout(browser):
    login_page = LoginHelper(browser)
    logout_success = login_page.logout()
    assert "YOU ARE SIGNED OUT" == logout_success, f"Wrong title:{logout_success}"