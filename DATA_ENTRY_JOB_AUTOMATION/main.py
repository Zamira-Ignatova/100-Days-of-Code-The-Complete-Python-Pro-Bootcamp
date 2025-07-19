from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

URL_LISTINGS = 'url'
URL_GOOGLE_FORM = 'url'


response = requests.get(URL_LISTINGS)
content = response.text
soup = BeautifulSoup(content, "html.parser")

list_of_link_elements = soup.find_all(name="a", class_="property-card-link")
list_of_links = [link.get('href') for link in list_of_link_elements]

list_of_price_elements = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
list_of_prices = [link.get_text().strip("+/mo") for link in list_of_price_elements]

list_of_address_elements = soup.find_all(name="address")
list_of_addresses = [address.get_text().strip().replace('|', '') for address in list_of_address_elements]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 5)
driver.get(URL_GOOGLE_FORM)

for item in range (0, (len(list_of_addresses) - 1)):
    address = wait.until(expected_conditions.element_to_be_clickable(
        (By.XPATH, "//input[contains(@aria-describedby, 'i2 i3')]")))
    address.click()
    address.clear()
    address.send_keys(f'{list_of_addresses[item]}')

    price = wait.until(expected_conditions.element_to_be_clickable(
        (By.XPATH, "//input[contains(@aria-describedby, 'i7 i8')]")))
    price.click()
    price.clear()
    price.send_keys(f'{list_of_prices[item]}')

    link = wait.until(expected_conditions.element_to_be_clickable(
        (By.XPATH, "//input[contains(@aria-describedby, 'i12 i13')]")))
    link.click()
    link.clear()
    link.send_keys(f'{list_of_links[item]}')

    submit = wait.until(expected_conditions.element_to_be_clickable(
        (By.XPATH, "//span[contains(@class, 'NPEfkd RveJvd snByac')]")))
    submit.click()


driver.quit()
