from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from bs4 import BeautifulSoup
import pandas as pd
import time
import re

def crawl_kakao_reviews(places, index):
    review_data = pd.DataFrame(columns=['식당이름', '식당리뷰', '식당평점', '닉네임', '유저리뷰수', '유저평점', '작성날짜'])
    
    # Initialize the WebDriver outside of the loop
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)  # Wait for webpage loading up to 5 seconds
    driver.maximize_window()   # Maximize window
    
    for place in places:
        sikdang = place
        try:
            driver.get('https://map.kakao.com/')  # Open the address
            time.sleep(1)  # Wait for the page to load
            
            search = driver.find_element(By.CSS_SELECTOR, "#search\.keyword\.query")
            search.send_keys(sikdang)
            time.sleep(1)  # Allow for delay
            
            # Click unnecessary images that appear on the map
            try:
                img = driver.find_element(By.CSS_SELECTOR, "div.inner_coach_layer")
                img.click()
            except:
                pass  # If the element is not found, just pass
            
            # Click the search button
            searchBtn = driver.find_element(By.CSS_SELECTOR, "#search\.keyword\.submit")
            searchBtn.click()
            
            # Find the review button
            reviewBtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.numberofscore")))
            review_link = reviewBtn.get_attribute("href")
            
            # Go to the review page
            driver.get(review_link)
            time.sleep(1)  # Wait for the page to load
            
            # Scrape the reviews
            page_source = driver.page_source
            soup = BeautifulSoup(page_source, 'html.parser')
            review_lists = soup.select('.list_evaluation > li')
            
            if review_lists:
                review_number = 0
                
                while len(review_lists) > review_number:
                    review_number = len(review_lists)
                    time.sleep(2)  # Wait for initial load
                    
                    if soup.find(class_='txt_more'):
                        button = driver.find_element(By.CLASS_NAME, 'txt_more')
                        while True:
                            try:
                                button.click()
                                time.sleep(2)
                                break
                            except StaleElementReferenceException:
                                button = driver.find_element(By.CLASS_NAME, 'txt_more')
                    
                    page_source = driver.page_source
                    soup = BeautifulSoup(page_source, 'html.parser')
                    review_lists = soup.select('.list_evaluation > li')
                
                for i, review in enumerate(review_lists):
                    comment = review.select('.txt_comment > span')  # 리뷰
                    username = review.select('.txt_username')[0].text  # 리뷰 남긴 유저 닉네임
                    usercount = review.select('.txt_desc')[0].text  # 유저의 리뷰 수
                    userrating = review.select('.txt_desc')[1].text  # 유저의 평균평점
                    rating = str(review.select('.ico_star.inner_star[style]'))
                    rating = int(re.search(r'\d+', rating).group()) / 20  # 유저가 남긴 가게의 평점
                    reviewdate = review.select('.time_write')[0].text  # 리뷰 작성 날짜

                    val = ''

                    if len(comment) != 0:
                        val = comment[0].text
                        new_row = pd.DataFrame({'식당이름': [sikdang], '식당리뷰': [val], '식당평점': [rating], '닉네임': [username], '유저리뷰수': [usercount],
                                                '유저평점': [userrating], '작성날짜': [reviewdate]})
                        review_data = pd.concat([review_data, new_row], ignore_index=True)
            
            else:
                print(f'{sikdang} 리뷰가 없음')
                
        except Exception as e:
            print(f"Error processing {sikdang}: {e}")
            continue
    
    # Save the DataFrame to a CSV file
    review_data.to_csv(f"kakao_review{index}.csv", encoding='utf-8-sig', index=False)
    
    # Quit the driver after completion
    driver.quit()

# Example usage of the function
if __name__ == "__main__":
    places = ['서울특별시 마포구 신촌로 김밥천국', 'another place']
    crawl_kakao_reviews(places, '001')
