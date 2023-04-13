import csv
import time
import uuid
from selenium import webdriver
from selenium.webdriver.common.by import By

#url launch
url = 'https://www.decathlon.nl/browse/c0-dames-sportkleding/c1-jassen-dames/_/N-4ydlr.html' 
driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)

#Accepteer cookies

cookie_button = driver.find_element(By.XPATH, '//*[@id="didomi-notice-agree-button"]')
cookie_button.click()

with open('images/Decathlon_images.csv', 'w', newline='', encoding='utf-8') as image_file, \
     open('reviews/Decathlon_reviews.csv', 'w', newline='', encoding='utf-8') as review_file:
     
    # create the csv writers
    image_fieldnames = ['Decathlon_images']
    image_writer = csv.DictWriter(image_file, fieldnames=image_fieldnames)

    review_fieldnames = ['Decathlon_reviews']
    review_writer = csv.DictWriter(review_file, fieldnames=review_fieldnames)

    links = []
    
    decajassen = driver.find_elements(By.CSS_SELECTOR,'a.dpb-product-model-link.svelte-1bclr8g')
    for i in decajassen:
        links.append(i.get_attribute('href'))
        #This loop iterates through all the elements found on the first page and adds their "href" attribute to the "links" list.


    print(len(links))# gives the length of the link list
    image_writer.writeheader()
    review_writer.writeheader()    
    for link in links: # goes through all the links in the "links" list and loads each webpage 
        driver.get(link)   

        try:  
            # Div = driver.find_elements(By.CSS_SELECTOR, 'div.dpb-models.vtmn-relative.svelte-310lux')
            img = driver.find_element(By.XPATH, '//*[@id="app"]/main/article/div[2]/div[2]/div[2]/div/div/section[2]/img')#chooses first div with all the images
            image_url = img.get_attribute('src')#gets the 'picture' so the link
            print(image_url)
            image_writer.writerow({'Decathlon_images': image_url})#writes img to csv


            time.sleep(3)
            
            bekijkrevBtn = driver.find_element(By.XPATH, '//*[@id="app"]/main/article/div[3]/div[2]/div[1]/a/span[2]')
            bekijkrevBtn.click()
            time.sleep(1)
            toonAlleRevBtn = driver.find_element(By.CSS_SELECTOR,'a.cta.cta--desatured.cta--block.svelte-5cgf47') 
            toonAlleRevBtn.click()     

            

            time.sleep(2)


            reviews = [] 

            # toonAlleRevBtn = driver.find_element(By.CSS_SELECTOR,'a.cta.cta--desatured.cta--block.svelte-5cgf47')      
            reviewsection = driver.find_element(By.CSS_SELECTOR,'section.review-list.svelte-1peidim')
            reviews = reviewsection.find_elements(By.CSS_SELECTOR,'p.answer-body.svelte-1v1nczs')



            for review in reviews:
                review_writer.writerow({'Decathlon_reviews': review.text})
                review_file.flush()

            
        except:
            continue


driver.quit()

