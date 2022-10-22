from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep

# Sign into our application using email and pw ----> use same login for desired websites listed
def application_login():
    ##########################################################################################
    # have some type of authentication (maybe w/ 2-step)
    # and this authentication will be reused within the website that Selenium will visit
    ###########################################################################################

    # authenticate with login here to be used


    # for now you can put your own email and pw here to test
    email = 'your_email'
    pw = 'your_password'
    return (email, pw)

def automate_login_to_azure(driver, email, pw):
    if not driver or not email or not pw:
        exit(1)
    
    # url to visit
    base_url = "https://portal.azure.com/#home"
    # driver should wait implicitly for a given duration, for the element under consideration to load
    driver.implicitly_wait(5)
    # to load a given URL in browser window
    driver.get(base_url)
    # fill in email and press enter (must be valid here to continue automation)
    driver.find_element(By.ID, "i0116").send_keys(email + Keys.ENTER)
    # fill in password and press enter (must be valid here to continue automation)
    sleep(2)    # hard wait needed
    driver.find_element(By.ID, 'i0118').send_keys(pw + Keys.ENTER)
    # select no to not stay signed in
    driver.find_element(By.ID, "idBtn_Back").click()
    

def automate_login_to_amazon(driver, email, pw):
    if not driver or not email or not pw:
        exit(1)

    base_url = "https://www.amazon.com/sign/s?k=sign+in"
    driver.implicitly_wait(5)
    driver.get(base_url)
    # redirect to sign-in pg
    driver.find_element(By.ID, "a-autoid-1-announce").click()
    # fill in email and press enter (must be valid here to continue automation)
    driver.find_element(By.ID, "ap_email").send_keys(email + Keys.ENTER)
    # fill in password and press enter (must be valid here to continue automation)
    driver.implicitly_wait(5)
    driver.find_element(By.ID, "ap_password").send_keys(pw + Keys.ENTER)
    # search an item in the search box
    driver.find_element(By.ID, "twotabsearchtextbox").send_keys("Logitech G PRO X SUPERLIGHT" + Keys.ENTER)

def automate_login_to_inzernet(driver, email, pw):
    base_url = "https://inzernet.com/"
    driver.implicitly_wait(5)
    # to load a given URL in browser window
    driver.get(base_url)
    # fill in email and press enter (must be valid here to continue automation)
    driver.find_element("link text","Log in").click()
    driver.find_element(By.ID,"CustomerEmail").send_keys(email)
    driver.find_element(By.ID,"CustomerPassword").send_keys(pw + Keys.ENTER)

def automate_site(driver, email, pw):
    #########################################################################################
    # perform some automation tasks with various sites
    #########################################################################################

    # choose site
    choice = 0
    while choice < 1 or choice > 3:
        choice = int(input('''Choose number corresponding to the website to automate:
        [1]: Microsoft Azure Deployment
        [2]: Amazon
        [3]: Inzernet (Powerlifting)\n'''))

    if choice == 1:
        automate_login_to_azure(driver, email, pw)
    elif choice == 2:
        automate_login_to_amazon(driver, email, pw)
    else:
        automate_login_to_inzernet(driver, email, pw)

def start():
    # login into our application first (required)
    print('Login to application.')
    email, pw = application_login()

    if not email or not pw:
        print('Empty email or password specified. Exiting.')
        exit(1)

    # setup browser (driver) from local download
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    DRIVER_PATH = 'C:\\Users\\evanr\\Downloads\\Project Sample\\drivers\\chromedriver.exe'
    
    driver = webdriver.Chrome(options=options, service=Service(DRIVER_PATH))
    driver.maximize_window()

    # automate a selected site
    automate_site(driver, email, pw)

    driver.close()

start()
