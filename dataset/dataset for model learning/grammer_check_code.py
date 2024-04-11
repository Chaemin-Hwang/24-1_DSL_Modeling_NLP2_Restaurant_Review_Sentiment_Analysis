# check_grammar.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

def check_grammar(text_to_check):
    # Initialize Chrome WebDriver
    dv = webdriver.Chrome()
    try:
        # Go to the Naver grammar check page
        dv.get("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%A7%9E%EC%B6%A4%EB%B2%95%EA%B2%80%EC%82%AC%EA%B8%B0")

        # Find the input box, clear any pre-filled text, and enter the text to check
        elem = dv.find_element(By.CLASS_NAME, 'txt_gray')
        elem.clear()
        elem.send_keys(text_to_check)

        # Click the 'check' button
        elem = dv.find_element(By.CLASS_NAME, "btn_check")
        elem.click()

        # Wait for the result
        time.sleep(1)

        # Parse the result using BeautifulSoup
        soup = BeautifulSoup(dv.page_source, 'html.parser')
        result_text = soup.select_one("p._result_text.stand_txt").text
        print(result_text)
    finally:
        # Close the WebDriver
        dv.quit()

# Example usage of the function
if __name__ == "__main__":
    text = input("Enter text for grammar check: ")
    check_grammar(text)
