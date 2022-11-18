from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep
from flask import Flask, jsonify, request
app = Flask(__name__)
@app.route('/')
def login():
   return "Base"

@app.route('/azure')
def automate_login_to_azure():
    base_url = "https://portal.azure.com/#home"
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='C:\\Users\\lopez\\Downloads\\chromedriver_win32\\chromedriver.exe')
    email = request.args.get('e')
    password = request.args.get('p')
    driver.implicitly_wait(5)
    # to load a given URL in browser window
    driver.get(base_url)
    # fill in email and press enter (must be valid here to continue automation)
    driver.find_element(By.ID, "i0116").send_keys(email + Keys.ENTER)
    # fill in password and press enter (must be valid here to continue automation)
    sleep(2)    # hard wait needed
    driver.find_element(By.ID, 'i0118').send_keys(password + Keys.ENTER)
    # select no to not stay signed in
    driver.find_element(By.ID, "idBtn_Back").click()

    return 'hello'

@app.route('/inzernet')
def automate_login_to_inzernet():
    base_url = "https://inzernet.com/"
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='C:\\Users\\lopez\\Downloads\\chromedriver_win32\\chromedriver.exe')
    email = request.args.get('e')
    password = request.args.get('p')
    driver.get(base_url)
    # fill in email and press enter (must be valid here to continue automation)
    driver.find_element("link text","Log in").click()
    driver.find_element(By.ID,"CustomerEmail").send_keys(email)
    driver.find_element(By.ID,"CustomerPassword").send_keys(password + Keys.ENTER)

    return 'hello'


@app.route('/amazon')
def automate_login_to_amazon():
    base_url = "https://www.amazon.com/sign/s?k=sign+in"
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='C:\\Users\\lopez\\Downloads\\chromedriver_win32\\chromedriver.exe')
    driver.get(base_url)
    email = request.args.get('e')
    password = request.args.get('p')
    driver.implicitly_wait(5)
    driver.get(base_url)
    # redirect to sign-in pg
    driver.find_element(By.ID, "a-autoid-1-announce").click()
    # fill in email and press enter (must be valid here to continue automation)
    driver.find_element(By.ID, "ap_email").send_keys(email + Keys.ENTER)
    # fill in password and press enter (must be valid here to continue automation)
    driver.implicitly_wait(5)
    driver.find_element(By.ID, "ap_password").send_keys(password + Keys.ENTER)
    # search an item in the search box
    driver.find_element(By.ID, "twotabsearchtextbox").send_keys("Logitech G PRO X SUPERLIGHT" + Keys.ENTER)
