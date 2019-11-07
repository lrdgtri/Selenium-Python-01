from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("http://localhost:8000/cashmi/")
driver.maximize_window()
time.sleep(25)
# button = driver.find_element_by_tag_name("button")
# ! button = driver.find_element_by_xpath("(//button)[3]")
# ! button = driver.find_elements_by_tag_name("button")
# texts = [el.text for el in driver.find_elements_by_tag_name("button")]
# button_label = button.get_attribute('textContent')
# button = driver.find_elements_by_xpath("//button[@class='btn btn-default add-btn'][.='Add Mission']")
# button = driver.find_elements_by_xpath("//button[text()='Add Mission']")

# add_mission = driver.find_elements_by_class_name('btn.btn-default.add-btn')
# add_mission.click()
# add_mission.delete()
# add_mission.send_keys("PYCON")
# add_mission.send_keys(Keys.RETURN)

# ! driver.save_screenshot("/home/peng/cashmi_ui.png")
print("Found items:")

# ! print(button)
# print(texts)
text = ''
# ! foundtexts = driver.find_elements_by_tag_name("button")
button = driver.find_elements_by_class_name("btn.btn-default")
for i in button:
    text += i.text + '\n'
print(text)

# for matched_element in button:
#     text = matched_element.text
#     texts.append(text)
#     print(text)
driver.close()

