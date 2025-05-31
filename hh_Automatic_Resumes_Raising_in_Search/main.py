from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import  random
from selenium.common.exceptions import StaleElementReferenceException

#CONSTANTS
PHONE = "9854695300"
NUMBER_OF_RESUME_IN_TOTAL = 3

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)


def login(phone):
    """To log in to the hh website"""
    driver.get("https://kolomna.hh.ru")
    time.sleep(random.randint(3, 7))
    # Syntax for more stable xpath by text: //tagname[text()=’exact_text’]
    driver.find_element(By.XPATH, " //a[text()='Войти']").click()
    time.sleep(random.randint(2, 4))
    driver.find_element(By.XPATH, " //div[text()='Профиль соискателя']").click()
    time.sleep(random.randint(2, 4))
    driver.find_element(By.XPATH, " //span[text()='Войти']").click()
    time.sleep(random.randint(2, 4))
    #Syntax for more stable xpath  by attribute //tagname[contains(@attribute, ‘partial_value’)]
    driver.find_element(By.XPATH, "//input[contains(@inputmode, 'tel')]").send_keys(phone, Keys.ENTER)
    time.sleep(random.randint(2, 4))
    try:
        driver.find_element(By.XPATH, "//img[contains(@alt, 'captcha')]")
        time.sleep(random.randint(15, 20))
        driver.find_element(By.XPATH, " //span[text()='Дальше']").click()
        time.sleep(random.randint(10, 12))
    except NoSuchElementException:
        print("There was no captcha")
    try:
        driver.find_element(By.XPATH, "//input[contains(@name, 'code')]").send_keys(Keys.ENTER)
        time.sleep(random.randint(5, 10))
    except NoSuchElementException:
        print("Python displays the error that does not exists in fact")



def raise_a_resume_in_search():
    """making a resume more  visible for employers"""
    driver.find_element(By.XPATH, " //div[text()='Мои резюме']").click()
    time.sleep(random.randint(3, 7))
    while True:
        try:
            raise_button = driver.find_element(By.XPATH, " //span[text()='Поднять в поиске']")
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", raise_button)
            driver.execute_script("arguments[0].click();", raise_button)
            time.sleep(random.randint(2, 5))
        except StaleElementReferenceException:
            continue
        except NoSuchElementException:
            break


login(phone=PHONE)
raise_a_resume_in_search()
driver.quit()

