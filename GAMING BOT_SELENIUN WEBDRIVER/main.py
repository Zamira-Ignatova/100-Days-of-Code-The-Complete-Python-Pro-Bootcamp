from selenium import webdriver
from selenium.webdriver.common.by import By
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
time.sleep(2) # give page time to load


def taking_elements_from_store():
    elements_to_click_to_buy = driver.find_elements(By.CSS_SELECTOR, "#store div")
    list_of_names_of_elements_to_click_on_to_buy = [element.get_attribute("id") for element in elements_to_click_to_buy]
    if "buyElder Pledge" in list_of_names_of_elements_to_click_on_to_buy:
        list_of_names_of_elements_to_click_on_to_buy.remove("buyElder Pledge")
    if "" in list_of_names_of_elements_to_click_on_to_buy:
        list_of_names_of_elements_to_click_on_to_buy.remove("")
    if '' in list_of_names_of_elements_to_click_on_to_buy:
        list_of_names_of_elements_to_click_on_to_buy.remove('')

    print(f"list_of_names_of_elements_to_click_on_to_buy: {list_of_names_of_elements_to_click_on_to_buy}")
    return list_of_names_of_elements_to_click_on_to_buy

def taking_prices_from_store():
    """Extracting prices and in this case all strings with prices has "-" before numbers, so it is a separator and in case they have "," it is going to be replaced"""
    elements_with_string_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
    list_of_prices = []
    for price_element in elements_with_string_prices:
        if "-" or "," in price_element:
            try:
                price_number = int(price_element.text.split("-")[1].strip().replace(",", ""))
                list_of_prices.append(price_number)
            except IndexError:
                print(f"Skipping invalid price string: '{price_element.text}'")
            except AttributeError:
                print(f"Skipping invalid price string: '{price_element.text}'")
        if 666666 in list_of_prices:
            list_of_prices.remove(666666)
    print(f"list_of_prices: {list_of_prices}")
    return list_of_prices

def counting_available_money():
    money = driver.find_element(By.ID, "money").text
    if "," in money:
        money = money.replace(",", "")
        print(f"money_string: {money}")
    money_int = int(money)
    return money_int

def counting_cookies_per_second():
    cookies_per_second_element = driver.find_element(By.ID, "cps")
    cookies_per_second = cookies_per_second_element.text
    print(f"cookies per sec: {cookies_per_second}")
    return cookies_per_second


#main

cookie = driver.find_element(By.ID, "cookie")
time_to_purchase = time.time() + 5 # after 5 sec it is time to make purchases
time_to_stop_the_game = time.time() + (60 * 5) #after 5 minutes the game should be stopped
all_that_can_afford_by_now = {}
while True:
    cookie.click()
    if time.time() > time_to_purchase:

        all_available_items_and_prices = dict(zip(taking_elements_from_store(), taking_prices_from_store()))
        print(f"all_available_items_and_prices: {all_available_items_and_prices}")
        for item, price in all_available_items_and_prices.items():
            if counting_available_money() >= price:
                all_that_can_afford_by_now[price] = item
                print(f"all_that_can_afford_by_now: {all_that_can_afford_by_now}")

        most_expensive_price_can_be_afford = max(all_that_can_afford_by_now)
        print(f"most_expensive_price_can_be_afford: {most_expensive_price_can_be_afford}")
        id_of_element_to_buy = all_that_can_afford_by_now[most_expensive_price_can_be_afford]
        print(f"id_of_element_to_buy: {id_of_element_to_buy}")
        driver.find_element(By.ID, value=id_of_element_to_buy).click()
        time_to_purchase = time.time() + 5

    if time.time() > time_to_stop_the_game:
        counting_cookies_per_second()
        break



