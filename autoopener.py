
from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.common.exceptions import NoSuchElementException # type: ignore
from selenium.webdriver.chrome.service import Service # type: ignore
from selenium.webdriver.chrome.options import Options # type: ignore
import time

def main():
    chrome_options = Options()
    chrome_options.add_argument("--disable-site-isolation-trials")
    service = Service(chromedriverpath)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    login(driver, asurite, Password123!, 4)

def login(driver, account_sid, auth_token, duopushid):
    try:
        driver.get("https://my.asu.edu/")
        time.sleep(3)
        try:
            # Enter username and password
            driver.find_element(By.CSS_SELECTOR, '#username').send_keys(account_sid)
            driver.find_element(By.CSS_SELECTOR, '#password').send_keys(auth_token)
            driver.find_element(By.CSS_SELECTOR, 'input[name="submit"]').click()
            time.sleep(6)

            # Click on the "Other options" link again if needed
            try:
                other_options_link = driver.find_element(By.LINK_TEXT, "Other options")
                other_options_link.click()
                time.sleep(2)
            except NoSuchElementException:
                print("Other options link not found")

            # Select the authentication method in the 6th row
            try:
                driver.find_element(By.CSS_SELECTOR, f'.auth-method-wrapper:nth-child({duopushid}) .method-body-with-description').click()
                time.sleep(1)
            except NoSuchElementException:
                print(f"Authentication method in row {duopushid} not found")

            time.sleep(20)  # Wait for Duo confirmation

            # Click the "Trust this browser" button
            try:
                trust_browser_button = driver.find_element(By.ID, "trust-browser-button")
                trust_browser_button.click()
                time.sleep(7)
            except NoSuchElementException:
                print("Trust browser button not found")
        except NoSuchElementException:
            print("Aldready Logged in")

    except Exception as e:
        print("Failed")


if __name__ == "__main__":
    main()
