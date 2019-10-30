from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

import time

driver = webdriver.Chrome()
driver.get("https://formy-project.herokuapp.com/dragdrop")

#image = driver.findElement(By.id("image"))
image = driver.find_element_by_id("image")
#box = driver.findElement(By.id("box"))
box = driver.find_element_by_id("box")

# Actions actions = new Actions(driver);
# actions.dragAndDrop(image, box).build().perform();

java_script = "var src=arguments[0],tgt=arguments[1];var dataTransfer={dropEffe" \
"ct:'',effectAllowed:'all',files:[],items:{},types:[],setData:fun" \
"ction(format,data){this.items[format]=data;this.types.append(for" \
"mat);},getData:function(format){return this.items[format];},clea" \
"rData:function(format){}};var emit=function(event,target){var ev" \
"t=document.createEvent('Event');evt.initEvent(event,true,false);" \
"evt.dataTransfer=dataTransfer;target.dispatchEvent(evt);};emit('" \
"dragstart',src);emit('dragenter',tgt);emit('dragover',tgt);emit(" \
"'drop',tgt);emit('dragend',src);"

time.sleep(2)
driver.execute_script(java_script, image, box)
time.sleep(2)
driver.quit()