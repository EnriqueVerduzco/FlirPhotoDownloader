from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time
import os

start_time = time.time()
print ('Starting Script...')
 
#options used for running Chrome
options = webdriver.ChromeOptions()

#headless, comment to view Chrome Open
options.add_argument('headless')
options.add_experimental_option("prefs", {
          "profile.managed_default_content_settings.images": 2,
          "profile.managed_default_content_settings.popups":2,
          "profile.default_content_setting_values.notifications":2,
 #Change Directory
          "download.default_directory": r"/DIRECTORY/",
          "download.prompt_for_download": False,
          "download.directory_upgrade": True,
          "safebrowsing.enabled": True
})


#Open up Chrome Webdriver
driver = webdriver.Chrome(options=options)
print ('Loading Chrome')
driver.implicitly_wait(10) #waits for element to be found for all code 


#Load camera website 
driver.get('IP ADDRESS OF CAMERA')
print ('Webpage loaded')

#Log into the camera
username = driver.find_element_by_name("user_name").send_keys('admin')
password = driver.find_element_by_name("user_password").send_keys("admin")
login = driver.find_element_by_id("button-login").click()
print ('Logged in')

#Take Photo
CapturePhoto = driver.find_element_by_id('button-save-image').click()
print ('Photo has been taken')

time.sleep(5)

#Access Storage page of photos 
storagePage = driver.find_element_by_link_text('STORAGE').click()
print ('Storage Page Accessed')

time.sleep(10)

#Start Downloading photos
link = driver.find_element_by_css_selector('.button.button-storage-save').click()
print('Photo has been downloaded')

time.sleep(5)

#Close Chrome
print ('Chrome Closed')
driver.close()

driver.quit()

print('Program Done')

print ("--- %s seconds ---" % (time.time()- start_time))

#exit()

