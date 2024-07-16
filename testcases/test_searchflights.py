import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestFlightSearchAndFilter():
    def test_search_flight(self):
        # launching browser and opening test travel website
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()

        # provide going from location
        wait = WebDriverWait(driver, 10)
        depart_from = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_city']")))
        depart_from.click()
        depart_from.send_keys("New Delhi")
        depart_from.send_keys(Keys.ENTER)

        # Provide going to location
        going_to = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_arrival_city']")))
        going_to.click()
        going_to.send_keys("New York")
        going_to.send_keys(Keys.ENTER)
        search_result = wait.until(EC.presence_of_all_elements_located(By.XPATH, " "))
        for results in search_result:
            if "New York (JSK)" in results.text:
                results.click()
                break

        # to resolve the sync issue
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_date']"))).click()
        all_dates = (wait.until(EC.element_to_be_clickable(By.XPATH, " "))
                     .find_elements(By.XPATH, " "))

        # Select the departure date
        for date in all_dates:
            if date.get_attribute("data-date") == "25/04/2024":
                date.click()
                break

        # Click on flight search button
        driver.find_element(By.XPATH, " ").click()

        # To Handle the dynamic scroll

        # Select the filer of 1 stop
        driver.find_element(By.XPATH, " ").click()
        time.sleep(4)
        allstop1 = wait.until(EC.element_to_be_clickable(By.XPATH, " "))
        print(len(allstop1))

        # Verifiy that the filtered result shows fights have only 1 stop
        for stop in allstop1:
            print("The text is " + stop.text)
            assert stop.text == "1 stop"
            print("assert pass")


testcase1 = TestFlightSearchAndFilter()
testcase1.test_search_flight()
