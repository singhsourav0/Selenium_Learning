from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

# Path to the ChromeDriver executable
service = Service()  
driver = webdriver.Chrome(service=service)

try:
    # Open YouTube
    driver.get("https://www.youtube.com")
    time.sleep(3) 

    # search_box = driver.find_element(By.NAME, "search_query")
    # search_query = "hindi song"  
    # search_box.send_keys(search_query)
    # search_box.send_keys(Keys.RETURN)
    search_box = driver.find_element(By.CLASS_NAME, "style-scope ytd-searchbox")
    search_query = "hindi song"  
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)
    # Wait for results to load
    time.sleep(5)

    # Print confirmation
    print(f"Searched for: {search_query}")
finally:
    # Close the browser
    driver.quit()
