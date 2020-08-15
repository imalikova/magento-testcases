from selenium import webdriver


# def setup():
#
#     global driver
#
#     driver = webdriver.Chrome(executable_path="../browsers/chromedriver")
#     driver.implicitly_wait(10)
#     driver.maximize_window()
#     # driver.get("https://patriotgaming.com/customer/account/login/")
#     # driver.find_element_by_id("email").send_keys("imalikova")
#     # driver.find_element_by_id("pass").send_keys("Estoyfeliz1234*")
#     # driver.find_element_by_id("send2").click()
#     # driver.implicitly_wait(10)
#     #
#     # account_email = driver.find_element_by_xpath("//div[@class='box box-information']/div/p")
#     # print(account_email)
#     # print(account_email.text)
#
#     driver.get("https://patriotgaming.com/customer/account/logoutSuccess/")
#     logout_page = driver.find_element_by_css_selector("H1").text
#     print(logout_page)
#
#
# setup()


from selenium import webdriver

expected_links_list = ["patriotgaming.com", "/aboutus", "/contact", "/resources", "/checkout/cart", "/inv", "/gaming,"
                           "/shop-by-game", "/repair-services", "/refurbished-casino-parts", "/bill-validators",
                           "/touch-screens-monitors", "/printers", "/gaming", "/cleaning-maintenance", "/electronic-components",
                           "/lighting", "/tools", "/atm-kiosk", "/patriot-items", "/refurbished-casino-parts", "/seating",
                           "/electrical-tripp-lite", "/table-game-products", "/player-tracking", "/oem-product-showcase",
                           "/personal-protection-equipment", "patriotgaming.com", "/aboutus", "/contact", "/resources",
                           "/contact", "/terms-and-conditions", "/sitemap"]


def find_links():

    locators_list = []  # create empty list

    driver = webdriver.Chrome(executable_path="../browsers/chromedriver")
    driver.implicitly_wait(10)
    driver.maximize_window()

    driver.get("https://patriotgaming.com/")
    links_list = driver.find_elements_by_css_selector('a[href]')

    print(links_list)

    for index, link in enumerate(links_list):
        if link.text:
            print(index, link.text, link.get_attribute("href"), sep=";")
            # locators_list.append(f"{link.text}, {link.get_attribute('href').split('?')}")
            # locators_list.append(f"{link.text}, {link.get_attribute('href').split('?')[0]}")
            # locators_list.append(f"{link.text}, {link.get_attribute('href').split('?')[0]}")
            locators_list.append(f'''a[href*="{link.get_attribute('href').split('?')[0][25:]}"]''')

    print(locators_list)
    return driver, locators_list


def click_links(driver, locators_list):

    url_list = []

    for locator in locators_list:
        try:
            driver.find_element_by_css_selector(locator).click()
            driver.implicitly_wait(5)
            print(driver.current_url)
            url_list.append(driver.current_url)
            driver.get("https://patriotgaming.com/")
            driver.implicitly_wait(5)

        except:
            print(locator, "not clicked")


    return url_list


def check_links(driver, url_list):


    expected_links_list.remove()


driver, locators_list = find_links() # saved returned result in function
url_list = click_links(driver, locators_list)
check_links(driver, url_list)
