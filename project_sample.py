from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

##########################################################################################
# before this, have some type of authentication (maybe w/ 2-step)
# and this authentication will be reused within the website that Selenium will visit
##########################################################################################

base_url = "https://portal.azure.com/#home"
# declare and initialize driver variable
driver = webdriver.Chrome(executable_path="C:\\Users\\evanr\\Downloads\\Project Sample\\drivers\\chromedriver.exe")
# browser should be loaded in maximized window
driver.maximize_window()
# driver should wait implicitly for a given duration, for the element under consideration to load.
# to enforce this setting we will use builtin implicitly_wait() function of our 'driver' object.
driver.implicitly_wait(10) #10 is in seconds
# to load a given URL in browser window
driver.get(base_url)
# fill in email and press enter (must be valid here to continue automation)
driver.find_element(By.ID, "i0116").send_keys("email" + Keys.ENTER)
# to close the browser
driver.close()