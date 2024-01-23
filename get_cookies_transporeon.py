import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import mysql.connector
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_cookies(username, password):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Open the login page
    login_url = "https://login.transporeon.com/login"
    driver.get(login_url)
    time.sleep(2)
    # Locate the username and password fields by their name, ID, or other attributes
    action = ActionChains(driver)
    EnterMobileNumber = driver.find_element(By.ID, 'emailForm_email-input')
    action.move_to_element(EnterMobileNumber).click(EnterMobileNumber).send_keys(username).perform()
    EnterMobileNumber = driver.find_element(By.ID, 'emailForm_password-input')
    action.move_to_element(EnterMobileNumber).click(EnterMobileNumber).send_keys(password).send_keys(Keys.ENTER).perform()
    time.sleep(2)
    text = str(driver.get_cookies())
    text = text.replace("'", '"')
    my_dict = eval(text)
    cookies = ''
    for dict in my_dict:
        cookies += (dict['name']+'='+dict['value']+', ')
    upload(cookies, username)
    driver.close()
def upload(cookies, username):
    conn = mysql.connector.connect(
        host='dolvera.hostingas.lt',
        user='dolvera_po',
        password='kJzrCH8cCG7d73sG',
        database='dolvera_po'
    )
    cursor = conn.cursor()
    cookies = '"'+cookies+'"'
    if username == 'logistics@dolvera.lt':
        id = 13
    elif username == 'darius@dolvera.lt':
        id = 14
    sql = "UPDATE us_tmsys_table_global_system SET sysval = "+cookies+" WHERE id = "+str(id)
    cursor.execute(sql)

    print(sql)
if __name__ == '__main__':
    get_cookies('logistics@dolvera.lt', 'Vilnius21')
    get_cookies('darius@dolvera.lt', 'darius1976')