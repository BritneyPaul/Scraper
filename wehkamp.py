from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import uuid
import time

url = 'https://www.wehkamp.nl/heren-kleding-jassen/?pagina=1' 
driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)

cookies = driver.find_element(By.XPATH, '//*[@id="header"]/aside[2]/div/div[1]/div/p[1]/a[1]')
cookies.click()
with open('images/Wehkamp_images.csv', 'w', newline='', encoding='utf-8') as image_file, \
     open('reviews/Wehkamp_reviews.csv', 'w', newline='', encoding='utf-8') as review_file:
     
    # create the csv writers
    image_fieldnames = ['Wehkamp_images']
    image_writer = csv.DictWriter(image_file, fieldnames=image_fieldnames)

    review_fieldnames = ['Wehkamp_reviews']
    review_writer = csv.DictWriter(review_file, fieldnames=review_fieldnames)

    PgNumber = 1 #start at page one
    links = []
    for PgNumber in range(2): 
        url_up = 'https://www.wehkamp.nl/heren-kleding-jassen/?pagina=' +str(PgNumber)
        driver.get(url_up)
        wehkampjassen = driver.find_elements(By.CSS_SELECTOR, 'a.ct-text-primary.display-block')
        for i in wehkampjassen:
            links.append(i.get_attribute('href'))

    print(len(links))
    image_writer.writeheader()
    review_writer.writeheader()    
    for link in links:
        driver.get(link)
        
        try:  
            Img = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[1]/div/div/div[1]/div/div[1]/div[1]/div/div/div[2]/button/figure/img')
            src = Img.get_attribute('src')
            image_id = str(uuid.uuid4())  # generate a unique identifier

            time.sleep(1)
            
            review_button = driver.find_element(By.CSS_SELECTOR, 'button.ReviewSummary__ba-review-link___PH5fZ.type-link-inline.inline-block.rating-link.margin-left-small.color-black-opacity-88')
            review_button.click()
            
            image_writer.writerow({'Wehkamp_images': src})#writes img to csv

            time.sleep(1)


            reviews = [] 

            reviewsection = driver.find_element(By.CSS_SELECTOR, 'div.Reviews__list___KfPgV')      
            reviews = reviewsection.find_elements(By.CSS_SELECTOR, 'p.color-black-opacity-88')



            for review in reviews:
                review_writer.writerow({'Wehkamp_reviews': review.text})
                review_file.flush()

            
        except:
            continue