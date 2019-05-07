import sys
import os
import chromedriver_binary
from pathlib import Path
from selenium.common.exceptions import NoAlertPresentException
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def main():
    # Init driver
    driver_options = Options()
    driver_options.add_argument("--headless")
    driver = webdriver.Chrome(options=driver_options)

    # Get login page
    driver.get("https://lukerissacher.com/hexquiz")

    score = 0
    while True:
        as_hex = driver.find_element_by_class_name("question").text.strip()
        as_decimal = int(as_hex, 16)
        as_binary = "{0:#b}".format(as_decimal)[2:]

        driver.find_element_by_id("Answer").send_keys(as_binary)
        driver.find_element_by_id("Submit").click()
        if score % 100 == 0:
            driver.save_screenshot("progress.png")
        driver.find_element_by_id("Submit").click()

        score += 1
        sys.stdout.write("\rscore: {0}".format(score))


if __name__ == "__main__":
    main()
