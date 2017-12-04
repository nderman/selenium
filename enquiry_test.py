from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import datetime
from dateutil.relativedelta import relativedelta
startDate = datetime.datetime.now() + relativedelta(years=2)
endDate = startDate + relativedelta(days=2)

# Create a new instance of the Firefox driver
driver = webdriver.PhantomJS()

# go to the google home page
driver.get("https://www.travelground.com/accommodation/karoo-ground-selenium-test/book?instant=no")
driver.execute_script ("document.getElementById('dpd1').removeAttribute('readonly',0);");
driver.execute_script ("document.getElementById('dpd2').removeAttribute('readonly',0);");
# driver.execute_script ("document.getElementById('dpd1').val('15 Dec 2017');");

# the page is ajaxy so the title is originally this:
print (driver.title)

# find the element that's name attribute is q (the google search box)
inputElement = driver.find_element_by_id("dpd1")
inputElement.send_keys(str(startDate.strftime("%d")),' ',str(startDate.strftime("%b")),' ',str(startDate.strftime("%Y")))
inputElement.send_keys(Keys.RETURN)

inputElement = driver.find_element_by_id("dpd2")
inputElement.send_keys(str(endDate.strftime("%d")),' ',str(endDate.strftime("%b")),' ',str(endDate.strftime("%Y")))
inputElement.send_keys(Keys.RETURN)



select = Select(driver.find_element_by_class_name("room-select"))
select.select_by_visible_text("1")
select = Select(driver.find_element_by_class_name("adult_count"))
select.select_by_visible_text(str(datetime.datetime.now().hour))

inputElement = driver.find_element_by_id("firstname")
inputElement.send_keys("Test")
inputElement = driver.find_element_by_id("surname")
inputElement.send_keys("Test")
inputElement = driver.find_element_by_id("email")
inputElement.send_keys("neal+seleniumtest@travelground.com")
inputElement = driver.find_element_by_id("cellphone")
inputElement.send_keys("1111111111")

driver.find_element_by_id('action_button').click()

try:
	WebDriverWait(driver, 10).until(EC.title_contains("Successful Enquiry"))
	print (driver.title)
finally:
	pass
	driver.quit()

