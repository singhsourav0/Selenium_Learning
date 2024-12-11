from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time


service = Service()  
driver = webdriver.Chrome(service=service)

try:
    # Open YouTube
    driver.get("https://www.youtube.com")
    time.sleep(3)  # Wait for the page to load

    # Search for Hindi songs
    search_box = driver.find_element(By.NAME, "search_query")
    search_query = "hindi song"
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)  # Wait for results to load

    # Get song titles
    song_titles = driver.find_elements(By.CSS_SELECTOR, "a#video-title")
    titles = [title.text for title in song_titles if title.text.strip() != ""]  # Avoid empty titles

    # Save titles to a file
    with open("hindi_songs.txt", "w", encoding="utf-8") as file:
        for title in titles:
            file.write(title + "\n")

    print(f"Successfully saved {len(titles)} song titles to 'hindi_songs.txt'.")
finally:
    # Close the browser
    driver.quit()
