from selenium import webdriver


driver = webdriver.Chrome(executable_path="../browsers/chromedriver")
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://patriotgaming.com/")
driver.find_element_by_css_selector('a[href*="/bill-validators.html"]').click()




