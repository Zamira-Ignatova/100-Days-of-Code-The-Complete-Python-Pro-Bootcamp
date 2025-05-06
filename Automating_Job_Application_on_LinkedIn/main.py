from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
import random


EMAIL = "email"
PASSWORD = "password"

def application_already_submitted():
    try:
        driver.find_element(By.LINK_TEXT, 'Application submitted')
        return True
    except NoSuchElementException:
        return False

def checking_if_the_submitting_contains_one_step():
    job.find_element(By.CSS_SELECTOR, '.jobs-apply-button--top-card').click()
    is_easy_apply_type = job.find_element(By.CSS_SELECTOR, '.artdeco-button__text').text
    if is_easy_apply_type == "Submit application":
        return True
    else:
        return False



chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4124889127&f_AL=true&keywords=sales&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R")
time.sleep(random.randint(3, 7))
#Click Sign in Button
driver.find_element(By.XPATH, '//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button').click()
time.sleep(random.randint(3, 7))
#Sign in
driver.find_element(By.XPATH, '//*[@id="base-sign-in-modal_session_key"]').send_keys(EMAIL)
time.sleep(random.randint(3, 7))
driver.find_element(By.XPATH, '//*[@id="base-sign-in-modal_session_password"]').send_keys(PASSWORD, Keys.ENTER)
time.sleep(random.randint(3, 7))
driver.find_element(By.XPATH, '//*[@id="jobs-apply-button-id"]/span').click()
time.sleep(random.randint(3, 7))
#Applying for all jobs that are "easy apply"
list_of_jobs = driver.find_elements(By.CLASS_NAME, "fQMfqrIjgaszXbRwnhXgiFtHCjjhQrcINSY")
for job in list_of_jobs:
        #send application
        try:
            job.click() #click "easy apply" button
            # check whether application has been submitted previously
            if not application_already_submitted():
                time.sleep(random.randint(3, 10))
                if checking_if_the_submitting_contains_one_step():
                    job.find_element(By.CSS_SELECTOR, '.artdeco-button__text').click()
        except NoSuchElementException:
            continue



