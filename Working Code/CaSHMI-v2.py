from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import subprocess

# command = '/home/peng/push_button.sh'
# process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
# output, error = process.communicate()

# import time
chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)
# driver = webdriver.Chrome()
driver.get("http://localhost:8000/cashmi/")
driver.maximize_window()
driver.implicitly_wait(15)
# time.sleep(25)
# add_mission = driver.find_element_by_xpath("//button[@class='btn btn-default add-btn']")
# add_mission = driver.find_element_by_class_name('btn.btn-default.add-btn')
add_mission = driver.find_element_by_xpath("//button[normalize-space()='Add Mission']")
add_mission.click()
# add_mission.send_keys(Keys.SPACE)

drag_UAV = driver.find_element_by_id("icon")
drop_UAV = driver.find_element_by_class_name("mission.selected.no-vehicle")

action = ActionChains(driver)
action.click_and_hold(drag_UAV).move_to_element(drop_UAV).perform()

# action.move_to_element(drop_UAV).perform()
driver.implicitly_wait(2)

java_script = "var src=arguments[0],tgt=arguments[1];var dataTransfer={dropEffe" \
"ct:'',effectAllowed:'all',files:[],items:{},types:[],setData:fun" \
"ction(format,data){this.items[format]=data;this.types.append(for" \
"mat);},getData:function(format){return this.items[format];},clea" \
"rData:function(format){}};var emit=function(event,target){var ev" \
"t=document.createEvent('Event');evt.initEvent(event,true,false);" \
"evt.dataTransfer=dataTransfer;target.dispatchEvent(evt);};emit('" \
"dragstart',src);emit('dragenter',tgt);emit('dragover',tgt);emit(" \
"'drop',tgt);emit('dragend',src);"

# driver.implicitly_wait(5)

driver.execute_script(java_script, drag_UAV, drop_UAV)
action.send_keys(Keys.ESCAPE).perform()
driver.close()
