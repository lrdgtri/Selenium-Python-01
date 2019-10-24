from selenium import webdriver
driver= webdriver.Chrome()
driver.get("file:///F:/Lynda_com/Python_Automation_Testing/CH02/html_code_02.html")
content = driver.find_element_by_class_name('content')
print("My class element is:")
print(content)
driver.close()
