from selenium import webdriver
driver = webdriver.Firefox()
driver.get("https://www.seleniumhq.org/")
# id q print
#element_id = driver.find_element_by_id("promo")

# name q print
#element_name = driver.find_element_by_name("q")
# heading Xpath What is Selenium print
#element_header_relative = driver.find_elements_by_xpath("//div[@id='mainContent']")
element_header_relative2 = driver.find_elements_by_xpath("//*[@id='mainContent']/h2[1]")
# class selenium-sponsors print
#selenium_sponsors = driver.find_element_by_class_name("selenium-sponsors")
print("My class element is:")
#print(element_id)

#print(element_name)
#print(element_header_relative)
print(element_header_relative2)
#print(selenium_sponsors)
driver.close()