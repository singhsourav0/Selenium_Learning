from selenium import webdriver

driver = webdriver.Chrome() 

try:
    # Open the website
    driver.get("https://google.com")

    # Get the current URL
    current_url = driver.current_url
    print(f"The current URL of the site is: {current_url}")

finally:
    # Close the browser
    driver.quit()
