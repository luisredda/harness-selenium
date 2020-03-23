from selenium import webdriver

#  ChromeOptions
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox') # required when running as root user. otherwise you would get no sandbox errors.
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.google.com')
#print(driver.title)
