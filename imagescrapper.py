
#References
#https://levelup.gitconnected.com/how-to-download-google-images-using-python-2021-82e69c637d59
#https://ladvien.com/scraping-internet-for-magic-symbols/

#importing the required libraries
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import time
import io
import os
from PIL import Image
import hashlib

 
# Chromedriver path
DRIVER_PATH = 'C:\\Users\Shrimanth\Desktop\Scrapping\chromedriver_win32\chromedriver'

#function to fetch links of the image search 
def fetch_image_urls(search_query:str, max_fetch:int, wd:webdriver, sleep_time:int=1):
    
    def go_to_end(wd):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(sleep_time)

    # Build the Google search query 
    search_url = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"

    # Load the page
    wd.get(search_url.format(q=search_query))

    image_urls = set()
    image_count = 0
    results_start = 0
    while image_count < max_fetch:
        go_to_end(wd)

        # Get all image thumbnail results
        thumbnail_results = wd.find_elements_by_css_selector("img.Q4LuWd")
        number_results = len(thumbnail_results)

        print(f"Found: {number_results} search results. Extracting links from {results_start}:{number_results}")

        for img in thumbnail_results[results_start:number_results]:
            # clicking every thumbnail images
            try:
                img.click()
                time.sleep(sleep_time)
            except Exception:
                continue

            # Extract image links
            actual_images = wd.find_elements_by_css_selector('img.n3VNCb')
            for actual_image in actual_images:
                if actual_image.get_attribute('src') and 'http' in actual_image.get_attribute('src'):
                    image_urls.add(actual_image.get_attribute('src'))

            image_count = len(image_urls)

            if len(image_urls) >= max_fetch:
                print(f"Found: {len(image_urls)} image links, done!")
                break
        else:
            print("Found:", len(image_urls), "image links, looking for more...")
            time.sleep(1)
            return
            load_more_button = wd.find_element_by_css_selector(".mye4qd")
            if load_more_button:
                wd.execute_script("document.search_querySelector('.mye4qd').click();")

        # Moving the result search down 
        results_start = len(thumbnail_results)

    return image_urls

def persist_image(folder_path:str, url:str):
    try:
        image_content = requests.get(url).content

    except Exception as e:
        print(f"ERROR - Could not download {url} - {e}")

    try:
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file).convert('RGB')
        file_path = os.path.join(folder_path, hashlib.sha1(image_content).hexdigest()[:10] + '.jpg')
        with open(file_path, 'wb') as f:
            image.save(f, "JPEG", quality=85)
        print(f"SUCCESS - saved {url} - as {file_path}")
    except Exception as e:
        print(f"ERROR - Could not save {url} - {e}")


def search_and_download(search_term:str, target_path='/Users/Shrimanth/GoogleImages', number_images=70):
    target_folder = os.path.join(target_path, '_'.join(search_term.lower().split(' ')))

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    #with webdriver.Chrome() as wd:
    with webdriver.Chrome(executable_path=DRIVER_PATH) as wd:
        res = fetch_image_urls(search_term, number_images, wd=wd, sleep_time=0.5) #or [] # my changes
 
    for elem in res:
        persist_image(target_folder, elem)
    
# my search string 
search_term = 'Amazon'

search_and_download(
    search_term = search_term,
)
