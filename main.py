from selenium import webdriver
import time
from random import seed
from random import randint
from selenium.webdriver.firefox.options import Options

def getRandomTime():
    randTime = randint(3, 5)
    return randTime

def sleepForSomeTime():
    print("Waiting Started!")
    time.sleep(getRandomTime())
    print("Waiting Over")

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(executable_path=r'C:\\Users\\id39r\\Documents\\like-bot\\geckodriver.exe', options=options)

driver.get("http://www.instagram.com")
sleepForSomeTime()

username_input_xpath = "//*[@id='loginForm']/div/div[1]/div/label/input"
password_input_xpath = "//*[@id='loginForm']/div/div[2]/div/label/input"
submit_button_xpath = "//button[@type='submit']"
not_now_button_xpath = "//*[@id='react-root']/div/div/section/main/div/div/div/div/button"
notification_button_xpath = "//*[@id='mount_0_0_EE']/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]"


username = "ashish.id93"
password = "93b@ng.gg"

driver.find_element("xpath", username_input_xpath).send_keys(username)
sleepForSomeTime()

driver.find_element("xpath", password_input_xpath).send_keys(password)
sleepForSomeTime()

driver.find_element("xpath", submit_button_xpath).click()
sleepForSomeTime()

driver.find_element("xpath", not_now_button_xpath).click()
sleepForSomeTime()

driver.find_element("xpath", notification_button_xpath).click()
sleepForSomeTime()