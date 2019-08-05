import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome('C:\Selenium Driver\chromedriver.exe')
driver.implicitly_wait(10)
driver.maximize_window()

def type_and_enter(element,text):
    element.send_keys(text)
    time.sleep(2)
    element.send_keys(Keys.ENTER)

source = "Mumbai"
destination = "Delhi"

# CREATE A NEW GOOGLE CHROME OBJECT & LOGIN TO makemytrip.com
driver.get('https://www.makemytrip.com/')

# ASSERT WE ARE ON THE CORRECT PAGE
assert "makemytrip" in driver.title.lower()

#selection of round trip redio button
radio_Button = driver.find_element_by_xpath("//*[contains(text(),'Round Trip')]")
radio_Button.click()

# ENTER VALUE FOR "FROM"
from_field = driver.find_element_by_xpath("//input[@value='Delhi']")
from_field.click()
element = WebDriverWait(driver, 60)
type_and_enter(from_field,source)
ActionChains(driver).key_down(Keys.CONTROL).key_up(Keys.CONTROL).perform()
driver.find_element_by_xpath("//div[@class='react-autosuggest__section-container react-autosuggest__section-container--first']//p[@class='font16 appendBottom8'][contains(text(),'Mumbai, India')]")
from_field.send_keys(Keys.ARROW_DOWN)


# ENTER VALUE FOR "TO"
from_field = driver.find_element_by_xpath("//input[@value='Bangalore']")
from_field.click()
element = WebDriverWait(driver, 60)
type_and_enter(from_field,source)
ActionChains(driver).key_down(Keys.CONTROL).key_up(Keys.CONTROL).perform()
from_field.send_keys(Keys.ARROW_DOWN)

# SET DEPART DATE TO PRESENT DAY
depart_field = driver.find_element_by_xpath("//span[contains(text(),'DEPARTURE')]")
depart_field.click()
depart_field = driver.find_element_by_xpath("//div[@class='DayPicker-wrapper']//div[1]//div[3]//div[2]//div[6]//div[1]//p[1]").click()


# SET RETURN DATE TO NEXT DAY
return_field = driver.find_element_by_xpath("//div[@class='DayPicker-Months']//div[2]//div[3]//div[3]//div[4]//div[1]//p[1]").click()

#click on search button
Search_Button = driver.find_element_by_xpath("//a[contains(@class,'primaryBtn font24 latoBlack widgetSearchBtn')]")
Search_Button.click()
time.sleep(20)

driver.quit()
