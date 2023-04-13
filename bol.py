import csv
import time
import uuid
from selenium import webdriver
from selenium.webdriver.common.by import By

#url launch
url = 'https://www.bol.com/nl/nl/l/jassen-dames/47203/' 
driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)

#Accept cookies
cookies_btn = driver.find_element(By.XPATH,'//*[@id="js-first-screen-accept-all-button"]')
cookies_btn.click()

with open('images/Bol_images.csv','w',newline='',encoding='utf-8') as image_file, \
     open('reviews/Bol_reviews.csv','w',newline='',encoding='utf-8') as review_file:
    
     # create the csv writers
    image_fieldnames = ['Bol_images']
    image_writer = csv.DictWriter(image_file, fieldnames=image_fieldnames)

    review_fieldnames = ['Bol_reviews']
    review_writer = csv.DictWriter(review_file, fieldnames=review_fieldnames)

    links = []
    page = 1
    for page in range(5): 
        url_up = 'https://www.bol.com/nl/nl/l/jassen-dames/47203/?page=' +str(page)
        driver.get(url_up)
        boljassen = driver.find_elements(By.CSS_SELECTOR,'a.product-title.product-title--placeholder.px_list_page_product_click.list_page_product_tracking_target')
        #
        for i in boljassen:
            links.append(i.get_attribute('href'))
    #This loop iterates through all the elements found on the first page and adds their "href" attribute to the "links" list.


    print(len(links))# gives the length of the link list
    image_writer.writeheader()
    review_writer.writeheader()    
    for link in links: # goes through all the links in the "links" list and loads each webpage 
        driver.get(link)   


        try:  
            img = driver.find_element(By.CSS_SELECTOR, 'img.js_selected_image.has-zoom')#chooses first div with all the images
            image_url = img.get_attribute('src')#gets the 'picture' so the link
            image_id = str(uuid.uuid4())  # generate a unique identifier
            print(image_url)
            image_writer.writerow({'Bol_images': image_url})#writes img to csv


            time.sleep(3)
            
            revBtn = driver.find_element(By.CSS_SELECTOR, 'div.u-pl--xxs')
            revBtn.click()
            

            time.sleep(2)


            reviews = [] 

            reviewsection = driver.find_element(By.CSS_SELECTOR,'ul.review__list.js-reviews')
            reviews = reviewsection.find_elements(By.CSS_SELECTOR,'div.review__body')


            for review in reviews:
                review_writer.writerow({'Bol_reviews': review.text})
                review_file.flush()

            
        except:
            continue


driver.quit()




