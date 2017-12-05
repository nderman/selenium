from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import time
import datetime
from dateutil.relativedelta import relativedelta
startDate = datetime.datetime.now() + relativedelta(years=2)+relativedelta(days= 11)
endDate = startDate + relativedelta(days=2)

# Create a new instance of the Firefox driver
driver = webdriver.PhantomJS()
#driver = webdriver.Firefox()

startDateString = '"'+ str(startDate.strftime("%d"))+' '+ str(startDate.strftime("%b"))+' '+ str(startDate.strftime("%Y")) + '"'
endDateString = '"'+ str(endDate.strftime("%d"))+' '+ str(endDate.strftime("%b"))+' '+ str(endDate.strftime("%Y")) + '"'

# go to the google home page
# driver.get("https://m.travelground.com/accommodation/karoo-ground-selenium-test/enquiry")
driver.get("http://m.tg.n-al.vm/accommodation/karoo-ground-selenium-test/enquiry")

driver.execute_script ("document.getElementById('enquiry-start-date').setAttribute('data', 'date: "+ startDateString +"' );")
driver.execute_script ("document.getElementById('enquiry-end-date').setAttribute('data', 'date: "+ endDateString +"');")

driver.execute_script ("startDate.setDate("+ startDateString +" );")
driver.execute_script ("endDate.setDate("+ endDateString +" );")


# the page is ajaxy so the title is originally this:
print (driver.title)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"spinner-container")))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME,"room-select")))

select = Select(driver.find_element_by_class_name("room-select"))
select.select_by_visible_text("1")
select = Select(driver.find_element_by_class_name("adult-select"))
select.select_by_visible_text(str(datetime.datetime.now().hour))

driver.find_element_by_class_name('btn-continue').click()

print ('date and pax submitted')

# WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID,"enquiry-firstname"))) this doesn't work with the damn phantom driver
time.sleep(3)

inputElement = driver.find_element_by_id("enquiry-firstname")
inputElement.send_keys("Test")
inputElement = driver.find_element_by_id("enquiry-surname")
inputElement.send_keys("Test")
inputElement = driver.find_element_by_id("enquiry-email")
inputElement.send_keys("neal+seleniumtest@travelground.com")
inputElement = driver.find_element_by_id("enquiry-phone")
inputElement.send_keys("1111111111")

# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME,"btn-continue")))

driver.find_element_by_css_selector('#contact-details .btn-continue').click()


try:
	WebDriverWait(driver, 10).until(EC.title_contains("Success!"))
	print (driver.title)
finally:
	driver.quit()

