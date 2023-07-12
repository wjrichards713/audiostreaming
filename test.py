from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from pyvirtualdisplay import Display
import time
import requests
display = Display(visible=0, size=(1024, 768))
display.start()
opt = Options()
opt.add_argument('--no-sandbox')
opt.add_argument('--auto-accept-camera-and-microphone-capture')

opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.automatic_downloads": 1,
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 0,
    "profile.default_content_setting_values.notifications": 1
})

driver = webdriver.Chrome(options=opt)
url = "https://audio.redenes.org/RedenesDefault/samples/publish_audio.html?debug=false"
driver.get(url)
time.sleep(2)
is_camera_granted = driver.execute_script("return navigator.mediaDevices.getUserMedia({ video: true }).then(() => true).catch(() => false);")
is_microphone_granted = driver.execute_script("return navigator.mediaDevices.getUserMedia({ audio: true }).then(() => true).catch(() => false);")
print("Camera access:", is_camera_granted)
print("Microphone access:", is_microphone_granted)
element = driver.find_element(By.ID, "streamId")
print(element.text)
element.clear()
element.send_keys('python-audio') #stream ID 
print(element.text)
javas = "document.getElementById('start_publish_button').click();"
driver.execute_script(javas)
while 1:
    pass
