import random
import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

PHONE = "592434991"
COUNTRY = "Georgia"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

def decline_trackers():
    try:
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[1]/div[2]/button/div[2]/div[2]").click()
        time.sleep(random.randint(2, 4))
    except NoSuchElementException:
        print("No trackers")


def login(phone, country):
    driver.get("https://tinder.com")
    time.sleep(random.randint(3, 7))
    decline_trackers()
    # Click Login Button
    driver.find_element(By.LINK_TEXT, "Log in").click()
    time.sleep(random.randint(3, 6))
    #click login with phone number
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[3]/button").click()
    time.sleep(random.randint(2, 4))
    #chose country
    driver.find_element(By.CSS_SELECTOR, "div[class='D(ib) Bdrsbstart(0)! Bdrststart(0)! Bdendw(1px) Bdends(s) Miw(60px) Px(4px) Mend(8px) C($c-ds-text-inactive) Bdtw(1px) Bdts(s) Bdbw(1px) Bdbs(s) Bdc($c-ds-border-primary) H(48px) Py(12px) Bdrs(4px) Bgc($c-ds-background-secondary)']").click()
    time.sleep(random.randint(2, 4))
    #entering country
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div[2]/div[1]/div/input').send_keys(country)
    time.sleep(random.randint(2, 4))
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div[2]/div[2]/div").click()
    time.sleep(random.randint(2, 4))
    #entering phone number
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div[2]/input').send_keys(phone, Keys.ENTER)
    time.sleep(random.randint(8, 10))
    #verification start puzzle
    driver.find_element(By.XPATH, "//button[contains(text(), 'Start Puzzle')]").click()
    time.sleep(random.randint(7, 15))
    # manual verification that you are not a robot and clicking submit
    driver.find_element(By.XPATH, "//button[text()='Submit']").click()
    time.sleep(random.randint(5, 10)) #for pop-ups

def dislike():
    for item in range (1, 100):
        try:
            driver.find_element(By.XPATH, '//*[@id="main-content"]/div[1]/div/div/div/div[1]/div/div/div[5]/div/div[2]/button/span/span[1]/svg/g/path').click()
            time.sleep(random.randint(2, 5))
        except NoSuchElementException:
            continue

def like():
    for item in range(1, 100):
        try:
            driver.find_element(By.XPATH, '//*[@id="main-content"]/div[1]/div/div/div/div[1]/div/div/div[5]/div/div[4]/button/span/span[1]/svg').click()
            time.sleep(random.randint(2, 5))
        except NoSuchElementException:
            continue


login(phone=PHONE, country=COUNTRY)
dislike()
#like()
driver.quit()
