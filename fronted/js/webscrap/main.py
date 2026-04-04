from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def scrape_movies_selenium(query):
    driver = webdriver.Chrome()

    url = f"https://mamasapi.vercel.app/search?query={query}"
    driver.get(url)

    time.sleep(3)  # wait for page load

    elements = driver.find_elements(By.CLASS_NAME, "movie-card")

    movies = []

    for el in elements:
        title = el.find_element(By.CLASS_NAME, "title").text
        link = el.find_element(By.TAG_NAME, "a").get_attribute("href")
        image = el.find_element(By.TAG_NAME, "img").get_attribute("src")

        movies.append({
            "title": title,
            "link": link,
            "image": image
        })

    driver.quit()
    return movies
res=scrape_movies_selenium("salaar")
print(res)